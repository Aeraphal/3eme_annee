#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 10:55:50 2022

@author: alexandre.jolin
"""

import os, sys
for i in range(3):
    pid = os.fork()
    if pid == 0:
        if i==0:
            os.execlp("who", "who")
        elif i==1:
            os.execlp("ps", "ps")
        else:
            os.execlp("ls", "ls", "-l")
sys.exit()









