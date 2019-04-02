#!/usr/bin/env python
import os
import sys
import ConfigParser
import json
para1=sys.argv[1]
para2=sys.argv[2]
def main():
    a=[]
    cf = ConfigParser.ConfigParser()
    cf.read("/etc/svn/accesspolicy.conf")
    cf.remove_option(para1+':/','@'+para2) 
    cf.write(open("/etc/svn/accesspolicy.conf","w"))
main()
