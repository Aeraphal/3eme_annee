import sys, os, signal, time

global fin
fin =  False

def arret(signal, frame = None):
    global fin
    fin = True
    print("On arrête tout!")


signal.signal(signal.SIGINT , arret)
while fin == False :
    time.sleep(1)
    print ("Je boucle")