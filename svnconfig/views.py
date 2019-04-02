from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import request
from svnconfig.models import User,UserGroup,Project
from svnconfig.exec_cmd import *
from django.core import serializers
from index.deco import require_login
import json
# Create your views here.
#coding:utf-8
@require_login
def svnconf(request):
    pname = Project.objects.all().order_by('name')
    gname = UserGroup.objects.all().order_by('name')
    uname = User.objects.all().order_by('name')
    return render(request,'index/svn.html',locals())
def svnadd(request):
    proname=request.POST.get('proname')
    username=request.POST.get('username')
    groupname=request.POST.get('groupname')
    if proname:
        Project.objects.create(name=proname,perm='rw',comment=1)
        addgtp(proname,'nogroup')
        #shell svnadmin create proname
        return HttpResponse('ok')
    elif username:
        #User.objects.create(name=username,role='1')
        res=User.objects.filter(name=username)
        if len(res)!=0:
            return HttpResponse('the name has used !!')
        else:
            User.objects.create(name=username,role='1')
            #shell htpasswd username
            addutg('nogroup',username)
        return HttpResponse('ok')
    elif groupname:
        UserGroup.objects.create(name=groupname,comment=1)
        #shell configparse add groupname
        addutg(groupname,'nouser')
        return HttpResponse('ok')
    else:
        return HttpResponse('error')
def svninfo(request):
    user=request.POST.get('username')
    groupname=request.POST.get('groupname')
    if groupname:
        a=UserGroup.objects.get(name=groupname)
        res=a.project_set.all()
        json_data = serializers.serialize("json", res)
        return HttpResponse(json_data)
    elif user:
        a=User.objects.get(name=user)
        res=a.group.all()
        json_data = serializers.serialize("json", res)
        return HttpResponse(json_data)
    else:
        return HttpResponse('error')
def svnutg(request):
    user=request.POST.get('user')
    group=request.POST.get('group')
    a=User.objects.get(name=user)
    b=UserGroup.objects.get(name=group)
    a.group.add(b)
    #shell user join group
    addutg(group,user)
    return HttpResponse('ok')
def svndutg(request):
    user=request.POST.get('user')
    group=request.POST.get('group')
    a=User.objects.get(name=user)
    b=UserGroup.objects.get(name=group)
    res=a.group.filter(name=group)
    if len(res)==0:
        return HttpResponse('error') 
    else:
        a.group.remove(b)
        delutg(group,user)
        #shell group kick user
        return HttpResponse('ok')
def svndeluser(request):
    user=request.POST.get('user')
    User.objects.filter(name=user).delete()
    deluser(user)
    return HttpResponse('ok')
def svngtp(request):
    group=request.POST.get('group')
    pro=request.POST.get('pro')
    a=Project.objects.get(name=pro)
    b=UserGroup.objects.get(name=group)    
    a.group.add(b)
    #shell group join project
    addgtp(pro,group)
    return HttpResponse('ok')

def svndgtp(request):
    group=request.POST.get('group')
    pro=request.POST.get('pro')
    a=Project.objects.get(name=pro)
    b=UserGroup.objects.get(name=group)    
    res=a.group.filter(name=group)
    if len(res)==0:
        return HttpResponse('error') 
    else:
        a.group.remove(b)
        delgtp(pro,group)
        #shell project kick group
        return HttpResponse('ok')
def syncsvn(request):
    data=sync_svn()
    data=json.loads(data)
    syncpro=[]
    for i in data:
        if i['name'].split(':')[0]!='groups':
            syncpro.append(i['name'].split(':')[0])
    Project.objects.exclude(name__in=syncpro).delete()
    userdata=sync_user()
    syncuser=[]
    data=json.loads(userdata)
    for i in data:
        syncuser.append(i['name'])
    User.objects.exclude(name__in=syncuser).delete()
    userdata=sync_group()
    syncgroup=[]
    syncuser_group=[]
    data=json.loads(userdata)
    for i in data:
        syncgroup.append(i['gname'])
        syncuser_group.append([i['gname'],[i['member']]])
    UserGroup.objects.exclude(name__in=syncgroup).delete()
    for usertgroup in syncuser_group: 
        b=UserGroup.objects.filter(name=usertgroup[0])
        if len(b)==0:
            UserGroup.objects.create(name=usertgroup[0],comment=1)
        b=UserGroup.objects.get(name=usertgroup[0])
        for user in usertgroup[1]:
            for username in user[0].split(','):
                a=User.objects.filter(name=username)
                if len(a)==0:
                    User.objects.create(name=username,role=1)
                a=User.objects.get(name=username)
                res=a.group.filter(name=usertgroup[0])
                if not res:
                    a.group.add(b)
    userdata=sync_pro()
    syncgroup_pro=[]
    data=json.loads(userdata)
    for i in data:
        syncgroup_pro.append([i['pname'],i['gmem']])
    for grouptpro in syncgroup_pro: 
        a=Project.objects.filter(name=grouptpro[0])
        if len(a)==0:
            Project.objects.create(name=grouptpro[0],perm='rw',comment=1)
        a=Project.objects.get(name=grouptpro[0])
        for gname in grouptpro[1]:
            b=UserGroup.objects.filter(name=gname)
            if len(b)==0:
                UserGroup.objects.create(name=gname,comment=1)
            b=UserGroup.objects.get(name=gname)
            res=a.group.filter(name=gname)
            if not res:
                a.group.add(b)
    return HttpResponse('ok')           
