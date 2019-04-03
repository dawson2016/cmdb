#!/usr/bin/env python
import os
import sys
import ConfigParser
import json
def main():
    a=[]
    cf = ConfigParser.ConfigParser()
    cf.read("/etc/svn/accesspolicy.conf")
    secs = cf.sections()
    for i in secs:
        a.append({'name':i})
    data=json.dumps(a)
    return data
print main()
