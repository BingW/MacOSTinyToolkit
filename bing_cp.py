#! /usr/bin/python
#version 0.02
#

import sys
import os
file_name = sys.argv[1]
mv_cmd = "mv %s %s"%(file_name,file_name+"_original")
os.system(mv_cmd)
open(file_name,"wb").write(open(file_name+"_original","rb").read())
chmod_cmd = "chmod 777 %s"%(file_name)
os.system(chmod_cmd)
