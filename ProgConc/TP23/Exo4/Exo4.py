#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 11:04:33 2022

@author: alexandre.jolin
"""

import os, sys

n=0
for i in range(1,5):
    fils_pid = os.fork() #1
    if (fils_pid > 0): #2
        os.wait() #3
        n = i*2
        break;
print("n = ", n) #4
sys.exit(0)



#Après la ligne étiquetée #2, dans le bloc d’exécution
#du if, on se retrouve dans quel processus, le père ou le
#fils ? Pour qui la valeur de fils_pid est-elle nulle ?

#On se retrouve dans le processus du père car le PID du fils est égal à 0


#Ce programme est-il déterministe? (Justifiez)

#Oui


#Même question si l’on supprime la ligne étiquetée #3,

#On se retrouve dans les deux processus en même temps qui s'effectuent
#alors en parallèle.


#Si le programme est déterministe tel quel, indiquez
#exactement ce qui sera affiché à l’écran lors de son
#exécution. S’il n’est pas déterministe, donnez un des
#affichages possibles.

#0, 8, 6, 4, 2


#L’appel à os.fork(), ligne étiquetée /*1*/, peut-il échouer? Pourquoi?

#Non