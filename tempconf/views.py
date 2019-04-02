from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import request
import json
import os
from jinja2 import Template
from tempconf.exec_cmd import *
#coding:utf-8
def index(request):
    return render(request,'index/temp.html',locals())
def addconf(request):
    domain=request.POST.get('domain')
    backend=request.POST.get('backend')
    f=open(os.getcwd()+'/tempfile/nginx','r')
    template = Template(f.read())
    mynginx=template.render(domain=domain,backend=backend)
    f.close()
    return HttpResponse(mynginx)
def pushconf(request):
    conf_file=request.POST.get('conf_file')
    file_name=request.POST.get('file_name')
    serverip=request.POST.get('serverip')
    f=open('/tmp/'+file_name,'w')
    f.write(conf_file)
    f.close()
    #push server
    res=push_nginx(serverip,file_name)
    return HttpResponse(res)
