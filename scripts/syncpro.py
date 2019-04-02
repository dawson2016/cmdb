#!/usr/bin/env python
import os
import sys
import ConfigParser
import json
def main():
    a=[]
    b=[]
    cf = ConfigParser.ConfigParser()
    cf.read("/etc/svn/accesspolicy.conf")
    proname = cf.sections()
    for i in proname:
        if i != 'groups':
            keys = cf.options(i)
            for j in cf.items(i):
                b.append(j[0].strip('@'))
            a.append({'pname':i.split(':')[0],'gmem':b})
            b=[]
    data=json.dumps(a)
    return data
print main()
