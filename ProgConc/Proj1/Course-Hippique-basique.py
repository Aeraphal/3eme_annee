# Cours hippique

#----------------------- Main ---------------------------------

# $ python3 Course-Hippique-basique.py

#--------------------------------------------------------------


# Version très basique, sans mutex sur l'écran, sans arbitre, sans annoncer le gagnant, ... ...

# Quelques codes d'échappement (tous ne sont pas utilisés)
CLEARSCR="\x1B[2J\x1B[;H"          #  Clear SCreen
CLEAREOS = "\x1B[J"                #  Clear End Of Screen
CLEARELN = "\x1B[2K"               #  Clear Entire LiNe
CLEARCUP = "\x1B[1J"               #  Clear Curseur UP
GOTOYX   = "\x1B[%.2d;%.2dH"       #  ('H' ou 'f') : Goto at (y,x), voir le code

DELAFCURSOR = "\x1B[K"             #  effacer après la position du curseur
CRLF  = "\r\n"                     #  Retour à la ligne

# VT100 : Actions sur le curseur
CURSON   = "\x1B[?25h"             #  Curseur visible
CURSOFF  = "\x1B[?25l"             #  Curseur invisible

# Actions sur les caractères affichables
NORMAL = "\x1B[0m"                  #  Normal
BOLD = "\x1B[1m"                    #  Gras
UNDERLINE = "\x1B[4m"               #  Souligné


# VT100 : Couleurs : "22" pour normal intensity
CL_BLACK="\033[22;30m"                  #  Noir. NE PAS UTILISER. On verra rien !!
CL_RED="\033[22;31m"                    #  Rouge
CL_GREEN="\033[22;32m"                  #  Vert
CL_BROWN = "\033[22;33m"                #  Brun
CL_BLUE="\033[22;34m"                   #  Bleu
CL_MAGENTA="\033[22;35m"                #  Magenta
CL_CYAN="\033[22;36m"                   #  Cyan
CL_GRAY="\033[22;37m"                   #  Gris

# "01" pour quoi ? (bold ?)
CL_DARKGRAY="\033[01;30m"               #  Gris foncé
CL_LIGHTRED="\033[01;31m"               #  Rouge clair
CL_LIGHTGREEN="\033[01;32m"             #  Vert clair
CL_YELLOW="\033[01;33m"                 #  Jaune
CL_LIGHTBLU= "\033[01;34m"              #  Bleu clair
CL_LIGHTMAGENTA="\033[01;35m"           #  Magenta clair
CL_LIGHTCYAN="\033[01;36m"              #  Cyan clair
CL_WHITE="\033[01;37m"                  #  Blanc
#-------------------------------------------------------
import multiprocessing as mp
 
import os, time,math, random, sys, ctypes, signal, threading
from shutil import move
from turtle import pos

from httplib2 import MalformedHeader


#Initialisation de fonction/Variables/Mutex

mutex = mp.Lock()

# Définition de qq fonctions de gestion de l'écran
def effacer_ecran() : 
    
    print(CLEARSCR,end='')
    

def erase_line_from_beg_to_curs() : 
    print("\033[1K",end='')
    

def curseur_invisible() : 
    print(CURSOFF,end='')
    

def curseur_visible() : 
    print(CURSON,end='')
    

def move_to(lig, col) : 
    print("\033[" + str(lig) + ";" + str(col) + "f",end='')
    

def en_couleur(Coul) :    
    print(Coul,end='')
    

def en_rouge() : 
    print(CL_RED,end='') # Un exemple !
    

#-------------------------------------------------------
# La tache d'un cheval
def un_cheval(ma_ligne : int, keep_running) : # ma_ligne commence à 0
    col=1
    positions[i] = col
    while col < LONGEUR_COURSE and keep_running.value :
        
        with mutex :
            move_to(ma_ligne+1,col)         # pour effacer toute ma ligne
            erase_line_from_beg_to_curs()
            en_couleur(lyst_colors[ma_ligne%len(lyst_colors)])
            #mutex.acquire()
            #print('('+chr(ord('A')+ma_ligne)+'>')
            print(' _____\/')
            move_to(ma_ligne+2, col);erase_line_from_beg_to_curs()
            print('/|_'+chr(ord('A')+ma_ligne)+'__/')
            move_to(ma_ligne+3, col);erase_line_from_beg_to_curs()
            print(' /\  /|')
            col+=1
            positions[i] = col
        #mutex.release()
        
        try : # En cas d'interruption
            time.sleep(0.1 * random.randint(1,5))
        finally : 
            pass

