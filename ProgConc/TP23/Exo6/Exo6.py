#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 11:30:17 2022

@author: alexandre.jolin
"""

import os, time, random, sys
for i in range(4) :
    if os.fork() != 0 :
        break
random.seed()
delai = random.randint(0,4)
time.sleep(delai)
os.wait()
print("Mon nom est " + chr(ord('A')+i) + " j ai dormi " + str(delai) + " secondes")

sys.exit(0)