#! /usr/bin/env python 
# coding:utf-8
# Author: bingwang
# Email: toaya.kase@gmail.com
# Copyleft Bing Wang
# LICENCES: GPL v3.0
# version: 0.1


__docformat__ = "epytext en"
'''
This program do git for all git repository under current path.
In this version it has:

# for pull request
bing_batchgit.py pull
# for push request
bing_batchgit.py push
'''

import os,sys

def print_help():
    print "batch git for all git repository under current path"
    print "USAGE\n"
    print "To push all repository under current path"
    print "./bing_batchgit.py push\n"
    print "To pull all repository under current path"
    print "./bing_batchgit.py pull\n"

if len(sys.argv) != 2:
    print_help()

elif sys.argv[1] == "pull":
    current_dir = os.getcwd() + "/"
    for item in os.listdir(current_dir):
        if os.path.isdir(current_dir+item):
            if ".git" in os.listdir(current_dir+item):
                cmd = "cd %s && git pull"%(current_dir+item)
                print cmd

elif sys.argv[1] == "push":
    current_dir = os.getcwd() + "/"
    for item in os.listdir(current_dir):
        if os.path.isdir(current_dir+item):
            if ".git" in os.listdir(current_dir+item):
                cmd = "cd %s && git push"%(current_dir+item)
                print cmd

else:
    print_help()
