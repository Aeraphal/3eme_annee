#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 10:15:58 2022

@author: alexandre.jolin
"""

import os
N = 5
for process in range(1,N+1) :
    pid = os.fork()
    if pid == 0:
        print("Je suis le processus FILS : ", os.getpid(), "du processus PERE : ", os.getppid())
        os._exit(0)
os._exit(0)