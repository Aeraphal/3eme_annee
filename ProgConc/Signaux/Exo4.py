import sys, os, signal, time

pid = os.fork()

compteur = 1
if pid == 0:
    while True :
        if compteur == 1:
            print("Je suis un fils turbulent!")
        elif compteur == 2:
            print("J'aime le faire savoir!")
        elif compteur == 3:
            print("Vous êtes nuls!")
        else :
            print("Pourquoi je suis encore en vie?")
        compteur = compteur+1
        time.sleep(1)
else :
    for i in range(6):
        if i == 3:
            print("MEURT FILS INDIGNE SI C'EST CE QUE TU SOUHAITES TANT!")
            time.sleep(0.1)
            print("N-... *Pan* ARGHHHH!!!")
            os.kill(pid, signal.SIGKILL)
            time.sleep(1.9)
        elif i > 3:
            print("Enfin un peu de calme... ;)")
            time.sleep(2)
        else :
            time.sleep(2)
            print("Tais-toi...")







