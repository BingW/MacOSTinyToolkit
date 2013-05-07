#! /usr/bin/env python
#coding: utf-8

#this program helps run command on LabServer through your macprobook Client

#IMPORT: Acturally it just replace "/Volumes/hittingerlab/" to "~" and run the command

import os,sys
cmd = " ".join(sys.argv[1:]).replace("/Volumes/hittingerlab/","~/")
print cmd
if raw_input("\nAre you sure to run this cmd? (y/n)\n") == "y":
    os.system(cmd)
else:
    print "exit"
    sys.exit()
