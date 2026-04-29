import sys, os, signal, time
import multiprocessing as mp

N = [1,2,3,4,5,6,7,8,9,10]
somme = mp.Value('i',0)
l = len(N)-1
if os.fork() == 0: #Pair
    sommePair = 0
    i = 0
    while i <= l:
        sommePair += N[i]
        i = i+2
    somme.value += sommePair

elif os.fork() == 0: #Impair
    sommeImpair = 0
    i = 1
    while i <= l:
        sommeImpair += N[i]
        i = i+2
    somme.value += sommeImpair

else :
    os.wait()
    os.wait()
    print(somme.value)







