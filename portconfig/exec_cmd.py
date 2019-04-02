#!/usr/bin/env python
#coding:utf-8
import paramiko
def remotecmd(ip,wanport,lanport):
	hostname='192.168.0.13'
	port=22
	username='root'
	password='huanshuo#888'
	save_cmd = 'service iptables save'
        prerouting_cmd = 'iptables -t nat -A PREROUTING -i eth0 -p tcp -m tcp --dport '+ wanport+' -j DNAT --to-destination '+ip+':'+lanport
	postrouting_cmd = 'iptables -t nat -A POSTROUTING -d '+ip+'/32'+' -p tcp -m tcp --dport '+lanport+' -j SNAT --to-source '+hostname
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname,username=username,password=password,allow_agent=False,look_for_keys=False)
	stdin, stdout, stderr = ssh.exec_command(prerouting_cmd)
	stdin0, stdout0, stderr0 = ssh.exec_command(postrouting_cmd)
	stdin1, stdout1, stderr1 = ssh.exec_command(save_cmd)
	#data = stdout.readlines()     
        channel = stdout.channel
        channel0 = stdout0.channel
        channel1 = stdout1.channel
	status = channel.recv_exit_status()
	status0 = channel0.recv_exit_status()
	status1 = channel1.recv_exit_status()
	#print prerouting_cmd,postrouting_cmd 
	ssh.close()
        return status,status0,status1
def iptables_cmd(ip,wanport,action):
	hostname='192.168.0.13'
	port=22
	username='root'
	password='huanshuo#888'
        para=ip+' '+wanport+' '+action
        cmd = '/bin/bash /root/test2.sh '+' '+para
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname,username=username,password=password,allow_agent=False,look_for_keys=False)
	stdin, stdout, stderr = ssh.exec_command(cmd)
        channel = stdout.channel
	data = stdout.readlines()[0]     
	#status = channel.recv_exit_status()
	ssh.close()
        return data
def sync_iptables():
	hostname='192.168.0.13'
	port=22
	username='root'
	password='huanshuo#888'
        cmd = '/usr/bin/python /root/sync_iptables.py'
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname,username=username,password=password,allow_agent=False,look_for_keys=False)
	stdin, stdout, stderr = ssh.exec_command(cmd)
        channel = stdout.channel
	data = stdout.readlines()[0]     
	#status = channel.recv_exit_status()
	ssh.close()
        return data
