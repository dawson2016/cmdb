#!/usr/bin/env python

import sys
import os
import ConfigParser
import time

cf = ConfigParser.ConfigParser()
cf.read("/etc/svn/accesspolicy.conf")

secs = cf.sections()
opts = cf.options("groups")
today=time.strftime('%m%d', time.localtime(time.time()))
if sys.argv[1] == "nogroup":
    os.system('htpasswd -b /etc/svn/svnusers.conf' + " " + sys.argv[2] + " " + str(sys.argv[2])+today )
elif sys.argv[2] == "nouser":
    cf.set("groups",sys.argv[1], "admin")
else:
     if sys.argv[1] in opts:
        a = cf.get("groups", sys.argv[1])
        cf.set("groups",sys.argv[1],a + "," + sys.argv[2])
     else:
        cf.set("groups",sys.argv[1], sys.argv[2])
cf.write(open("/etc/svn/accesspolicy.conf","w"))
