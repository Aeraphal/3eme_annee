import sys, os, signal, time

pid = os.fork()

def message(signal, frame = None):
    print("Toujours!")

def arret(signal, frame=None):
    print("Bien")

k = 10000

compteur = 1
if pid == 0:
    while True:
        signal.signal(signal.SIGUSR1,message)
        signal.signal(signal.SIGUSR2, arret)
else :
    for i in range(8):
        if i == 3 or i == 5:
            os.kill(pid,signal.SIGUSR1)
            time.sleep(1)
        elif i ==7:
            print("On y va!")
            os.kill(pid,signal.SIGUSR2)
            time.sleep(1)
        else :
            time.sleep(1)
            print("Tu es prêt!?")
