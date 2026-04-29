import sys, os, signal, time
import multiprocessing as mp
import random as rd

C1 = mp.Queue()
C2 = mp.Queue()
S1 = mp.Semaphore(1)
S2 = mp.Semaphore(0)
k = 5

if os.fork() == 0:
    rd.seed(os.getpid())
    for i in range(k):
        alea1 = rd.randint(1,100)
        C1.put(alea1)
elif os.fork() == 0:
    for i in range(k):
        alea2 = rd.randint(1, 100)
        C2.put(alea2)
elif os.fork() == 0:
    for i in range(k):
        S1.acquire()
        print("Je suis C1 et je lis la valeur")
        valeur1 = C1.get()
        print(valeur1)
        S2.release()
else:
    for i in range(k):
        S2.acquire()
        print("Je suis C2 et je lis la valeur")
        valeur2 = C2.get()
        print(valeur2)
        S1.release()
