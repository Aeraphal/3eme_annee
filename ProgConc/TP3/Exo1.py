#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 08:15:40 2022

@author: alexandre.jolin
"""

import os , sys
msg = 8.0
print ("Création d’un pipe anonyme")
(dfr , dfw) = os.pipe()
var_b = msg.hex().encode()
length = len(var_b)

lb = length.to_bytes(4,byteorder="little",signed = True)
msgReception = os.write(dfw,lb)
os.write(dfw,var_b)
print ("Le processus %d a transmis le message %s\n" %(os.getpid() , msg ) )
lb = os.read(dfr,4)
length = int.from_bytes(lb,byteorder="little",signed=True)
var_b = os.read(dfr,length)
var = float.fromhex(var_b.decode())
print ("Le processus %d a reçu le message %s\n" %(os.getpid() , msgReception))
dfr.close()
dfw.close()
sys.exit(0) 