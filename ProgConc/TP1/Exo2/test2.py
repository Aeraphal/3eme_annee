#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 09:19:00 2022

@author: alexandre.jolin
"""
import os,sys
for i in range(4) :
    pid = os.fork()
    if pid != 0 :
        print("Ok !")
    print("Bonjour !")
sys.exit(0)