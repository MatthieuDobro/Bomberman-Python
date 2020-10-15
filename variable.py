import sys
from PyQt5.QtWidgets import *

class var(QWidget) :
    def __init__(self) :
        super(var, self).__init__()
        
        self.listePowerUp = [6.1, 6.2, 6.3, 6.4, 6.5, 6.6]
        self.listeJoueur = [3, 7, 8, 9]
        self.listeBombeJ = [34, 74, 84, 94]
        self.MAXBOMB = 8
        self.MAXFIRE = 8
        self.score_j1 = 0
        self.nbBombeJ1 = 0
        self.allowedBombJ1 = 1
        self.rangej1 = 1
        self.score_j2 = 0
        self.nbBombeJ2 = 0
        self.allowedBombJ2 = 1
        self.rangej2 = 1
        self.score_j3 = 0
        self.nbBombeJ3 = 0
        self.allowedBombJ3 = 1
        self.rangej3 = 1
        self.score_j4 = 0
        self.nbBombeJ4 = 0
        self.allowedBombJ4 = 1
        self.rangej4 = 1
        self.stopIA2 = False
        self.stopIA3 = False
        self.stopIA4 = False
        self.keyJ1=False
        self.keyJ2=False
        self.keyJ3=False
        self.keyJ4=False

        

        # Ce sont toutes nos variables qui nous serviront plus tard dans le code
        
        self.posJ1 = 1  # Sert à savoir dans quelle direction est allée le joueur 1 en dernier
        self.bombeJ1 = "bomb"  # Sert à connaitre le type de la bombe duu joueur 1
        self.stateJ1 = "normal"  # Sert à savoir si le joueur 1 a ramassé un crâne ou non
        self.movementJ1 = 0  # Sert à animer le sprite quand on se déplace
        self.posJ2 = 1
        self.bombeJ2 = "bomb"
        self.stateJ2 = "normal"
        self.posJ3 = 0
        self.bombeJ3 = "bomb"
        self.stateJ3 = "normal"
        self.movementJ3 = 0
        self.posJ4 = 0
        self.bombeJ4 = "bomb"
        self.stateJ4 = "normal"
        self.movementJ4 = 0

    def giveKey(self,n):
        if n==3:
            self.keyJ1=True
        
        if n==7:
            self.keyJ2=True
        
        if n==8:
            self.keyJ3=True
        
        if n==9:
            self.keyJ4=True
        
    def checkKey(self,n):
        if n==3:
            return self.keyJ1
        
        if n==7:
            return self.keyJ2
        
        if n==8:
            return self.keyJ3
        
        if n==9:
            return self.keyJ4
        
        
    def gainPoint(self, n):
        if n == 3:
            self.score_j1 += 1

        elif n == 7:
            self.score_j2 += 1

        elif n == 8:
            self.score_j3 += 1

        elif n == 9:
            self.score_j4 += 1

    # Cette def permet de changer le type de bombe d'un joueur quand il prend le bonus pyke

    def setPyke(self, n):
        if n == 3:
            self.bombeJ1 = "pyke"
        elif n == 7:
            self.bombeJ2 = "pyke"
        elif n == 8:
            self.bombeJ3 = "pyke"
        elif n == 9:
            self.bombeJ4 = "pyke"


    # Cette def nous permet de connaitre la range.

    def range(self, n):
        if n == 3:
            return self.rangej1

        if n == 7:
            return self.rangej2

        if n == 8:
            return self.rangej3

        if n == 9:
            return self.rangej4

    # Quand on tue un joueur, faut bien etre récompensé. On gagne donc des points

    def gainPointKill(self, n, a):
        if n == 3 and (a == 7 or a == 8 or a == 9):
            self.score_j1 += 5
            

        if n == 7 and (a == 9 or a == 8 or a == 3):
            self.score_j2 += 5

        if n == 8 and (a == 9 or a == 7 or a == 3):
            self.score_j3 += 5

        if n == 9 and (a == 3 or a == 8 or a == 7):
            self.score_j4 += 5
        
    # Cette def nous permet de connaitre combien de bombe sont posées sur le terrain

    def checkbombe(self, n):
        if n == 3:
            return self.nbBombeJ1

        elif n == 7:
            return self.nbBombeJ2

        elif n == 8:
            return self.nbBombeJ3

        elif n == 9:
            return self.nbBombeJ4

    # Cette def permet d'ajouter au compteur une bombe qui servira à savoir si le joueur peut encore poser une bombe.

    def addBomb(self, n):
        if n == 3:
            self.nbBombeJ1 += 1
        elif n == 7:
            self.nbBombeJ2 += 1
        elif n == 8:
            self.nbBombeJ3 += 1

        elif n == 9:
            self.nbBombeJ4 += 1

    # Cette def permet retirer au compteur une bombe.

    def removeBomb(self, n):
        if n == 3:
            self.nbBombeJ1 -= 1

        elif n == 7:
            self.nbBombeJ2 -= 1

        elif n == 8:
            self.nbBombeJ3 -= 1

        elif n == 9:
            self.nbBombeJ4 -= 1

    # Cette def nous permet de connaitre le nombre de bombe qu'un joueur peut poser au total

    def allowedBomb(self, n):
        if n == 3:
            return self.allowedBombJ1

        elif n == 7:
            return self.allowedBombJ2

        elif n == 8:
            return self.allowedBombJ3

        elif n == 9:
            return self.allowedBombJ4

    # Cette def nous permet d'ajouter au nombre de bombe posable une bombe supplémentaire

    def allowMoreBomb(self, n):
        if n == 3:
            self.allowedBombJ1 += 1

        elif n == 7:
            self.allowedBombJ2 += 1

        elif n == 8:
            self.allowedBombJ3 += 1

        elif n == 9:
            self.allowedBombJ4 += 1

    # Cette def nous permet de retirer une bombe au nombre de bombe posable

    def allowLessBomb(self, n):
        
        if n == 3:
            if self.allowedBombJ1 > 1:
                self.allowedBombJ1 -= 1
            

        elif n == 7:
            if self.allowedBombJ2 > 1:
                self.allowedBombJ2 -= 1
            

        elif n == 8:
            if self.allowedBombJ3 > 1:
                self.allowedBombJ3 -= 1
            

        elif n == 9:
            if self.allowedBombJ4 > 1:
                self.allowedBombJ4 -= 1
            

    # Cette def nous permet d'augmenter la distance de la flamme du joueur

    def allowMoreRange(self, n):

        if n == 3:
            self.rangej1 += 1

        elif n == 7:
            self.rangej2 += 1

        elif n == 8:
            self.rangej3 += 1

        elif n == 9:
            self.rangej4 += 1

    # Cette def nous permet de retirer 1 à la longueur de notre flamme

    def allowLessRange(self, n):
        if n == 3:
            if self.range(3) > 1:
                self.rangej1 -= 1
        elif n == 7:
            if self.range(7) > 1:
                self.rangej2 -= 1
        elif n == 8:
            if self.range(8) > 1:
                self.rangej3 -= 1

        elif n == 9:
            if self.range(9) > 1:
                self.rangej4 -= 1

    # Ces defs servent à réinitialiser l'état du joueur

    def resetSkullJ1(self):
        self.stateJ1 = "normal"

    def resetSkullJ2(self):
        self.stateJ2 = "normal"

    def resetSkullJ3(self):
        self.stateJ3 = "normal"

    def resetSkullJ4(self):
        self.stateJ4 = "normal"

    # Et celle la au contraire, elle modifie l'état du joueur

    def setSkull(self, n):
        if n == 3:
            if self.stateJ1 == "normal":
                self.stateJ1 = "skull"
        if n == 8:
            if self.stateJ2 == "normal":
                self.stateJ2 = "skull"

        if n == 8:
            if self.stateJ3 == "normal":
                self.stateJ3 = "skull"

        if n == 9:
            if self.stateJ4 == "normal":
                self.stateJ4 = "skull"
