import sys, os, signal, time

def arret(signal, frame = None):
    print("On arrête tout!")
    sys.exit()

signal.signal(signal.SIGINT , signal.SIG_IGN)
while True :
    time.sleep(10)
    print ("Je boucle")

