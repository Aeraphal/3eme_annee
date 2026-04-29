#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 08:10:28 2022

@author: alexandre.jolin
"""

#Partie 1

""""$ python exercice1.py python un deux 3"""
import sys
print("Nom du programme : ", sys.argv[0])
print("Nombre d’arguments : ", len(sys.argv)-1)
print("Les arguments sont : ")
for arg in sys.argv[1:] :
    print(arg)