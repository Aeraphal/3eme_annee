#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 08:45:39 2022

@author: alexandre.jolin
"""

import sys
notes = sys.argv[1:]
tot = 0
if len(notes)<1:
    print('Aucune moyenne à calculer')
else:
    for k in range(1, len(notes)+1):
        try:
            note = float(notes[k-1])
            if note<=20 and note>=0:
                tot = tot + note
            else:
                print("Note(s) non valide(s)")
                tot = 0
                break
        except ValueError:
            print('Note(s) non valide(s)')
            t = 0
            tot = 0
            break
if tot > 0: 
    moyenne = tot/k
    print('Moyenne est : ' "%.2f" %moyenne)