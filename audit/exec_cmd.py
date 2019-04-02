#!/usr/bin/env python
#coding:utf-8
import sys
import requests
import time 
import random
import json
import hashlib
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.exceptions import ReadTimeout,ConnectionError,RequestException
import smtplib
from email.mime.text import MIMEText
from email.header import Header
default_encoding = 'utf-8'
MAIL_FROM = 'xxx@qq.com'
def smg(info):
    ran=random.randint(100000, 999999)
    sh=hashlib.sha256()
    smgurl='https://yun.tim.qq.com/v5/tlssmssvr/sendmultisms2?sdkappid=1400036582&random='+str(ran)
    user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    ak='xxx'
    telnum="xxx"
    tel=["xxx"]
    mytime=int(time.time())
    mydata='appkey=xxx&random='+str(ran)+'&time='+str(mytime)+'&mobile='+str(telnum)
    sh.update(mydata)
    mysig=sh.hexdigest()
    values = {"ext":"","extend":"","params": info,"sign": "xx","tel":[{"nationcode":"86", "mobile": pn} for pn in tel], "sig":mysig,"tpl_id": 231832,"time":mytime}
    myheaders = {"Content-Type": "application/json","User-Agent":user_agent }
    r = requests.post(url=smgurl,data=json.dumps(values),headers=myheaders)
    print r.content
def mysendmail(data):
    message = MIMEText(data,'plain','utf-8')
    message['From'] = Header('xxx','utf-8')
    towho=['xxx@qq.com','xx@qq.com']
    subject = 'online notice'
    message['Subject'] = Header(subject,'utf-8')
    sender = 'xx@qq.com'
    receiver = towho
    smtpserver = 'smtp.qq.com'
    username = 'xx@qq.com'
    password = 'xxxx'
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    smtp.ehlo()
    smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, message.as_string())
