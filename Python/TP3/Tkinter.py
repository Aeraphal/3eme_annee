from tkinter import Label, Tk, Frame,Button
import tkinter as Tk
#Initialisation de Variables

image1 = Tk.PhotoImage('bonhomme1.gif')
image2 = Tk.PhotoImage('bonhomme2.gif')
image3 = Tk.PhotoImage('bonhomme3.gif')
image4 = Tk.PhotoImage('bonhomme4.gif')
image5 = Tk.PhotoImage('bonhomme5.gif')
image6 = Tk.PhotoImage('bonhomme6.gif')
image7 = Tk.PhotoImage('bonhomme7.gif')
image8 = Tk.PhotoImage('bonhomme8.gif')



#Création de Fonctions

def Penduf():
    return 1


#La page Tkinter

pendu = Tk()
pendu.title('Jeu du pendu')


textPendu = Label(pendu, text = "aa")
textPendu.pack(side = 'top', padx=10, pady=10)

chancePendu = Label(pendu)
chancePendu.pack(side = 'right', padx=10, pady=10)

boutonPendu = Button(pendu, text = "Proposer", relief = 'groove', command = Penduf)
boutonPendu.pack(side = 'bottom', padx = 5, pady = 5)


lettre = Tk.StringVar()

ProposerPendu = Tk.Entry(pendu, textvariable = lettre)
ProposerPendu.pack(side = 'bottom', padx = 1, pady = 1)

Longueur = 400
Largeur = 300
CanvasPendu = Tk.Canvas(pendu, width = Largeur, height = Longueur, bg='white')
CanvasPendu.pack(side = 'right')




pendu.mainloop()
