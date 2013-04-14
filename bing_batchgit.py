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

version 0.1:
-------------------
# for pull request
bing_batchgit.py pull
# for push request
bing_batchgit.py push

new in version 0.11
-------------------
#same as pull/push
bing_batchgit.py start/end

new in version 0.12
-------------------
1. push/end bug fix
2. functionlize
3. add batchgit status
'''

import os,sys

def print_help():
    print "batch git for all git repository under current path"
    print "USAGE\n"
    print "To push all repository under current path"
    print "./bing_batchgit.py push/end\n"
    print "To pull all repository under current path"
    print "./bing_batchgit.py pull/start\n"

def batchrun_git_cmd(gitcmd):
    current_dir = os.getcwd() + "/"
    for item in os.listdir(current_dir):
        if os.path.isdir(current_dir+item):
            if ".git" in os.listdir(current_dir+item):
                cmd = "cd %s && git %s"%(current_dir+item,gitcmd)
                print "\ngit %s %s"%(gitcmd,item)
                os.system(cmd)

if len(sys.argv) != 2:
    print_help()

elif sys.argv[1] in ["pull","start"]:
    batchrun_git_cmd("pull")
    
elif sys.argv[1] in ["push","end"]:
    batchrun_git_cmd("push")

elif sys.argv[1] in ["status"]:
    batchrun_git_cmd("status")

else:
    print_help()
