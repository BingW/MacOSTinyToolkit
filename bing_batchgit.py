#! /usr/bin/env python 
# coding:utf-8
# Author: bingwang
# Email: toaya.kase@gmail.com
# Copyleft Bing Wang
# LICENCES: GPL v3.0
# version: 0.11


__docformat__ = "epytext en"
'''
This program do git for all git repository under current path.
In version 0.1 it has:

# for pull request
bing_batchgit.py pull
# for push request
bing_batchgit.py push

new in version 0.11

#same as pull/push
bing_batchgit.py start/end
'''

import os,sys

def print_help():
    print "batch git for all git repository under current path"
    print "USAGE\n"
    print "To push all repository under current path"
    print "./bing_batchgit.py push/end\n"
    print "To pull all repository under current path"
    print "./bing_batchgit.py pull/start\n"

if len(sys.argv) != 2:
    print_help()

elif sys.argv[1] in ["pull","start"]:
    current_dir = os.getcwd() + "/"
    for item in os.listdir(current_dir):
        if os.path.isdir(current_dir+item):
            if ".git" in os.listdir(current_dir+item):
                cmd = "cd %s && git pull"%(current_dir+item)
                print "git pull %s"%(item)
                os.system(cmd)

elif sys.argv[1] == ["push","end"]:
    current_dir = os.getcwd() + "/"
    for item in os.listdir(current_dir):
        if os.path.isdir(current_dir+item):
            if ".git" in os.listdir(current_dir+item):
                cmd = "cd %s && git push"%(current_dir+item)
                print "git push %s"%(item)
                os.system(cmd)

else:
    print_help()
