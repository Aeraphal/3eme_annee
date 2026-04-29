#Le Pendu
import random as rd

def Pendu(chance=int, best=int):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    erreur = chance
    lettredonne = ['initialisation']
    #Recherche du Mot
    with open('TP3/liste_francais_sans-accent.txt', 'r') as lst:
        liste=lst.readlines()
    #Randint pour prendre un mot aléatoire dans une liste
    recherche = rd.randint(0,len(liste))
    #On formate le mot en liste
    mot = liste[recherche]
    mot = mot.lower()
    mot = list(mot)
    mot.pop()
    secret = []
    #On effectue une série de _ _ _ _ _ suivant la taille du mot
    for i in range(len(mot)):
        secret.append('_')
    compteur = len(secret)
    #Input de lettres
    while erreur > 0 and compteur > 0:
        print(secret)
        #On place un input de lettre
        lettre = input('Donnez la lettre à analyser (en minuscule) : ')
        trouver = 0
        pos=[]
        delta = 0
        for i in range(0,len(alphabet)):
            #Si autre chose qu'une lettre est donné, on recommence le processus
            if lettre == alphabet[i]:
                #On sauvegarde la lettre dans une liste lettre faites et on recommence le processus si c'est déjà le cas.
                for k in range(0, len(lettredonne)):
                    if lettre == lettredonne[k] and len(lettredonne) > 1:
                        print('Vous avez déjà donné cette lettre, la preuve ici : ', lettredonne)
                        delta = 1
                if delta == 0:
                    lettredonne.append(lettre)
                    #vérification de l'input dans le mot
                    #On compare la lettre au travers de la totalité de la liste
                    for m in range(0, len(mot)):
                        if lettre==mot[m]:
                            trouver = trouver+1
                            pos.append(m)
                    #Si on ne trouve rien, chance - 1
                    if trouver == 0:
                        erreur = erreur - 1
                    #Sinon, cela veut dire qu'on trouve au moins une fois la lettre, _ => la lettre
                    else:
                        for p in range(0,len(pos)):
                            secret[pos[p]]=lettre
                            compteur = compteur - 1
        print("Il vous reste ", erreur, "chances.")
        print('')
    #Le pendu est terminé si le mot est fini ou si il n'y a plus de chance
    if compteur == 0:
        print(secret)
        print('Bravo! Vous avez réussi ce pendu!')
        best = erreur
    elif erreur == 0:
        print(secret)
        print('Vous avez échoué, il a fini au bucher alors que vous aviez ', chance, ' chances...')
    print('Rejouer?')
    replayPendu(best)


def replayPendu(best):
    replay = input('0 pour jouer, sinon tapez ce que vous souhaitez : ')
    truc = str(0)
    if replay == truc:
            #Cette partie ci dessous est facilement exploité pour buguer la machine. 
        #chance = input('Combien de chances souhaitez vous avoir? : ')
        #print('Vous aurez donc ', chance, "chances.")
        #chance = int(chance)
        print('Votre meilleur score est ', best, '! Bonne chance!')
        Pendu(7, best)
    else : 
        print('Au revoir en vous souhaitant une bonne journée!')
        return


replayPendu(0)




