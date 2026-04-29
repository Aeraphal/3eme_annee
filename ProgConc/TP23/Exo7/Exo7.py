#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 11:38:27 2022

@author: alexandre.jolin
"""

import os, sys
N = 3
for i in range(N) :
    #__________début des ajouts_________
    os.fork()
    os.fork()
    # __________fin des ajouts__________
print("Bonjour")
sys.exit(0)