#! /usr/bin/python
#version 0.02
#
'''
This program is not mature, do not use!
'''
import sys
import os
file_name = sys.argv[1]
os.system(mv_cmd)
open(file_name+"_cp","wb").write(open(file_name,"rb").read())
chmod_cmd = "chmod 777 %s"%(file_name+"_cp")
os.system(chmod_cmd)
