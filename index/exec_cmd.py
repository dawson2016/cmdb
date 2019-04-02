#!/usr/bin/env python
#coding:utf-8
import paramiko
import subprocess
import redis
import time
def scp_put(filename):
    ip='192.168.0.46'
    password='huanshuo#888'
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, 22, 'root', password)
    local_file="/tmp/"+filename
    remote_file='/data/upload/appstore/'+filename
    check = subprocess.Popen(["file","/tmp/"+filename],stdout=subprocess.PIPE)
    output = check.communicate()[0].strip().find('Zip')
    if int(output)!=-1:
        sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
        sftp = ssh.open_sftp()
        sftp.put(local_file, remote_file)
def log_out(lanip,dockername):
    ip=str(lanip)
    password='huanshuo#888'
    line_num=0
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, 22, 'root', password)
    r=redis.StrictRedis(host='192.168.0.27', port=6379,password='Hs123#')
    #cmd='journalctl -u docker -f --no-pager'
    cmd='docker logs -f  --tail 100 '+str(dockername)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    while True:
        line=stdout.readline()
        line_num+=1
        r.publish(dockername,line)
        if line_num==5000: 
            ssh.close()
            r.publish(dockername,'###############1000 lines log has displayed over or No logs are produced !!!#######################')
            break
    print 'ssh over'

