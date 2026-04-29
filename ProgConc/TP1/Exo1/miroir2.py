#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 08:41:37 2022

@author: alexandre.jolin
"""

import sys
mots = sys.argv[1:]
for nombre in range(1,len(mots)+1):
    mot = mots[nombre-1]
    k = ''
    n = len(mot)
    for m in range(1, n+1):
        k+=mot[-m]
    print(k)