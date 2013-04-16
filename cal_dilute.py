#! /usr/bin/env python
# coding: utf-8

import sys
try:
    assert len(sys.argv) == 3
except:
    print "Useage\n"
    print "Bing_dilute.py original target"

original = float(sys.argv[1])
target = float(sys.argv[2])
print "dilute from %.2f x -> %.2f x"%(original,target)

water = original/target-1
print "you need add %.5f water for every 1 original solution"%(water)
