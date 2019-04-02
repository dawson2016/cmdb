#!/usr/bin/env python
import json
def main():
    userlist=[]
    f = open("/etc/svn/svnusers.conf", "r")
    for i in f.readlines():
        userlist.append({'name':i.split(':')[0],'password':i.split(':')[1].strip('\n')}) 
    return json.dumps(userlist)
    f.close()
print main()
