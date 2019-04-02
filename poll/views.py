from __future__ import absolute_import
from django.shortcuts import render
from django.http import HttpResponse
from poll.models import Polls
from poll.tasks import add 
import json
import time
import os
# Create your views here.
def pv(request):
    #res=add.delay(3,5)
    #data=Polls.objects.all()
    return render(request,'index/pv.html',locals())
    #res=AsyncResult(task_id='442c2efa-bf03-45e0-aa8d-6140656109a3')
    #return HttpResponse(res)
def pvsum(request):
    data=Polls.objects.all()
    for i in data:
        data=i.pv
    return HttpResponse(data)
def sign(request):
    return render(request,'index/mytest.html')
def pvapi(request):
    #reset=request.GET.get('reset')
    pvsign=request.POST.get('sign')
    #data=Polls.objects.all()
    #nowpv=data[0].pv
    #if pvsign==('phone'):
    #    mypv=int(nowpv)+1
    #    Polls.objects.filter(id=1).update(pv=mypv)
    #if reset=='1':
    #    Polls.objects.filter(id=1).update(pv=0)
    output = os.popen('python /root/script/auto-study.py')	
    print output
    return HttpResponse('ok')
