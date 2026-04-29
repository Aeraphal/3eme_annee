#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 10:27:17 2022

@author: alexandre.jolin
"""

import os, sys
pid = os.fork()
if pid==0:
    print('Traitement 1')
else:
    os.wait()
    print('Traitement 2')
    os.execlp("python", "python", "test.py")
sys.exit()