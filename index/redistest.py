#!/usr/local/bin/python2.7
#coding:utf-8
import redis
r=redis.StrictRedis(host='192.168.0.27', port=6379,password='Hs123#')
r.publish(str(dockerid),'ok')

