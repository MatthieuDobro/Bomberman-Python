import sys
from PyQt5.QtWidgets import *
from random import *


class mouvement(QWidget) :
    def __init__(self, Map) :
        super(mouvement, self).__init__()
        self.map = Map

    def moveTop(self, n, nb):
        finiI = False
        finiJ = False
        i = 0
        while not finiI and i < len(self.map.Map1):
            j = 0
            while not finiJ and j < len(self.map.Map1[i]):

                if self.map.Map1[i][j] == nb:
                    if self.map.Map1[i - 1][j] == 1 or self.map.Map1[i - 1][j] in self.map.var.listePowerUp or self.map.Map1[i - 1][j] == 5 or self.map.Map1[i - 1][j] == 10:
                        if self.map.Map1[i - 1][j] == 6.2:
                            self.map.var.allowMoreBomb(n)
                        if self.map.Map1[i - 1][j] == 6.1:
                            self.map.var.allowMoreRange(n)
                        if self.map.Map1[i - 1][j] == 6.3:
                            self.map.var.setPyke(n)
                        if self.map.Map1[i - 1][j] == 6.1:
                            self.map.var.allowLessRange(n)
                        if self.map.Map1[i - 1][j] == 6.5:
                            self.map.var.setSkull(n)
                        if self.map.Map1[i - 1][j] == 6.6:
                            self.map.var.allowLessBomb(n)
                        if self.map.Map1[i - 1][j] == 5:
                            self.map.var.giveKey(n)
                        if self.map.Map1[i - 1][j] == 10 and self.map.var.checkKey(n):
                            self.map.victory(n)
                        


                        self.map.Map1[i - 1][j] = n
                        self.map.Map1[i][j] = 4
                        finiI = True
                        finiJ = True

                if self.map.Map1[i][j] == n:
                    if self.map.Map1[i - 1][j] == 1 or self.map.Map1[i - 1][j] in self.map.var.listePowerUp or self.map.Map1[i - 1][j] == 5 or self.map.Map1[i - 1][j] == 10:
                        if self.map.Map1[i - 1][j] == 6.2:
                            self.map.var.allowMoreBomb(n)
                        if self.map.Map1[i - 1][j] == 6.1:
                            self.map.var.allowMoreRange(n)
                        if self.map.Map1[i - 1][j] == 6.4:
                            self.map.var.allowLessRange(n)
                        if self.map.Map1[i - 1][j] == 6.3:
                            self.map.var.setPyke(n)
                        if self.map.Map1[i - 1][j] == 6.5:
                            self.map.var.setSkull(n)
                            
                        if self.map.Map1[i - 1][j] == 6.6:
                            self.map.var.allowLessBomb(n)
                        if self.map.Map1[i - 1][j] == 5:
                            self.map.var.giveKey(n)
                        if self.map.Map1[i - 1][j] == 10 and self.map.var.checkKey(n):
                            self.map.victory(n)

                           
                        self.map.Map1[i - 1][j] = n
                        self.map.Map1[i][j] = 1
                        finiI = True
                        finiJ = True

                j += 1
            i += 1
        self.map.update()

    # Ici, c'est déplacement vers la gauche

    def moveLeft(self, n, nb):
        finiI = False
        finiJ = False
        i = 0
        while not finiI and i < len(self.map.Map1):
            j = 0
            while not finiJ and j < len(self.map.Map1[i]):

                if self.map.Map1[i][j] == nb:
                    if self.map.Map1[i][j - 1] == 1 or self.map.Map1[i][j - 1] in self.map.var.listePowerUp or self.map.Map1[i][j - 1] == 5 or self.map.Map1[i - 1][j] == 10:
                        if self.map.Map1[i][j - 1] == 6.2:
                            self.map.var.allowMoreBomb(n)
                        if self.map.Map1[i][j - 1] == 6.1:
                            self.map.var.allowMoreRange(n)
                        if self.map.Map1[i][j - 1] == 6.4:
                            self.map.var.allowLessRange(n)
                        if self.map.Map1[i][j - 1] == 6.3:
                            self.map.var.setPyke(n)
                        if self.map.Map1[i][j - 1] == 6.5:
                            self.map.var.setSkull(n)
                        
                        if self.map.Map1[i][j - 1] == 6.6:
                            self.map.var.allowLessBomb(n)
                        
                        if self.map.Map1[i][j - 1] == 5:
                            self.map.var.giveKey(n)

                        if self.map.Map1[i - 1][j] == 10 and self.map.var.checkKey(n):
                            self.map.victory(n)

                        self.map.Map1[i][j - 1] = n
                        self.map.Map1[i][j] = 4
                        finiI = True
                        finiJ = True

                if self.map.Map1[i][j] == n:
                    if self.map.Map1[i][j - 1] == 1 or self.map.Map1[i][j - 1] in self.map.var.listePowerUp or self.map.Map1[i][j - 1] == 5 or self.map.Map1[i - 1][j] == 10:
                        if self.map.Map1[i][j - 1] == 6.2:
                            self.map.var.allowMoreBomb(n)
                        if self.map.Map1[i][j - 1] == 6.1:
                            self.map.var.allowMoreRange(n)
                        if self.map.Map1[i][j - 1] == 6.3:
                            self.map.var.setPyke(n)
                        if self.map.Map1[i][j - 1] == 6.4:
                            self.map.var.allowLessRange(n)
                        if self.map.Map1[i][j - 1] == 6.5:
                            self.map.var.setSkull(n)
                        
                        if self.map.Map1[i][j - 1] == 6.6:
                            self.map.var.allowLessBomb(n)
                        if self.map.Map1[i][j - 1] == 5:
                            self.map.var.giveKey(n)
                        if self.map.Map1[i - 1][j] == 10 and self.map.var.checkKey(n):
                            self.map.victory(n)

                        self.map.Map1[i][j - 1] = n
                        self.map.Map1[i][j] = 1
                        finiI = True
                        finiJ = True

                j += 1
            i += 1
        self.map.update()

    # Ici, c'est déplacement vers le bas

    def moveDown(self, n, nb):
        finiI = False
        finiJ = False
        i = 0
        while not finiI and i < len(self.map.Map1):
            j = 0
            while not finiJ and j < len(self.map.Map1[i]):

                if self.map.Map1[i][j] == nb:
                    if self.map.Map1[i + 1][j] == 1 or self.map.Map1[i + 1][j] in self.map.var.listePowerUp or self.map.Map1[i + 1][j] == 5 or self.map.Map1[i - 1][j] == 10:
                        if self.map.Map1[i + 1][j] == 6.2:
                            self.map.var.allowMoreBomb(n)
                        if self.map.Map1[i + 1][j] == 6.1:
                            self.map.var.allowMoreRange(n)
                        if self.map.Map1[i + 1][j] == 6.3:
                            self.map.var.setPyke(n)
                        if self.map.Map1[i + 1][j] == 6.4:
                            self.map.var.allowLessRange(n)
                        if self.map.Map1[i + 1][j] == 6.5:
                            self.map.var.setSkull(n)
                        
                        if self.map.Map1[i + 1][j] == 6.6:
                            self.map.var.allowLessBomb(n)
                        
                        if self.map.Map1[i + 1][j] == 5:
                            self.map.var.giveKey(n)

                        if self.map.Map1[i - 1][j] == 10 and self.map.var.checkKey(n):
                            self.map.victory(n)

                        self.map.Map1[i + 1][j] = n
                        self.map.Map1[i][j] = 4
                        finiI = True
                        finiJ = True

                if self.map.Map1[i][j] == n:
                    if self.map.Map1[i + 1][j] == 1 or self.map.Map1[i + 1][j] in self.map.var.listePowerUp or self.map.Map1[i + 1][j] == 5 or self.map.Map1[i - 1][j] == 10:
                        if self.map.Map1[i + 1][j] == 6.2:
                            self.map.var.allowMoreBomb(n)
                        if self.map.Map1[i + 1][j] == 6.1:
                            self.map.var.allowMoreRange(n)
                        if self.map.Map1[i + 1][j] == 6.3:
                            self.map.var.setPyke(n)
                        if self.map.Map1[i + 1][j] == 6.4:
                            self.map.var.allowLessRange(n)
                        if self.map.Map1[i + 1][j] == 6.5:
                            self.map.var.setSkull(n)
                        
                        if self.map.Map1[i + 1][j] == 5:
                            self.map.var.giveKey(n)
                        
                        if self.map.Map1[i + 1][j] == 6.6:
                            self.map.var.allowLessBomb(n)

                        if self.map.Map1[i - 1][j] == 10 and self.map.var.checkKey(n):
                            self.map.victory(n)
                        self.map.Map1[i + 1][j] = n
                        self.map.Map1[i][j] = 1
                        finiI = True
                        finiJ = True

                j += 1
            i += 1
        self.map.update()

    # Ici, c'est déplacement vers la droite

    def moveRight(self, n, nb):
        finiI = False
        finiJ = False
        i = 0
        while not finiI and i < len(self.map.Map1):
            j = 0
            while not finiJ and j < len(self.map.Map1[i]):

                if self.map.Map1[i][j] == nb:
                    if self.map.Map1[i][j + 1] == 1 or self.map.Map1[i][j + 1] in self.map.var.listePowerUp or self.map.Map1[i][j + 1] == 5 or self.map.Map1[i - 1][j] == 10:
                        if self.map.Map1[i][j + 1] == 6.2:
                            self.map.var.allowMoreBomb(n)
                        if self.map.Map1[i][j + 1] == 6.1:
                            self.map.var.allowMoreRange(n)
                        if self.map.Map1[i][j + 1] == 6.4:
                            self.map.var.allowLessRange(n)
                        if self.map.Map1[i][j + 1] == 6.3:
                            self.map.var.setPyke(n)
                        if self.map.Map1[i][j + 1] == 6.5:
                            self.map.var.setSkull(n)
                        if self.map.Map1[i][j + 1] == 6.6:
                            self.map.var.allowLessBomb(n)
                        if self.map.Map1[i][j + 1] == 5:
                            self.map.var.giveKey(n)
                        if self.map.Map1[i - 1][j] == 10 and self.map.var.checkKey(n):
                            self.map.victory(n)

                        self.map.Map1[i][j + 1] = n
                        self.map.Map1[i][j] = 4
                        finiI = True
                        finiJ = True

                if self.map.Map1[i][j] == n:
                    if self.map.Map1[i][j + 1] == 1 or self.map.Map1[i][j + 1] in self.map.var.listePowerUp or self.map.Map1[i][j + 1] == 5 or self.map.Map1[i - 1][j] == 10:
                        if self.map.Map1[i][j + 1] == 6.2:
                            self.map.var.allowMoreBomb(n)
                        if self.map.Map1[i][j + 1] == 6.1:
                            self.map.var.allowMoreRange(n)
                        if self.map.Map1[i][j + 1] == 6.4:
                            self.map.var.allowLessRange(n)
                        if self.map.Map1[i][j + 1] == 6.3:
                            self.map.var.setPyke(n)
                        if self.map.Map1[i][j + 1] == 5:
                            self.map.var.giveKey(n)

                        if self.map.Map1[i][j + 1] == 6.5:
                            self.map.var.setSkull(n)
                        
                        if self.map.Map1[i][j + 1] == 6.6:
                            self.map.var.allowLessBomb(n)
                        if self.map.Map1[i - 1][j] == 10 and self.map.var.checkKey(n):
                            self.map.victory(n)

                        self.map.Map1[i][j + 1] = n
                        self.map.Map1[i][j] = 1
                        finiI = True
                        finiJ = True

                j += 1
            i += 1
        self.map.update()