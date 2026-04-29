#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 09:56:54 2022

@author: alexandre.jolin
"""

import os,sys
N = 10
i=1
while os.fork()==0 and i<=N :
    i += 1
print("Je suis le processus FILS : ", os.getpid(), "du processus PERE : ", os.getppid())
sys.exit(0)