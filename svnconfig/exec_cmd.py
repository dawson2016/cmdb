#!/usr/bin/env python
#coding:utf-8
import paramiko
def addutg(group,user):
	hostname='192.168.0.36'
	port=22
	username='root'
	password='huanshuo#888'
        para=group+' '+user
        cmd = '/usr/bin/python /root/addgroup.py '+' '+para
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname,username=username,password=password,allow_agent=False,look_for_keys=False)
	stdin, stdout, stderr = ssh.exec_command(cmd)
        channel = stdout.channel
	data = stdout.readlines()     
        #print stdin,stdout,stderr
	ssh.close()
        return data
def delutg(group,user):
	hostname='192.168.0.36'
	port=22
	username='root'
	password='huanshuo#888'
        para=group+' '+user
        cmd = '/usr/bin/python /root/delutg.py '+' '+para
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname,username=username,password=password,allow_agent=False,look_for_keys=False)
	stdin, stdout, stderr = ssh.exec_command(cmd)
        channel = stdout.channel
	data = stdout.readlines()     
        #print stdin,stdout,stderr
	ssh.close()
        return data
def deluser(user):
	hostname='192.168.0.36'
	port=22
	username='root'
	password='huanshuo#888'
        cmd = '/usr/bin/python /root/deluser.py '+' '+user
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname,username=username,password=password,allow_agent=False,look_for_keys=False)
	stdin, stdout, stderr = ssh.exec_command(cmd)
        channel = stdout.channel
	data = stdout.readlines()     
        #print stdin,stdout,stderr
	ssh.close()
        return data
def addgtp(pro,group):
	hostname='192.168.0.36'
	port=22
	username='root'
	password='huanshuo#888'
        para=pro+' '+'@'+group
        cmd = '/usr/bin/python /root/section.py '+' '+para
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname,username=username,password=password,allow_agent=False,look_for_keys=False)
	stdin, stdout, stderr = ssh.exec_command(cmd)
        channel = stdout.channel
	data = stdout.readlines()     
        print data
        #print stdin,stdout,stderr
	ssh.close()
        return data
def delgtp(pro,group):
	hostname='192.168.0.36'
	port=22
	username='root'
	password='huanshuo#888'
        para=pro+' '+group
        cmd = '/usr/bin/python /root/delgroup.py '+' '+para
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname,username=username,password=password,allow_agent=False,look_for_keys=False)
	stdin, stdout, stderr = ssh.exec_command(cmd)
        channel = stdout.channel
	data = stdout.readlines()     
        #print stdin,stdout,stderr
	ssh.close()
        return data
def sync_svn():
	hostname='192.168.0.36'
	port=22
	username='root'
	password='huanshuo#888'
        cmd = '/usr/bin/python /root/syncsvn.py '
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname,username=username,password=password,allow_agent=False,look_for_keys=False)
	stdin, stdout, stderr = ssh.exec_command(cmd)
        channel = stdout.channel
	data = stdout.readlines()[0]     
	ssh.close()
        return data
def sync_user():
	hostname='192.168.0.36'
	port=22
	username='root'
	password='huanshuo#888'
        cmd = '/usr/bin/python /root/syncuser.py '
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname,username=username,password=password,allow_agent=False,look_for_keys=False)
	stdin, stdout, stderr = ssh.exec_command(cmd)
        channel = stdout.channel
	data = stdout.readlines()[0]     
	ssh.close()
        return data
def sync_group():
	hostname='192.168.0.36'
	port=22
	username='root'
	password='huanshuo#888'
        cmd = '/usr/bin/python /root/syncgroup.py '
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname,username=username,password=password,allow_agent=False,look_for_keys=False)
	stdin, stdout, stderr = ssh.exec_command(cmd)
        channel = stdout.channel
	data = stdout.readlines()[0]     
	ssh.close()
        return data
def sync_pro():
	hostname='192.168.0.36'
	port=22
	username='root'
	password='huanshuo#888'
        cmd = '/usr/bin/python /root/syncpro.py '
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname,username=username,password=password,allow_agent=False,look_for_keys=False)
	stdin, stdout, stderr = ssh.exec_command(cmd)
        channel = stdout.channel
	data = stdout.readlines()[0]     
	ssh.close()
        return data
