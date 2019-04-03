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
    for i in keys:
        a.append({'gname':i[0],'member':i[1:]})
    data=json.dumps(a)
    return data
print main()
