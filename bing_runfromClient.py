#! /usr/bin/env python
#coding: utf-8

#this program helps run command on LabServer through your macprobook Client

#IMPORTANT: Acturally it just replace "/Volumes/hittingerlab/" to "~/" and run the command

import os,sys

def print_usage():
    print "\nUsage:\n"
    print "./bing_runfromClient.py command\n"
    print "This program will print a command which can run from your ssh client."
    print "Acturally what this program do it just replace \"/Volumes/hittingerlab/\" to \"~/\"\n"

if len(sys.argv) == 1:
    print_usage()
    sys.exit()

cmd = " ".join(sys.argv[1:]).replace("/Volumes/hittingerlab/","~/")
print cmd

'''
if raw_input("\nAre you sure to run this cmd? (y/n)\n") == "y":
    os.system(cmd)
else:
    print "exit"
    sys.exit()
'''
