#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 09:18:52 2022

@author: alexandre.jolin
"""

import os,sys
N = 10
i=1
while os.fork()==0 and i<=N :
    i += 1
print(i)
sys.exit(0)