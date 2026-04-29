import sys, os, signal, time
verif = True
print("Entrez un entier en moins de 5 secondes")
signal.alarm(5)

while verif == True:
    k = input("Svp un entier : ")
    try :
        k = int(k)
    except :
        print("Veuillez recommencez")

    else :
        print("Super bien joué!")
        verif = False


if verif == False:
    sys.exit()


