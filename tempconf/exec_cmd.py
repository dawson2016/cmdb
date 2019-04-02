#!/usr/bin/env python
#coding:utf-8
import paramiko
import subprocess
def push_nginx(ip,filename):
    password='xxx'
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, 22, 'root', password)
    local_file="/tmp/"+filename
    remote_file='/www/nginx/etc/vhost/devops/'+filename
    reloadcmd='nginx -s reload'
    checkcmd='nginx -t'
    if ip=='192.168.0.43':
        remote_file='/data/nginx/vhost/wbl/'+filename
        reloadcmd='docker exec nginx nginx -s reload'
        checkcmd='docker exec nginx nginx -t'
    sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
    sftp = ssh.open_sftp()
    sftp.put(local_file, remote_file)
    stdin, stdout, stderr = ssh.exec_command(checkcmd)
    data = stderr.readlines()
    output = data[0].strip().find('successful')
    if output!=-1:
        ssh.exec_command(reloadcmd)
    return data 
