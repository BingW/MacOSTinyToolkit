#! /usr/bin/python
#version 0.03
#
'''
version 0.03
won't rename original file, just create a totally "local copy" 
of original file end with "_cp"
'''

import sys
import os
file_name = sys.argv[1]
os.system(mv_cmd)
open(file_name+"_cp","wb").write(open(file_name,"rb").read())
chmod_cmd = "chmod 777 %s"%(file_name+"_cp")
os.system(chmod_cmd)
