#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 08:16:56 2022

@author: alexandre.jolin
"""

import os, sys



dicoNotes = { "E1" : [10, 15, 20], "E2" : [12, 16, 15], "E3" : [11, 13, 20]}

l = len(dicoNotes)


MoyTot = 0
Max = 0
indicemax = 0
Min = 20
indicemin = 0
listemoyenne = []
listeEleve = []

for elevei, notei in dicoNotes.items():
    (dfr , dfw) = os.pipe()
    pid = os.fork()
    if pid == 0:
        os.close(dfr)
        moyenne = 0.0
        for k in range(0, len(notei)):
            moyenne = moyenne + notei[k]
        moyenne = moyenne/len(notei)
        var = moyenne.hex().encode()
        length = len(var)
        lb = length.to_bytes(4,byteorder="little",signed = True)
        os.write(dfw, lb)
        os.write(dfw, var)
        sys.exit(0)
    else:
        os.close(dfw)
        lb = os.read(dfr, 4)
        length = int.from_bytes(lb,byteorder="little",signed=True)
        var = os.read(dfr,length)
        var = float.fromhex(var.decode())
        listemoyenne.append(var)
        listeEleve.append(elevei)
        

Max = max(listemoyenne)
imax = listemoyenne.index(Max)
Min = min(listemoyenne)
imin = listemoyenne.index(Min)
indicemax = listeEleve[imax]
indicemin = listeEleve[imin]

print("Le processus a compilé les moyenne de la classe qui sont ",listemoyenne)
print("La meilleur moyenne est celle de l'élève", indicemax, Max)
print("La plus basse moyenne est celle de l'élève", indicemin, Min)

dfr.close() ; dfw.close()
sys.exit(0)