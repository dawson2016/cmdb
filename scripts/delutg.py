#!/usr/bin/env python
import os
import sys
import ConfigParser
import json
def main():
    a=[]
    cf = ConfigParser.ConfigParser()
    cf.read("/etc/svn/accesspolicy.conf")
    keys = cf.items('groups')
    print keys
    for i in keys:
        if i[0]==sys.argv[1]:
            userlist=i[1].split(',')
            userlist.remove(sys.argv[2])
            pre=','
            for j in userlist:
                pre=pre+','+j
            cf.set("groups",sys.argv[1],str(pre[2:]))
    cf.write(open("/etc/svn/accesspolicy.conf","w"))
main()
