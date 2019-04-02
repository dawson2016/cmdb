from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import StreamingHttpResponse
from bcc_api import *
from bcm_api import *
from index.exec_cmd import *
from models import Hostlist
from django.contrib.auth import authenticate
from deco import require_login
import json,time,datetime
import os
import threading 
import requests
import MySQLdb

# Create your views here.
def page_not_found(request):
    return render(request,'index/404.html')
def login(request):
    return render(request,'index/login.html')
def logincheck(request):
    name=request.POST.get('username')
    password=request.POST.get('password')
    checkres = authenticate(username=name, password=password)
    if checkres != None:
        request.session['IS_LOGIN'] = True
        return HttpResponse('ok')
    else:
        return HttpResponse('error')
def bcc_list():
    credentials = BceCredentials("xxx","xxx")
    http_method = "GET"
    path = "/v2/instance"
    headers = {"host": "bcc.bj.baidubce.com",
    "content-Type":"application/json",
    "x-bce-date":get_canonical_time()}
    params = {}
    timestamp = 0
    result = sign(credentials, http_method, path, headers, params, timestamp,1800)
    url = 'http://bcc.bj.baidubce.com/v2/instance'
    req = urllib2.Request(url)
    req.add_header('Authorization',result)
    req.add_header("content-Type","application/json")
    req.add_header("x-bce-date",get_canonical_time())
    r = urllib2.urlopen(req)
    html = r.read()
    data = json.loads(html)
    data = data['instances']
    for i in data:
        if not Hostlist.objects.filter(lanip=i['internalIp']):
            Hostlist.objects.create(name=i['name'],lanip=i['internalIp'],wanip=i['publicIp'],
                                    status=i['status'],cpu=i['cpuCount'],mem=i['memoryCapacityInGB'],usedate=i['createTime'][:10])
    return 'ok'
   #return render(request,'index/list.html',{'data':data['instances']})
@require_login
def list(request):
    bcc_list()
    #if offset=='':offset=1
    #start=(int(offset)-1)*5
    #end=start+5
    alldata=Hostlist.objects.all().order_by('lanip')
    count=alldata.count()
    #data=alldata[start:end]
    data=alldata
    #pages=range(1,divmod(count, 5)[0]+2)
    #start+=1
    return render(request,'index/index.html',locals())
def hostselect(request):
    myos=request.GET.get('ostype')
    data=Hostlist.objects.filter(ostype=myos).values_list('lanip','instanceid')
    jsondata=[]
    for i in data:
        jsondata.append([i[0],i[1]])
    return HttpResponse(json.dumps(jsondata))
def edit(request):
    myid=request.POST.get('id')
    myusage=request.POST.get('usage')
    Hostlist.objects.filter(instanceid=myid).update(usage=myusage)
    return HttpResponse('ok')
def docker(request):
    return render(request,'index/docker.html')
def log(request):
    lanip= request.GET.get('ip')
    dockername= request.GET.get('name')
    new_thread = threading.Thread(target=log_out,args=(lanip,dockername,))
    new_thread.setDaemon(True)
    new_thread.start()
    return HttpResponse('ok')
def postmanapi(request):
    testurl= request.GET.get('testurl')
    try:
        r = requests.get(testurl,verify=False)
    except requests.exceptions.ConnectionError:
        return HttpResponse('Connection Error:URL is error or API server is down,Contact the OPS !! ')
    except requests.exceptions.ChunkedEncodingError:
        return HttpResponse('An Unknow Error Happened')
    except:
        return HttpResponse('What the fuck is this url ??')
    try:
	data=r.json()
    except:
        return HttpResponse('What the fuck is this apiserver ??')
    return JsonResponse(r.json()) 
def postman(request):
    return render(request,'index/postman.html')
def mysqlhandler(request):
    return render(request,'index/mysql.html',locals())
def mysqlapi(request):
    ip=request.POST.get('ip')
    pwd=request.POST.get('pwd')
    gname=request.POST.get('gname')
    gpwd=request.POST.get('gpwd')
    gdb=request.POST.get('gdb')
    qx=request.POST.get('qx')
    print ip,pwd,gname,gpwd,gdb,qx
    #sql='grant on .* to ''@'' identified by '''
    db = MySQLdb.connect(ip,"root", pwd, charset='utf8') 
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    return HttpResponse(data) 
def upload(request):
    return render(request,'index/upload.html')
def uploadapi(request):
    apkfile=request.FILES.get('upfile')
    apkname=request.POST.get('upname')
    if apkfile == None:
        return HttpResponse('file not select !!')
    else:
        systmp = open(os.path.join("/tmp",apkname),'wb+') 
        for chunk in apkfile.chunks():  
            systmp.write(chunk)  
        systmp.close()  
        scp_put(apkname)
        return HttpResponse("upload success!!") 

@require_login
def hostinfo(request):
    return render(request,'index/graph.html')
def utc2stamp(date):
    timeArray = time.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
    date=int(time.mktime(timeArray))
    return date
def stamp2utc(stamp):
    dt=datetime.datetime.utcfromtimestamp(int(stamp))
    utc=datetime.datetime.strftime(dt,'%Y-%m-%dT%H:%M:%SZ')
    return utc
def bcm_data_api(request,instanceid,monitortype,datatype='average'):
    headers = {}
    accesskey = 'xxx'
    secretkey = 'xxx'
    headers['Content-Type'] = 'application/json'
    headers['Host'] = 'bcm.bj.baidubce.com'
    start1=int(time.time())-432000
    end1=int(time.time())
    start=stamp2utc(start1)
    end=stamp2utc(end1)
    query_params = {
        'statistics[]': datatype,
        'dimensions': 'InstanceId:'+str(instanceid),
        'startTime': start,
        'endTime': end,
        'periodInSecond': 60
    }
    request = {
        'method': 'GET',
        'uri': '/json-api/v1/metricdata/xxx/BCE_BCC/'+str(monitortype),
        'params': query_params,
        'headers': headers
    }
    signer = BceSigner(accesskey, secretkey)
    auth = signer.gen_authorization(request)
    headers['Authorization'] = auth
    url = "http://bcm.bj.baidubce.com/json-api/v1/metricdata/xxx/BCE_BCC/"+str(monitortype)
    response = requests.get(url, headers=headers, params=query_params)
    if response.status_code==200:
        data=response.json()["dataPoints"]
        biglist=[]
        for i in data:
            biglist.append([utc2stamp(i['timestamp']),i.setdefault('average',None)])
    else:
        data='data is null'
    data=json.dumps(biglist)
    return HttpResponse(data)
