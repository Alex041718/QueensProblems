from tkinter import *
import turtle
class Echiquier :
    def __init__(self):
        self.cote = 8
        self.Grille = [[' ♛ ' for _ in range(self.cote)] for _ in range(self.cote)]
        
    def display(self):
        for i in range(self.cote):
            
            for j in range(self.cote):
                
                print(self.Grille[i][j],end='')
            print('')
                
myEchiquier = Echiquier()

myEchiquier.display()