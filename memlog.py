#!/usr/bin/python3
import sys, os, psutil, time

"""
example crontab:
*/5 * * * * /home/dbm/memlog/memlog.py >> /home/dbm/memlog/memlog.log
"""

#os.system("whoami")
#rint(os.path.abspath('.'))

m=psutil.virtual_memory()
#print (m)
tot=m[0]
avail=m[1]
use=(tot-avail)/tot

print ("%s,total,%4.3f,use,%4.5f" % (time.ctime(), tot/1000000000, use))
sys.stdout.flush()
