###Début Projet

import tkinter as tk
import random as rd

#Fonctions

def Recommencer(x, y):
    x = 300
    y = 200
    taille = [x, y]



#Fenetre

snake = tk.Tk()
snake.title('SNAKE!')


Largeur = 600
Hauteur = 400

Terrain = tk.Canvas(snake, height=Hauteur, width=Largeur, bg='yellow')
Terrain.pack(padx=5, pady=5)

#essai_tete = tk.Canvas(snake, height=20, width=20, fill='green')
#essai_tete.pack()


score = tk.Label(snake, text = '0', fg = 'yellow')
score.pack()

#Boutons

ButtonStart = tk.Button(snake, text = 'Nouvelle partie!', command = Recommencer)
ButtonStart.pack()


ButtonEnd = tk.Button(snake, text = 'Quitter?', command = snake.destroy)
ButtonEnd.pack()

    #MENU!!!



#pomme = snake.create_oval(7,7)
#pomme.coords(0,1)

    #Le Jardin

class jardin:
    def __init__(self, canvas, window=None):
        self.canvas = canvas
        self.window = window
        self.serpent=[]
        self.pomme=[]

        

    #Serpent

class serpent:
    def __init__(self, x, y, taille):
        self.x = x
        self.y = y
        self.head = [20, 20]
        self.tete = []
        self.taille = taille
        self.corps = tk.create_rectangle(Hauteur/2 -10, Largeur/2 - 10, Hauteur/2 + 10, Largeur/2 + 10)
        self.canvas_image = self.canvas.create_image(self.x,self.y, anchor="snake", image = self.corps)


    def haut(self, event):
        self.taille.append([self.x, self.y + 20])
        self.y = self.y + 20
        self.taille.pop(0)

    def bas(self, event):
        self.taille.append([self.x, self.y - 20])
        self.y = self.y - 20
        self.taille.pop(0)

    def droite(self, event):
        self.taille.append([self.x + 20, self.y])
        self.x = self.x + 20
        self.taille.pop(0)

    def gauche(self, event):
        self.taille.append([self.x - 20, self.y])
        self.x = self.x - 20
        self.taille.pop(0)




class tete:
    def __init__(self, canvas, x, y, window = None):
        self.x = x
        self.y = y



#Pomme

class pomme:
    def __init__(self, canvas, taille, window = None):
        pass



    def Pomme(self, taille):
        x = rd.randint(0,Largeur)
        y = rd.randint(0,Hauteur)
        rayon = 7 
        #Rajout condition sur la taille
        Terrain.create_oval(x-7, y-7, x+7, y+7, fill='red')
        
#Déplacement
snake.bind("<Keypress-a>", lambda e : serpent.haut(e))
snake.bind("<Keypress-q>", lambda e : serpent.bas(e))
snake.bind("<Keypress-o>", lambda e : serpent.gauche(e))
snake.bind("<Keypress-p>", lambda e : serpent.droite(e))
snake.after(20, snake.deplacement)


snake.mainloop()




