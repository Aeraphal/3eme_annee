import os, sys

import random as rd

(Lecture , Ecriture) = os.pipe()

N = 320
liste = []
for i in N:
    nombre = rd.randint(0,10)
    liste.append(nombre)

for k in liste:
    if liste[k]%0 == 0:
        i = 1
    else :
        i = 2



