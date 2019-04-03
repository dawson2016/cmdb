#!/usr/bin/env python
import os
import sys
import ConfigParser


cf = ConfigParser.ConfigParser()
cf.read("/etc/svn/accesspolicy.conf")

secs = cf.sections()

if sys.argv[2] == "@nogroup":
    cf.add_section(sys.argv[1]+":/")
    os.system('svnadmin create /data/svn/'+sys.argv[1])
    os.system('chown -R apache.apache /data/svn/'+sys.argv[1])
elif sys.argv[1] in secs:
    cf.set(sys.argv[1]+":/", sys.argv[2], "rw")
    #print "[" + sys.argv[1] + "]"  + " already exist!"
else:
        #os.system('svnadmin create /data/svn/'+sys.argv[1])
    #cf.add_section(sys.argv[1]+":/")
    cf.set(sys.argv[1]+":/", sys.argv[2], "rw")
#else:
#    cf.add_section(sys.argv[1])
#    cf.set(sys.argv[1], sys.argv[2], "rw")


cf.write(open("/etc/svn/accesspolicy.conf","w"))
