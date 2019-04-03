#!/usr/bin/env python
import os
import sys
import ConfigParser
import json
def main():
    os.system('htpasswd -D /etc/svn/svnusers.conf' + " " + sys.argv[1])
main()
