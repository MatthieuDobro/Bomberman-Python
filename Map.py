import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
import os
from random import *
from time import *
from sprite import *
from variable import *
from IA import *
from mouvement import *
from bombe import *


class Map(QWidget):
    def __init__(self, main, parent=None):
        super(Map, self).__init__(parent)
        self.main = main
        self.sprite = sprite()
        self.var = var()
        self.ia = ia(self)
        self.mouvement = mouvement(self)
        self.bombe = bombe(self)

        self.timerIA2 = QTimer()
        self.timerIA2.timeout.connect(self.ia.moveIA2)
        
        self.timerIA3 = QTimer(self)
        self.timerIA3.timeout.connect(self.ia.moveIA3)

        self.timerIA4 = QTimer(self)
        self.timerIA4.timeout.connect(self.ia.moveIA4)

        self.sj1 = QLabel("Score joueur 1", self)
        self.sj2 = QLabel("Score joueur 2", self)
        self.sj3 = QLabel("Score joueur 3", self)
        self.sj4 = QLabel("Score joueur 4", self)
        self.sj1.setMinimumWidth(self.width() / 2)
        self.sj2.setMinimumWidth(self.width() / 2)
        self.sj3.setMinimumWidth(self.width() / 2)
        self.sj4.setMinimumWidth(self.width() / 2)
        self.sj1.setStyleSheet("QLabel {background: #FF0000; border-radius: 10px; color: white; font: bold 27px; border: 1.5px " \
                               "solid black; height: 85; width: 305; margin: 8px;}")
        self.sj2.setStyleSheet("QLabel {background: #0000FF; border-radius: 10px; color: white; font: bold 27px; border: 1.5px " \
                               "solid black; height: 85; width: 305; margin: 8px;}")
        self.sj3.setStyleSheet("QLabel {background: #FFF300; border-radius: 10px; color: white; font: bold 27px; border: 1.5px " \
                               "solid black; height: 85; width: 305; margin: 8px;}")
        self.sj4.setStyleSheet("QLabel {background: #FF00FF; border-radius: 10px; color: white; font: bold 27px; border: 1.5px " \
                               "solid black; height: 85; width: 305; margin: 8px;}")
        # On initialise le focus sur notre clavier pour pouvoir controler nos personnages
        self.setFocusPolicy(Qt.StrongFocus)

        # On déclare les label dans lequels on trouvera les scores de chaques joueurs

        self.sj1.setText("Score Rouge : " + str(self.var.score_j1))
        self.sj2.setText("Score Bleu : " + str(self.var.score_j2))
        self.sj3.setText("Score Jaune : " + str(self.var.score_j3))
        self.sj4.setText("Score Rose : " + str(self.var.score_j4))
    
        self.sj1.move(10, 10)
        self.sj2.move(10, 70)
        self.sj3.move(10, 130)
        self.sj4.move(10, 190)

    def initUI(self):
        pass
        # Ici, bah on fait rien

    def setOriginalFigure(self):
        # On définit notre rectancle de départ
        original = QRect(400, 50, 50, 50)
        return original

    def transformFigure(self, original, degrees):
        # On transforme notre rectancle de départ (Pour + d'infos, contactez Maxime Dujardin)

        res = original.translated(degrees)
        return res

    # Ici, c'est notre map de base. Chaque numéro correspond a un carré d'une couleur différentes :
    # 0 Block cassable
    # 1 Zone libre
    # 2 Block incassable
    # 3 Joueur 1
    # 4 Bombe
    # 5 Flamme
    # Power-up   6.1 FireUp   6.2 BombUp   6.3 pykeBomb   6.4 FireDown   6.5 Skull   6.6 BombDown
    # 7 Joueur 2
    # 8 Joueur 3
    # 9 Joueur 4
    # 34 Joueur + bombe
    # 74 Joueur 2 + Bombe
    # 84 Joueur 3 + Bombe
    # 94 Joueur 4 + Bombe

    Map1 = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 7, 2],
            [2, 1, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 1, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 1, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 1, 2],
            [2, 8, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]

    # Cette double boucle for nous sert à randomizer notre terrain à chaque partie
    for i in range(1, 18):
        for j in range(1, 20):
            if Map1[i][j] == 0:
                k = randint(1, 4)
                if k == 4:
                    Map1[i][j] = 1

    def findJoueur(self, n):
        # Cette def nous permet de savoir quel joueur est encore en vie
        # Ces booléens passeront à True si le joueur est trouvé car pour l'instant, nous ne savons pas si il est en vie
        bleu = False
        rouge = False
        jaune = False
        rose = False
        finiI = False
        finiJ = False
        i = 0
        j = 0
        saveI1 = 0 
        saveJ1 = 0
        saveI2 = 0 
        saveJ2 = 0
        saveI3 = 0 
        saveJ3 = 0
        saveI4 = 0 
        saveJ4 = 0
        while i < len(self.Map1):
            while j < len(self.Map1[i]):
                if self.Map1[i][j] == 3 or self.Map1[i][j] == 34:
                    rouge = True
                    saveI1 = i
                    saveJ1 = j 

                if self.Map1[i][j] == 7 or self.Map1[i][j] == 74:
                    bleu = True
                    saveI2 = i 
                    saveJ2 = j 

                if self.Map1[i][j] == 8 or self.Map1[i][j] == 84:
                    jaune = True
                    saveI3 = i 
                    saveJ3 = j 

                if self.Map1[i][j] == 9 or self.Map1[i][j] == 94:
                    rose = True
                    saveI4 = i 
                    saveJ4 = j

                j += 1
            i += 1
            j = 0

        if n == 0:
            return rouge, bleu, jaune, rose

        elif n == 1:
            return rouge, saveI1, saveJ1

        elif n == 2:
            return bleu, saveI2, saveJ2

        elif n == 3:
            return jaune, saveI3, saveJ3

        elif n == 4:
            return rose, saveI4, saveJ4

    def paintEvent(self, event):
        # Ici, on fait plein de trucs cool

        # Par exemple, on lance une nouvelle musique quand on arrive sur le terrain.

        # Ca ? Je sais pas. Demandez à mon équipe

        self.xc = self.width() * 0.5
        self.yc = self.height() * 0.5

        # On déclare notre rectangle de base

        original = self.setOriginalFigure()

        # On déclare notre Painter

        painter = QPainter(self)

        # Ca ? C'est pour dessiner notre map. Il parcourt notre matrice et place le rectangle de la couleur associée au numéro

        cpt1 = 0
        cpt2 = 0
        for i in range(0, len(self.Map1)):
            cpt1 = 0
            for j in range(0, len(self.Map1[i])):

                if self.Map1[i][j] == 2:
                    pen = QBrush()
                    pen.setTexture(self.sprite.texture['pierre'])
                    rec = self.transformFigure(original, QPoint(cpt1, cpt2))
                    cpt1 += 50

                elif self.Map1[i][j] == 0:
                    pen = QBrush()
                    pen.setTexture(self.sprite.texture['brique'])
                    rec = self.transformFigure(original, QPoint(cpt1, cpt2))
                    cpt1 += 50

                elif self.Map1[i][j] == 3:
                    pen = QBrush()
                    pen.setTexture(self.sprite.spriteJ1[self.var.posJ1][self.var.movementJ1])

                    rec = self.transformFigure(original, QPoint(cpt1, cpt2))
                    cpt1 += 50

                elif self.Map1[i][j] == 34:
                    pen = QBrush(Qt.darkRed)
                    pen.setTexture(self.sprite.texture['erenBomb'])
                    rec = self.transformFigure(original, QPoint(cpt1, cpt2))
                    cpt1 += 50

                elif self.Map1[i][j] == 4:
                    pen = QBrush()
                    pen.setTexture(self.sprite.texture['bombe'])
                    rec = self.transformFigure(original, QPoint(cpt1, cpt2))
                    cpt1 += 50

                elif self.Map1[i][j] == 7:
                    pen = QBrush(Qt.blue)
                    pen.setTexture(self.sprite.spriteJ2[self.var.posJ2])
                    rec = self.transformFigure(original, QPoint(cpt1, cpt2))
                    cpt1 += 50

                elif self.Map1[i][j] == 74:
                    pen = QBrush()
                    pen.setTexture(self.sprite.texture['dkBomb'])
                    rec = self.transformFigure(original, QPoint(cpt1, cpt2))
                    cpt1 += 50


                elif self.Map1[i][j] == 8:
                    pen = QBrush()
                    pen.setTexture(self.sprite.spriteJ3[self.var.posJ3][self.var.movementJ3])
                    rec = self.transformFigure(original, QPoint(cpt1, cpt2))
                    cpt1 += 50


                elif self.Map1[i][j] == 84:
                    pen = QBrush()
                    pen.setTexture(self.sprite.texture['bomberBomb'])
                    rec = self.transformFigure(original, QPoint(cpt1, cpt2))
                    cpt1 += 50

                elif self.Map1[i][j] == 9:
                    pen = QBrush()
                    pen.setTexture(self.sprite.spriteJ4[self.var.posJ4][self.var.movementJ4])
                    rec = self.transformFigure(original, QPoint(cpt1, cpt2))
                    cpt1 += 50

                elif self.Map1[i][j] == 94:
                    pen = QBrush()
                    pen.setTexture(self.sprite.texture['trumpBomb'])
                    rec = self.transformFigure(original, QPoint(cpt1, cpt2))
                    cpt1 += 50

                elif self.Map1[i][j] == 6.1:
                    pen = QBrush()
                    pen.setTexture(self.sprite.texture['fire'])
                    rec = self.transformFigure(original, QPoint(cpt1, cpt2))
                    cpt1 += 50

                elif self.Map1[i][j] == 6.2:
                    pen = QBrush()
                    pen.setTexture(self.sprite.texture['bomb'])
                    rec = self.transformFigure(original, QPoint(cpt1, cpt2))
                    cpt1 += 50

                elif self.Map1[i][j] == 6.3:
                    pen = QBrush()
                    pen.setTexture(self.sprite.texture['pyke'])
                    rec = self.transformFigure(original, QPoint(cpt1, cpt2))
                    cpt1 += 50

                elif self.Map1[i][j] == 6.4:
                    pen = QBrush()
                    pen.setTexture(self.sprite.texture['firedown'])
                    rec = self.transformFigure(original, QPoint(cpt1, cpt2))
                    cpt1 += 50

                elif self.Map1[i][j] == 6.5:
                    pen = QBrush()
                    pen.setTexture(self.sprite.texture['skull'])
                    rec = self.transformFigure(original, QPoint(cpt1, cpt2))
                    cpt1 += 50
                elif self.Map1[i][j] == 6.6:
                    pen = QBrush()
                    pen.setTexture(self.sprite.texture['bombDown'])
                    rec = self.transformFigure(original, QPoint(cpt1, cpt2))
                    cpt1 += 50
                else:
                    pen = QBrush(Qt.transparent)
                    rec = self.transformFigure(original, QPoint(cpt1, cpt2))
                    cpt1 += 50

                painter.setPen(Qt.transparent)
                painter.setBrush(pen)
                painter.drawRect(rec)
            cpt2 += 50  # Oui il était long mais très efficace

        
        if not self.timerIA2.isActive() and not self.var.stopIA2:
            self.timerIA2.start(500)
        
        if not self.timerIA3.isActive() and not self.var.stopIA3:
            self.timerIA3.start(500)
            

        if not self.timerIA4.isActive() and not self.var.stopIA4:
            self.timerIA4.start(500)


        # Ca c'est pour savoir cb de joueurs sont encore en vie sur le terrain. On réutilise la fonction findJoueur pour cela
        cptJoueur = 0

        if self.findJoueur(1)[0]:
            cptJoueur += 1

        if self.findJoueur(0)[1]:
            cptJoueur += 1

        if self.findJoueur(0)[2]:
            cptJoueur += 1

        if self.findJoueur(0)[3]:
            cptJoueur += 1

            
        # Si le compteur de joueur arrive à 2, c'est que ca devient un 1v1 donc on met une musique épique.
        if cptJoueur > 2 :
            if self.main.playlist.currentIndex() != 1:
                self.main.music.stop()
                self.main.playlist.setCurrentIndex(1)
                self.main.music.play()
        if cptJoueur == 2:
            if self.main.playlist.currentIndex() != 2:
                self.main.music.stop()
                self.main.playlist.setCurrentIndex(2)
                self.main.music.play()

        # Si il ne reste qu'un seul joueur, on met une musique de victoire ^^

        if cptJoueur == 1:
            if self.main.playlist.currentIndex() != 3:
                self.main.music.stop()
                self.main.playlist.setCurrentIndex(3)
                self.main.music.play()

            # Puis, on vérifie qui est le dernier joueur en vie et on le félicite ^^

            if self.findJoueur(3)[0]:
                self.vj3 = QLabel("VICTOIRE DU JOUEUR JAUNE !", self)
                self.vj3.move(250, 450)
                self.vj3.setStyleSheet("QLabel {border-radius: 10px; color: yellow; font: bold 90px;" \
                                       "height: 485; width: 705; margin: 8px;}")
                self.vj3.show()
                jaune = False
                stop = QTimer(self)
                stop.timeout.connect(quit)
                stop.start(5000)

            elif self.findJoueur(1)[0]:
                self.vj1 = QLabel("VICTOIRE DU JOUEUR ROUGE !", self)
                self.vj1.move(250, 450)
                self.vj1.setStyleSheet("QLabel {border-radius: 10px; color: red; font: bold 90px;" \
                                       "height: 485; width: 705; margin: 8px;}")
                self.vj1.show()
                rouge = False
                stop = QTimer(self)
                stop.timeout.connect(quit)
                stop.start(5000)

            elif self.findJoueur(3)[0]:
                self.vj2 = QLabel("VICTOIRE DU JOUEUR BLEU !", self)
                self.vj2.move(250, 450)
                self.vj2.setStyleSheet("QLabel {border-radius: 10px; color: cyan; font: bold 90px;" \
                                       "height: 485; width: 705; margin: 8px;}")
                self.vj2.show()
                bleu = False
                stop = QTimer(self)
                stop.timeout.connect(quit)
                stop.start(5000)

            elif self.findJoueur(4)[0]:
                rose = False
                self.vj4 = QLabel("VICTOIRE DU JOUEUR ROSE !", self)
                self.vj4.move(250, 450)
                self.vj4.setStyleSheet("QLabel {border-radius: 10px; color: magenta; font: bold 90px;" \
                                       "height: 485; width: 705; margin: 8px;}")
                self.vj4.show()
                stop = QTimer(self)
                stop.timeout.connect(quit)
                stop.start(5000)

        # Bien évidemment, les égalités sont possibles. Elles sont donc gérées ici
        if cptJoueur == 0:
            
            if self.main.playlist.currentIndex() != 4:
                self.main.music.stop()
                self.main.playlist.setCurrentIndex(4)
                self.main.music.play()
                self.egalite = QLabel("ÉGALITÉ !", self)
                self.egalite.move(250, 450)
                self.egalite.setStyleSheet("QLabel {border-radius: 10px; color: black; font: bold 90px;" \
                                       "height: 485; width: 705; margin: 8px;}")
                self.egalite.show()
            stop = QTimer(self)
            stop.timeout.connect(quit)
            stop.start(5000)

        # Et on close la fenetre. Pas encore de retour au menu principal

    
    

    def updateScore(self):
        self.sj1.setText("Score Rouge : " + str(self.var.score_j1))
        self.sj2.setText("Score Bleu : " + str(self.var.score_j2))
        self.sj3.setText("Score Jaune : " + str(self.var.score_j3))
        self.sj4.setText("Score Rose : " + str(self.var.score_j4))


    # Et ca, c'est notre keyPressEvent

    def keyPressEvent(self, event):
        #if event.key() == Qt.Key_H:

        if event.key() == Qt.Key_A:
            if not self.findJoueur(1)[0]:
                self.Map1[1][1] = 3

        if event.key() == Qt.Key_Z:

            self.var.posJ1 = 0
            if self.var.movementJ1 == 0:
                self.var.movementJ1 = 1
            elif self.var.movementJ1 == 1:
                self.var.movementJ1 = 2
            elif self.var.movementJ1 == 2:
                self.var.movementJ1 = 3
            elif self.var.movementJ1 == 3:
                self.var.movementJ1 = 0

            if self.var.stateJ1 == "skull":
                self.mouvement.moveDown(3, 34)

            else:
                self.mouvement.moveTop(3, 34)




        elif event.key() == Qt.Key_Q:
            self.var.posJ1 = 2
            if self.var.movementJ1 == 0:
                self.var.movementJ1 = 1
            elif self.var.movementJ1 == 1:
                self.var.movementJ1 = 2
            elif self.var.movementJ1 == 2:
                self.var.movementJ1 = 3
            elif self.var.movementJ1 == 3:
                self.var.movementJ1 = 0
            if self.var.stateJ1 == "skull":
                self.mouvement.moveRight(3, 34)

            else:
                self.mouvement.moveLeft(3, 34)




        elif event.key() == Qt.Key_S:
            self.var.posJ1 = 1
            if self.var.movementJ1 == 0:
                self.var.movementJ1 = 1
            elif self.var.movementJ1 == 1:
                self.var.movementJ1 = 2
            elif self.var.movementJ1 == 2:
                self.var.movementJ1 = 3
            elif self.var.movementJ1 == 3:
                self.var.movementJ1 = 0

            if self.var.stateJ1 == "skull":
                self.mouvement.moveTop(3, 34)

            else:
                self.mouvement.moveDown(3, 34)




        elif event.key() == Qt.Key_D:
            self.var.posJ1 = 3
            if self.var.movementJ1 == 0:
                self.var.movementJ1 = 1
            elif self.var.movementJ1 == 1:
                self.var.movementJ1 = 2
            elif self.var.movementJ1 == 2:
                self.var.movementJ1 = 3
            elif self.var.movementJ1 == 3:
                self.var.movementJ1 = 0
            if self.var.stateJ1 == "skull":
                self.mouvement.moveLeft(3, 34)
            else:
                self.mouvement.moveRight(3, 34)




        elif event.key() == Qt.Key_Space:
            if self.var.bombeJ1 == "bomb":
                self.bombe.poseBombe(3, 34)
            if self.var.bombeJ1 == "pyke":
                self.bombe.posePikeBombe(3, 34)


        elif event.key() == Qt.Key_M:
            self.var.posJ2 = 3
            
            if self.timerIA2.isActive() :
                self.timerIA2.stop()
                self.var.stopIA2 = True
            if self.var.stateJ2 == "skull":
                self.mouvement.moveLeft(7, 74)
            else:
                self.mouvement.moveRight(7, 74)


        elif event.key() == Qt.Key_K:
            self.var.posJ2 = 2
        
            if self.timerIA2.isActive() :
                self.timerIA2.stop()
                self.var.stopIA2 = True
            if self.var.stateJ2 == "skull":
                self.mouvement.moveRight(7, 74)
            else:
                self.mouvement.moveLeft(7, 74)


        elif event.key() == Qt.Key_O:
            self.var.posJ2 = 0

            if self.timerIA2.isActive() :
                self.timerIA2.stop()
                self.var.stopIA2 = True
            if self.var.stateJ2 == "skull":
                self.mouvement.moveDown(7, 74)
            else:
                self.mouvement.moveTop(7, 74)


        elif event.key() == Qt.Key_L:
            self.var.posJ2 = 1

            if self.timerIA2.isActive() :
                self.timerIA2.stop()
                self.var.stopIA2 = True
            if self.var.stateJ2 == "skull":
                self.mouvement.moveTop(7, 74)
            else:
                self.mouvement.moveDown(7, 74)


        elif event.key() == Qt.Key_Shift:
            if self.timerIA2.isActive() :
                self.timerIA2.stop()
                self.var.stopIA2 = True
            self.bombe.poseBombe(7, 74)


        elif event.key() == Qt.Key_Right:
            self.var.posJ3 = 3
            if self.var.movementJ3 == 0:
                self.var.movementJ3 = 1
            elif self.var.movementJ3 == 1:
                self.var.movementJ3 = 2
            elif self.var.movementJ3 == 2:
                self.var.movementJ3 = 3
            elif self.var.movementJ3 == 3:
                self.var.movementJ3 = 0

            if self.timerIA3.isActive() :
                self.timerIA3.stop()
                self.var.stopIA3 = True
            if self.var.stateJ3 == "skull":
                self.mouvement.moveLeft(8, 84)
            else:
                self.mouvement.moveRight(8, 84)


        elif event.key() == Qt.Key_Left:
            self.var.posJ3 = 2
            if self.var.movementJ3 == 0:
                self.var.movementJ3 = 1
            elif self.var.movementJ3 == 1:
                self.var.movementJ3 = 2
            elif self.var.movementJ3 == 2:
                self.var.movementJ3 = 3
            elif self.var.movementJ3 == 3:
                self.var.movementJ3 = 0
            if self.timerIA3.isActive() :
                self.timerIA3.stop()
                self.var.stopIA3 = True
            if self.var.stateJ3 == "skull":
                self.mouvement.moveRight(8, 84)
            else:
                self.mouvement.moveLeft(8, 84)


        elif event.key() == Qt.Key_Up:
            self.var.posJ3 = 0
            if self.var.movementJ3 == 0:
                self.var.movementJ3 = 1
            elif self.var.movementJ3 == 1:
                self.var.movementJ3 = 2
            elif self.var.movementJ3 == 2:
                self.var.movementJ3 = 3
            elif self.var.movementJ3 == 3:
                self.var.movementJ3 = 0
            if self.timerIA3.isActive() :
                self.timerIA3.stop()
                self.var.stopIA3 = True
            if self.var.stateJ3 == "skull":
                self.mouvement.moveDown(8, 84)
            else:
                self.mouvement.moveTop(8, 84)


        elif event.key() == Qt.Key_Down:
            self.var.posJ3 = 1
            if self.var.movementJ3 == 0:
                self.var.movementJ3 = 1
            elif self.var.movementJ3 == 1:
                self.var.movementJ3 = 2
            elif self.var.movementJ3 == 2:
                self.var.movementJ3 = 3
            elif self.var.movementJ3 == 3:
                self.var.movementJ3 = 0
            if self.timerIA3.isActive() :
                self.timerIA3.stop()
                self.var.stopIA3 = True
            if self.var.stateJ3 == "skull":
                self.mouvement.moveTop(8, 84)
            else:
                self.mouvement.moveDown(8, 84)


        elif event.key() == Qt.Key_Control or event.key() == Qt.Key_0:
            if self.timerIA3.isActive() :
                self.timerIA3.stop()
                self.var.stopIA3 = True
            self.bombe.poseBombe(8, 84)


        elif event.key() == Qt.Key_6:
            self.var.posJ4 = 3
            if self.var.movementJ4 == 0:
                self.var.movementJ4 = 1
            elif self.var.movementJ4 == 1:
                self.var.movementJ4 = 2
            elif self.var.movementJ4 == 2:
                self.var.movementJ4 = 3
            elif self.var.movementJ4 == 3:
                self.var.movementJ4 = 0
            if self.timerIA4.isActive() :
                self.timerIA4.stop()
                self.var.stopIA4 = True
            if self.var.stateJ4 == "skull":
                self.mouvement.moveLeft(9, 94)
            else:
                self.mouvement.moveRight(9, 94)


        elif event.key() == Qt.Key_4:
            self.var.posJ4 = 2
            if self.var.movementJ4 == 0:
                self.var.movementJ4 = 1
            elif self.var.movementJ4 == 1:
                self.var.movementJ4 = 2
            elif self.var.movementJ4 == 2:
                self.var.movementJ4 = 3
            elif self.var.movementJ4 == 3:
                self.var.movementJ4 = 0
            if self.timerIA4.isActive() :
                self.timerIA4.stop()
                self.var.stopIA4 = True
            if self.var.stateJ4 == "skull":
                self.mouvement.moveRight(9, 94)
            else:
                self.mouvement.moveLeft(9, 94)


        elif event.key() == Qt.Key_8:
            self.var.posJ4 = 0
            if self.var.movementJ4 == 0:
                self.var.movementJ4 = 1
            elif self.var.movementJ4 == 1:
                self.var.movementJ4 = 2
            elif self.var.movementJ4 == 2:
                self.var.movementJ4 = 3
            elif self.var.movementJ4 == 3:
                self.var.movementJ4 = 0
            if self.timerIA4.isActive() :
                self.timerIA4.stop()
                self.var.stopIA4 = True
            if self.var.stateJ4 == "skull":
                self.mouvement.moveDown(9, 94)
            else:
                self.mouvement.moveTop(9, 94)


        elif event.key() == Qt.Key_5:
            self.var.posJ4 = 1
            if self.var.movementJ4 == 0:
                self.var.movementJ4 = 1
            elif self.var.movementJ4 == 1:
                self.var.movementJ4 = 2
            elif self.var.movementJ4 == 2:
                self.var.movementJ4 = 3
            elif self.var.movementJ4 == 3:
                self.var.movementJ4 = 0
            if self.timerIA4.isActive() :
                self.timerIA4.stop()
                self.var.stopIA4 = True
            if self.var.stateJ4 == "skull":
                self.mouvement.moveTop(9, 94)
            else:
                self.mouvement.moveDown(9, 94)


        elif event.key() == Qt.Key_Plus:
            if self.timerIA4.isActive() :
                self.timerIA4.stop()
                self.var.stopIA4 = True
            self.bombe.poseBombe(9, 94)

        elif event.key() == Qt.Key_Escape:
            self.main.menuPause()

        self.update()
