import sys, os, signal, time
import multiprocessing as mp

S = mp.Semaphore(0)

if os.fork() == 0:
    print("Je suis T1 et je retarde la tâche de T2")
    time.sleep(3)
    print("J'aime le faire attendre longtemps...")
    time.sleep(3)
    print("Très... Très... Très... Très... Très... Très... Très...")
    time.sleep(3)
    print("Longtemps...")
    time.sleep(1)
    S.release()

else:
    S.acquire()
    print("Je suis T2 et j'ai été retardé par T1")
    print("Désolé pour le retard...")
