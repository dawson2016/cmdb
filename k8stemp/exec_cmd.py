#!/usr/bin/env python
#coding:utf-8
import subprocess
from kubernetes import client, config
import json
import redis
import time
def url_capture(urlname,imgpath,proto):
    subprocess.Popen(["phantomjs","/root/phantomjs/jietu.js",urlname,imgpath,"1366px*1500px",proto],stdout=subprocess.PIPE)
def k8slog_out(ns,pod):
    config.load_kube_config('/root/.kube/config')
    v1=client.CoreV1Api()
    line_num=0
    r=redis.StrictRedis(host='192.168.0.27', port=6379,password='Hs123#')
    logres=v1.read_namespaced_pod_log(pod,ns,since_seconds=1800)
    print logres
    print type(logres)
    r.publish(pod,logres)
    #while True:
        #line=logres.readline()
        #line_num+=1
        #r.publish(pod,logres)
        #if line_num==5000:
        #    r.publish(pod,'###############1000 lines log has displayed over or No logs are produced !!!#######################')
        #    break
    print 'pod over'
