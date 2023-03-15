from tkinter import *
import turtle

class Queen :
    def __init__(self, num, row, column):
        self.num = num
        self.row = row
        self.column = column
        



class Echiquier :
    def __init__(self):
        self.cote = 8
        self.Grille = [[' _ ' for _ in range(self.cote)] for _ in range(self.cote)]
        self.compteur = 0
        
    def display(self):
        for i in range(self.cote):
            
            for j in range(self.cote):
                
                print(self.Grille[i][j],end='')
            print('')
            
    def placeQueen(self,i,j):
        self.Grille[i][j] = Queen(self.compteur,i,j)
        self.compteur = self.compteur + 1
        
    def deplaceQueen(self,i,j):
        if(j<self.cote-1) : 
            temp = self.Grille[i][j+1]
            self.Grille[i][j+1] = self.Grille[i][j]
            self.Grille[i][j] = temp
        elif(j==self.cote-1 and i <self.cote-1) :
            temp = self.Grille[i+1][0]
            self.Grille[i+1][0] = self.Grille[i][j]
            self.Grille[i][j] = temp

    def verrif(self):
        res = True
        
             
myEchiquier = Echiquier()
myEchiquier.placeQueen(3,3)

myEchiquier.display()