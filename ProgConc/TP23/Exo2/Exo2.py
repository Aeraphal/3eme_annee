#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 10:47:14 2022

@author: alexandre.jolin
"""

import os, sys


for i in range(3):
    print(i, "je suis le processus : ", os.getpid(), ", mon pere est : ", os.getppid(),", retour : ", os.fork())
sys.exit()