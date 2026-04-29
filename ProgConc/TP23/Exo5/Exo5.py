#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 11:24:28 2022

@author: alexandre.jolin
"""

import sys, os, time

N = int(sys.argv[1])
i = 0
while i!=N:
    pid = os.fork()
    ppid = os.getppid()
    print("processus fils %d" %(pid))
    print("processus père %d" %(ppid))
    time.sleep(2*i)
    i = i+1
sys.exit()