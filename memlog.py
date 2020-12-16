import sys, psutil, time

m=psutil.virtual_memory()
#print (m)
tot=m[0]
avail=m[1]
use=(tot-avail)/tot

print ("time,%s,total,%4.3f,use,%4.2f" % (time.ctime(), tot/1000000000, use))
sys.stdout.flush()
