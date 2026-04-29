import sys, os, signal, time

def arret(signal, frame = None):
    print("On arrête tout!")
    sys.exit()


signal.signal(signal.SIGINT , arret)
while True :
    time.sleep(1)
    print ("Je boucle")


