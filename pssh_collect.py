#!/usr/bin/python
import os
import sys

try:
   sys.argv[1]
except IndexError:
   print "Please give the command as argument in \" \" quotes"
   sys.exit()
   
if os.popen("id -u").read().rstrip("\n")!=0:
   os.system("rm -fr ./test")
else:
   print "Danger you are root !!"

CSI="\x1B["   # for coloring  
command = "pssh -O StrictHostKeyChecking=no -o test -h '%s'  -l girishb '%s'"  %(sys.argv[2],sys.argv[1])
state = os.system(command)

if state!=0:
   print "ERROR running command\n"
   sys.exit()

dirlist = os.listdir("./test")

for files in dirlist:
   filepath ="./test/%s" %(files)
   fh = open(filepath)
   #CSI="\x1B["
   print CSI+"31;40m" + "%s" %(files) + CSI + "0m" 
   lines = fh.read()
   print lines,
   print "\n"
