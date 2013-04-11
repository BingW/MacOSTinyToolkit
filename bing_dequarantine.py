#! /usr/bin/python 
# coding:utf-8
# Author: bingwang
# Email: toaya.kase@gmail.com
# Copyleft Bing Wang
# LICENCES: GPL v3.0
# version: 0.1

__docformat__ = "epytext en"

import os,sys

def print_help():
    print "dequarantine file or folder"
    print "USAGE\n"
    print "./bing_dequarantine [-h/-help] file_name/folder_name\n"
    print "OPTIONAL ARGUMENTS\n"
    print "-h/help"
    print "\t print help info"

if "-h" in sys.argv or "-help" in sys.argv:
    print_help()
    sys.exit()

try:
    file_name = sys.argv[1]
    assert os.path.exists(file_name)
except:
    print_help()
    sys.exit()
if os.path.isfile(file_name):
    cmd = "xattr -d com.apple.quarantine %s"%(file_name)
    os.system(cmd)
    print "%s dequarantined"%file_name
else:
    lines = os.popen("ls -l@ %s"%file_name).read().split("\n")
    for i,line in enumerate(lines):
        if "@" in line.split(" ")[0] and "com.apple.quarantine" in lines[i+1]:
            f = line.split(" ")[-1]
            cmd = "xattr -d com.apple.quarantine %s"%(file_name+"/"+f)
            os.system(cmd)
            print "%s dequarantined"%(file_name+"/"+f)



