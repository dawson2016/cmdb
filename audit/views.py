from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Q
from django.http import StreamingHttpResponse
from models import Audit
from django.contrib.auth import authenticate
from deco import require_login
from audit.exec_cmd import mysendmail
import json
import threading
import time
@require_login
def audit_list(request):
    data=Audit.objects.all().order_by('-status')
    print data
    return render(request,'index/audit.html',locals())
def auditapi(request):
    if request.method == 'GET':
        proname=request.GET.get('proname')
        proenv=request.GET.get('proenv')
        res=Audit.objects.filter(Q(proname=proname) & Q(proenv=proenv))
        if len(res)==0:
            return HttpResponse('null')
        data=res[0].status
        return HttpResponse(data)
    elif request.method == 'POST':
        proname=request.POST.get('proname')
        proenv=request.POST.get('proenv')
        action=request.POST.get('action')
        if  action == 'accept':
            Audit.objects.filter(Q(proname=proname) & Q(proenv=proenv)).update(status=1)
            return HttpResponse('accept ok')
        elif  action == 'deny':
            Audit.objects.filter(Q(proname=proname) & Q(proenv=proenv)).update(status=0)
            return HttpResponse('deny ok')
        elif  action == 'reset':
            Audit.objects.filter(Q(proname=proname) & Q(proenv=proenv)).update(status=2)
            myurl='https://cmdb.hseduyun.net/auditlist/'
            mesg=str(proname)+str(' ')+str(proenv)+' online need audit'+'\n'+'audit url : '+str(myurl)
            new_thread = threading.Thread(target=mysendmail,args=(mesg,))
            new_thread.setDaemon(True)
            new_thread.start()
            return HttpResponse('reset ok')
        else:
            return HttpResponse('null')
def auditsleep(request):
        time.sleep(3)
        return HttpResponse('wait 3s')

