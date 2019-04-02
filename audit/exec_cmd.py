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
MAIL_FROM = '87075387@qq.com'
def smg(info):
    ran=random.randint(100000, 999999)
    sh=hashlib.sha256()
    smgurl='https://yun.tim.qq.com/v5/tlssmssvr/sendmultisms2?sdkappid=1400036582&random='+str(ran)
    user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    ak='c37cb436ee7a250512c3ab47d54509cb'
    telnum="13633445821,17610168211"
    tel=["13633445821","17610168211"]
    #telnum="13633445821"
    #tel=["13633445821"]
    mytime=int(time.time())
    mydata='appkey=c37cb436ee7a250512c3ab47d54509cb&random='+str(ran)+'&time='+str(mytime)+'&mobile='+str(telnum)
    sh.update(mydata)
    mysig=sh.hexdigest()
    values = {"ext":"","extend":"","params": info,"sign": "寰烁","tel":[{"nationcode":"86", "mobile": pn} for pn in tel], "sig":mysig,"tpl_id": 231832,"time":mytime}
    myheaders = {"Content-Type": "application/json","User-Agent":user_agent }
    r = requests.post(url=smgurl,data=json.dumps(values),headers=myheaders)
    print r.content
def mysendmail(data):
    message = MIMEText(data,'plain','utf-8')
    message['From'] = Header('huanshuo-online-notice','utf-8')
    towho=['87075387@qq.com','632030580@qq.com','1290192631@qq.com']
    subject = 'online notice'
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
