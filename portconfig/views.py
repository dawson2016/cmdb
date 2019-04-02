#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from pip._vendor.requests.api import request
from portconfig.models import Portlist
from index.models import Hostlist
from portconfig.exec_cmd import remotecmd,iptables_cmd,sync_iptables
from index.deco import require_login
import socket
import time
import json
# Create your views here.
@require_login
def port(request):
    data = Portlist.objects.all()
    data=data.order_by('ipaddr')
    Portlist.objects.filter(wanport=22).update(status=2)
    '''for i in data:
        if not porttest('180.76.162.41',i.wanport):
            Portlist.objects.filter(wanport=i.wanport).update(status=0)'''
    return render(request,'index/port.html',locals())
def syncport(request):
    data=sync_iptables()
    data=json.loads(data)
    synclist=[]
    for i in data:
        Portlist.objects.filter(wanport=i['wan']).update(status=i['status'])
        synclist.append(i['wan'])
    Portlist.objects.exclude(wanport__in=synclist).delete()
    return StreamingHttpResponse('ok')
def addport(request):
    ipaddr=request.POST.get('ipaddr')
    lanport=request.POST.get('lanport')
    wanport=request.POST.get('wanport')
    checkip = Hostlist.objects.filter(lanip=ipaddr)
    checkwanport = Portlist.objects.filter(wanport=wanport)
    if checkwanport :
        return HttpResponse('外网端口已被使用')
    elif not checkip:
        return HttpResponse('ip地址无效')
    else:
        id=Hostlist.objects.values("id").filter(lanip=ipaddr)
        Portlist.objects.create(ipaddr_id=id[0]['id'],wanport=wanport,lanport=lanport,status=1)
        res=remotecmd(ipaddr,wanport,lanport)
        return HttpResponse(res)
def editport(request):
    ipaddr=request.POST.get('ipaddr')
    wan=request.POST.get('wanport')
    action=request.POST.get('action')
    if  int(action) == 1:
        res=iptables_cmd(ipaddr,wan,action)
        Portlist.objects.filter(wanport=wan).update(status=0)
        return HttpResponse('close')
    else:
        res=iptables_cmd(ipaddr,wan,action)
        Portlist.objects.filter(wanport=wan).update(status=1)
        return HttpResponse('open')
    '''statuscode = 1^int(action)
    if  res == 'ok':
        Portlist.objects.filter(wanport=wan).update(status=statuscode)
        return HttpResponse('200')
    else:
        Portlist.objects.filter(wanport=wan).update(status=statuscode)
        return HttpResponse('500')
    '''
def portusage(request):
    wan=request.POST.get('wan')
    usage=request.POST.get('usage')
    Portlist.objects.filter(wanport=wan).update(comment=usage)
    return HttpResponse('ok')
def porttest(ip,port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(1)
    try:
        sk.connect((ip,port))
        return True
    except Exception:
        return False
    sk.close()
