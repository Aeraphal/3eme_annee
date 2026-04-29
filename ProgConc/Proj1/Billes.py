#Gestionnaire de Billes

#----------------------Main-------------------------

# $ python3 Billes.py

#---------------------------------------------------

import multiprocessing as mp
 
import os, time,math, random, sys, ctypes, signal, threading

#-----------------------------------------------------------

Verif = mp.Lock()

cond = mp.Lock()

payement = mp.Lock()

#-----------------------------------------------------------
def travail(nb_billes):
    k = random.randint(1,5)
    for i in range(k):
        presentation(i,k,nb_billes)
        demander(nb_billes)
        print("Encore du travail?")
        time.sleep(2 * nb_billes)
        print("Travail terminé!")
        rendre(nb_billes)

def demander(nb_billes):
    cond.acquire()
    assez=billes_dispo.value
    while assez < nb_billes:
        cond.release()
        print("Je dois attendre...")
        time.sleep(2)
        assez=billes_dispo.value
        cond.acquire()
    with Verif:
        print("Il reste ", billes_dispo.value, "billes dans le tas. Et j'en prend ",nb_billes)
        billes_dispo.value -= nb_billes 
        assez = billes_dispo.value
        print("Il y en a donc ", billes_dispo.value)
        cond.release()

def presentation(i, k , nb_billes):
    if i == 0:
        print("-----------")
        print("Bonjour, j'ai ",k, " travaux à faire aujourd'hui.")
        print("Il me faut ",nb_billes, " billes pour le réaliser.")
        print("-----------")

def rendre(nb_billes):
    payement.acquire()
    with Verif:
        print("Voici la moula!")
        print("Il reste ", billes_dispo.value, "billes dans le tas. Et j'en rajoute ",nb_billes)
        billes_dispo.value += nb_billes 
        print("Il y en a donc ", billes_dispo.value)
        payement.release()

def Controle(max_bille):
    t = True
    while t == True:
        with Verif:
            assez = billes_dispo.value
            if assez < 0 or assez > max_bille:
                t == False
                print("création de billes non autorisé !")
        time.sleep(1)
    for i in range(Nb_process): 
        salarie[i].terminate() 
    sys.exit()

#-----------------------------------------------------
#Lancement du main

Nb_process = int(input("Donnez le nombre de salarié voulu : "))
Max_bille = int(input("Combien de billes avez vous pour les payer? : "))
salarie = [0 for i in range(Nb_process)]
billes_dispo = mp.Value('i',Max_bille)
#signal.signal(signal.SIGINT , prise_en_compte_signaux)
#signal.signal(signal.SIGQUIT , prise_en_compte_signaux)

for i in range(Nb_process):  # Lancer     Nb_process  processus
    nb_billes = random.randint(2,5)
    salarie[i] = mp.Process(target=travail, args= (nb_billes,))
    salarie[i].start()

controleur = mp.Process(target=Controle, args=(int(Max_bille),))
controleur.start()







controleur.terminate()