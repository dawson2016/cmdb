from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.http import StreamingHttpResponse
from django.core.context_processors import request
from jinja2 import Template
from k8stemp.exec_cmd import *
from kubernetes import client, config
from deco import require_login
import json
import os
import sys
import urllib2
import cStringIO
import smtplib
import threading 
import time 
import pytz
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
#coding:utf-8
def index(request):
    return render(request,'index/k8stemp.html',locals())
def addconf(request):
    appname=request.POST.get('appname')
    appport=request.POST.get('appport')
    webrpc=request.POST.get('webrpc')
    filepath='/tempfile/k8s'+str(webrpc)
    f=open(os.getcwd()+str(filepath),'r')
    template = Template(f.read())
    myk8s=template.render(appname=appname,appport=appport)
    f.close()
    return HttpResponse(myk8s)
def sendpicmail(request,url,towho):
    message = MIMEMultipart('related') 
    message['From'] = Header('huanshuo-URL-alert','utf-8')
    message.attach(MIMEText('<b>URL screenshot</b><br><img src="cid:image1"><br>', 'html', 'utf-8'))
    f = cStringIO.StringIO(urllib2.urlopen(url).read())
    msgImage = MIMEImage(f.read())
    msgImage.add_header('Content-ID', '<image1>')
    message.attach(msgImage)
    f.close()
    subject = 'zabbix URL info'
    message['Subject'] = Header(subject,'utf-8')
    sender = '87075387@qq.com'
    receiver = towho
    smtpserver = 'smtp.qq.com'
    username = '87075387@qq.com'
    password = 'dwienqivqfbxbifa'
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    smtp.ehlo()
    smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, message.as_string())
def capture(request):
    urlname=request.GET.get('url','www.baidu.com')
    protoname=request.GET.get('proto','http')
    imgpath="/tmp/"+urlname+".png"
    new_thread = threading.Thread(target=url_capture,args=(urlname,imgpath,protoname,))
    new_thread.setDaemon(True)
    new_thread.start()
    image_data = open(imgpath,"rb").read()
    return HttpResponse(image_data,content_type="image/png")
@require_login
def ingconf(request):
    	ns=request.GET.get('ns','all')
	config.load_kube_config('/root/.kube/config')
	v1=client.CoreV1Api()
	v2=client.ExtensionsV1beta1Api()
	allns=[ns]
	allres=[]
	if ns=='all':
		allns=[]
		nss=v1.list_namespace()
		for ns in nss.items:
			if ns.metadata.name not in ['kube-public','kube-system','weave','default']:
				allns.append(ns.metadata.name)
	for ns in allns:
		ings=v2.list_namespaced_ingress(ns)
		for ing in ings.items:
			multihost=[]
			for rule in ing.spec.rules:
				multihost.append(rule.host)
			allres.append({'ns':ns,'ingname':ing.metadata.name,'host':','.join(multihost),'servicename':rule.http.paths[0].backend.service_name,'serviceport':rule.http.paths[0].backend.service_port})
	return render(request,'index/k8sing.html',locals())
def ingscan(request):
    	ns=request.GET.get('ns','all')
	config.load_kube_config('/root/.kube/config')
	v1=client.CoreV1Api()
	v2=client.ExtensionsV1beta1Api()
	allns=[ns]
	allres={}
	if ns=='all':
		allns=[]
		nss=v1.list_namespace()
		for ns in nss.items:
			if ns.metadata.name not in ['kube-public','kube-system','default']:
				allns.append(ns.metadata.name)
	for ns in allns:
		ings=v2.list_namespaced_ingress(ns)
		nsarr=[]
		for ing in ings.items:
			multihost=[]
			for rule in ing.spec.rules:
				multihost.append(rule.host)
			nsarr.append(','.join(multihost))
		allres[ns]=nsarr
	return JsonResponse(allres)
def ingapi(request):
	config.load_kube_config('/root/.kube/config')
	v2=client.ExtensionsV1beta1Api()
    	ns=request.POST.get('ns')
    	ing_name=request.POST.get('ing_name')
    	host=request.POST.get('host')
    	service_name=request.POST.get('service_name')
    	service_port=request.POST.get('service_port')
        rules=[]
	for i in host.split(','):
		rules.append({'host':i, 'http': {'paths': [{'path': '/', 'backend': {'serviceName': service_name, 'servicePort': int(service_port)}}]}})	
	body={'spec': {'rules':rules}, 'apiVersion': 'extensions/v1beta1', 'metadata': {'namespace':ns,'name':ing_name}}
	res=v2.replace_namespaced_ingress(ing_name,ns,body)
	return HttpResponse(res)
def k8slog(request):
        ns=request.GET.get('ns','all')
        config.load_kube_config('/root/.kube/config')
        v1=client.CoreV1Api()
        v2=client.ExtensionsV1beta1Api()
        allns=[ns]
        allres=[]
	bjtz = pytz.timezone('Asia/Shanghai')
        if ns=='all':
                allns=[]
                nss=v1.list_namespace()
                for ns in nss.items:
                        if ns.metadata.name not in ['kube-public','kube-system','default']:
                                allns.append(ns.metadata.name)
        for ns in allns:
                pods=v1.list_namespaced_pod(ns)
                for pod in pods.items:
			mypodstatus=pod.status.container_statuses[0].state
			container_id=pod.status.container_statuses[0].image.split(':')[1]
			if mypodstatus==None:
				podstatus=None
			else:
				podstatus=mypodstatus
			allres.append({'ns':ns,'podname':str(pod.metadata.name),'create_time':str(pod.metadata.creation_timestamp.astimezone(bjtz))[:-6],'podstatus':podstatus,'container_id':container_id})
        return render(request,'index/k8slog.html',locals())
        #return HttpResponse(allres)
def k8slogapi(request):
    ns= request.GET.get('ns')
    pod= request.GET.get('pod')
    times= request.GET.get('times',3600)
    lines= request.GET.get('lines',1000)
    config.load_kube_config('/root/.kube/config')
    v1=client.CoreV1Api()
    logres=v1.read_namespaced_pod_log(pod,ns,since_seconds=times)
    if times==3600:
        logres=v1.read_namespaced_pod_log(pod,ns,tail_lines=lines)
    if logres=='':
	logres='no newer log produced,pls wait...'
    return HttpResponse(logres)
def k8slogdownapi(request):
    ns= request.GET.get('ns')
    pod= request.GET.get('pod')
    config.load_kube_config('/root/.kube/config')
    v1=client.CoreV1Api()
    r=v1.read_namespaced_pod_log(pod,ns,_preload_content=False).stream()
    filename=str(ns)+str(pod)+'-log.txt'
    response = StreamingHttpResponse(r)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename)
    return response