#------------------------------------------------   
def prise_en_compte_signaux(signum, frame) :
    # On vient ici en cas de CTRL-C p. ex.
    move_to(Nb_process+11, 1)
    mutex.acquire()
    print(f"Il y a eu interruption No {signum} au clavier ..., on finit proprement")
    mutex.release()
    
    for i in range(Nb_process): 
        mes_process[i].terminate() 
    
    move_to(Nb_process+12, 1)
    curseur_visible()
    en_couleur(CL_WHITE)
    print("Fini")
    sys.exit(0)
# ---------------------------------------------------

# L'arbitre

def arbitre(positions,LONGEUR_COURSE):
    while keep_running.value:
        imax = 0
        imin = 0
        max = 0
        min = LONGEUR_COURSE
        for i in range(len(positions)):
            save = positions
            if positions[i]>= max:
                imax = i
                max = positions[i]
            if positions[i]<=min:
                imin = i
                min = positions[i]
        if max == LONGEUR_COURSE:
            break
                
        with mutex:
            move_to(Nb_process*3+5, 1)
            en_rouge()
            print("La vache en tête est la "+chr(ord('A')+imax*3))
            print("la vache en fin de course est la "+chr(ord('A')+imin*3))
    gagnant = ""
    tentative = []
    for i in range(len(save)):
        if save[i]==LONGEUR_COURSE:
            gagnant = gagnant + chr(ord('A')+i*3)
            tentative.append(i)
    with mutex:
        move_to(Nb_process*3+7, 1)
        print("La(Les) vache(s) gagnante(s) est(sont) la(les) "+gagnant)
        return tentative


# La partie principale :
if __name__ == "__main__" :
    print("Il y a 8 chevaux. Pariez sur le gagnant!")
    print("Le cheval A correspond au numéro 1, le cheval D au numéro 2 et ainsi de suite.")
    numero = input('Donner le gagnant : (avec un chiffre allant de 1 à 8) ')
    
    # Une liste de couleurs à affecter aléatoirement aux chevaux
    lyst_colors=[CL_WHITE, CL_BLACK, CL_RED, CL_GREEN, CL_BROWN , CL_BLUE, CL_MAGENTA, CL_CYAN, CL_GRAY,
                CL_DARKGRAY, CL_LIGHTRED, CL_LIGHTGREEN,  CL_LIGHTBLU, CL_YELLOW, CL_LIGHTMAGENTA, CL_LIGHTCYAN]
    
    LONGEUR_COURSE = 50 # Tout le monde aura la même copie (donc no need to have a 'value')
    
    keep_running=mp.Value(ctypes.c_bool, True)

    Nb_process=8
    positions = mp.Array('i',Nb_process)
    mes_process = [0 for i in range(Nb_process)]
    
    signal.signal(signal.SIGINT , prise_en_compte_signaux)
    signal.signal(signal.SIGQUIT , prise_en_compte_signaux)

    effacer_ecran()
    curseur_invisible()

    for i in range(Nb_process):  # Lancer     Nb_process  processus
        mes_process[i] = mp.Process(target=un_cheval, args= (i*3,keep_running,))
        mes_process[i].start()

    tentative = arbitre(positions,LONGEUR_COURSE)

    move_to(Nb_process*3+10, 1)

    #mutex.acquire()
    print("tous lancés, Controle-C pour tout arrêter")
    #mutex.release()

    # On attend la fin de la course
    for i in range(Nb_process): mes_process[i].join()

    move_to(Nb_process*3+12, 1)
    curseur_visible()

    result = False
    for i in range(len(tentative)):
        move_to(Nb_process*3+9, 1)
        if int(numero) == tentative[i]+1:
            result = True
    if result == True:
        print("Coup de chance? Vous avez bien jouer!")
    else:
        print("Pas de chance.")
