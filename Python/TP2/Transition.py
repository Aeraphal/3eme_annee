#On importe json, la ou se trouve nos fichiers à lire.
import json

#Le dictionnaire de mot

dictionnaire ={"le" : 0, "la" : 0, "chat" : 2, "souris" : 2, "martin" : 4,
"mange" : 3, "la" : 0, "petite" : 1, "joli" : 1, "grosse" : 1, "bleu" : 1, 
"verte" : 1, "dort" : 3,"julie" : 4, "jean" : 4, "." : 5}

Phrase = "le petite chat mange julie ."

#La table de transitions d'état

def Table_de_Transition(pos,obj):
    Transition = [
    [1,8,8,8,4,8],
    [8,1,2,8,8,8],
    [8,2,8,3,8,8],
    [5,8,8,8,7,9],
    [8,8,8,3,8,8],
    [8,5,6,8,8,8],
    [8,6,8,8,8,9],
    [8,8,8,8,8,9]]
    return Transition[pos][obj]


def verif_phrase(phrase):
#J'ai eut un problème de chemin. __file__ nous donne le chemin absolue vers la fonction voulue!
    print(__file__)
    with open('TP2/dictionnaire.json') as dico_json:
        dictionnaire=json.load(dico_json)
#On enlève toutes les majuscules et on retire la ponctuation.
    phrase = phrase.replace(",", "")
    phrase = phrase.replace(";", "")
    phrase = phrase.replace(":", "")
    phrase = phrase.replace(".", " .")
    phrase_lower = phrase.lower()
#Le .split découpe les mots à pratir des espaces dans la phrase.   
    Phrase_test = phrase_lower.split()
    pos=0
    for i in Phrase_test:
        obj = dictionnaire[i]
        pos = Table_de_Transition(pos,obj)

        if pos == 8:
            return False
        if pos == 9:
            return True

def verif():
    phrase = input("Inserer une phrase! : ")
    if verif_phrase(phrase,) == True:
        print("Cette phrase est correcte.")
    else:
        print("Cette phrase est incorrecte.")


verif()