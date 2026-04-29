#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 08:23:50 2022

@author: alexandre.jolin
"""
import sys
mot = sys.argv[1]
k = ''
n = len(mot)
print(mot)
for m in range(1, n+1):
    k+=mot[-m]
print(k)