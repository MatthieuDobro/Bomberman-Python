import sys
from math import *
from PyQt5.QtGui import *

class sprite() :
    def __init__(self) :
        super(sprite, self).__init__()
        self.spriteJ3 = [[QPixmap("Images/haut1.png").copy(0, 138, 52, 65).scaled(50, 50), QPixmap("Images/haut2.png").copy(0, 138, 52, 65).scaled(50, 50),
                            QPixmap("Images/haut1.png").copy(0, 138, 52, 65).scaled(50, 50), QPixmap("Images/haut3.png").copy(0, 138, 52, 65).scaled(50, 50)],
                            [QPixmap("Images/bas1.png").copy(0, 138, 52, 65).scaled(50, 50), QPixmap("Images/bas2.png").copy(0, 138, 52, 65).scaled(50, 50),
                            QPixmap("Images/bas1.png").copy(0, 138, 52, 65).scaled(50, 50), QPixmap("Images/bas3.png").copy(0, 138, 52, 65).scaled(50, 50)],
                            [QPixmap("Images/gauche1.png").copy(0, 138, 52, 65).scaled(50, 50), QPixmap("Images/gauche2.png").copy(0, 138, 52, 65).scaled(50, 50),
                            QPixmap("Images/gauche1.png").copy(0, 138, 52, 65).scaled(50, 50), QPixmap("Images/gauche3.png").copy(0, 138, 52, 65).scaled(50, 50)],
                            [QPixmap("Images/droite1.png").copy(0, 138, 52, 65).scaled(50, 50), QPixmap("Images/droite2.png").copy(0, 138, 52, 65).scaled(50, 50),
                            QPixmap("Images/droite1.png").copy(0, 138, 52, 65).scaled(50, 50), QPixmap("Images/droite3.png").copy(0, 138, 52, 65).scaled(50, 50)]]

        self.spriteJ1 = [[QPixmap("Images/erenHaut1.png").copy(0, 138, 52, 65).scaled(50, 50), QPixmap("Images/erenHaut2.png").copy(0, 138, 52, 65).scaled(50, 50),
                            QPixmap("Images/erenHaut1.png").copy(0, 138, 52, 65).scaled(50, 50), QPixmap("Images/erenHaut3.png").copy(0, 138, 52, 65).scaled(50, 50)],
                            [QPixmap("Images/erenBas1.png").copy(0, 138, 52, 65).scaled(50, 50), QPixmap("Images/erenBas2.png").copy(0, 138, 52, 65).scaled(50, 50),
                            QPixmap("Images/erenBas1.png").copy(0, 138, 52, 65).scaled(50, 50), QPixmap("Images/erenBas3.png").copy(0, 138, 52, 65).scaled(50, 50)],
                            [QPixmap("Images/erenGauche1.png").copy(0, 138, 52, 65).scaled(50, 50), QPixmap("Images/erenGauche2.png").copy(0, 138, 52, 65).scaled(50, 50),
                            QPixmap("Images/erenGauche1.png").copy(0, 138, 52, 65).scaled(50, 50), QPixmap("Images/erenGauche3.png").copy(0, 138, 52, 65).scaled(50, 50)],
                            [QPixmap("Images/erenDroite1.png").copy(0, 138, 52, 65).scaled(50, 50), QPixmap("Images/erenDroite2.png").copy(0, 138, 52, 65).scaled(50, 50),
                            QPixmap("Images/erenDroite1.png").copy(0, 138, 52, 65).scaled(50, 50), QPixmap("Images/erenDroite3.png").copy(0, 138, 52, 65).scaled(50, 50)]]
        
        self.spriteJ2 = [QPixmap("Images/dk_haut.png").copy(0, 138, 52, 65).scaled(50, 50), QPixmap("Images/dk_bas.png").copy(0, 138, 52, 65).scaled(50, 50),
                            QPixmap("Images/dk_gauche.png").copy(0, 138, 52, 65).scaled(50, 50), QPixmap("Images/dk_droite.png").copy(0, 138, 52, 65).scaled(50, 50)]


        self.spriteJ4 = [[QPixmap("Images/trumpHaut1.png").copy(0, 138, 52, 65).scaled(50, 50), QPixmap("Images/trumpHaut2.png").copy(0, 138, 52, 65).scaled(50, 50),
                            QPixmap("Images/trumpHaut1.png").copy(0, 138, 52, 65).scaled(50, 50), QPixmap("Images/trumpHaut3.png").copy(0, 138, 52, 65).scaled(50, 50)],
                            [QPixmap("Images/trumpBas1.png").copy(0, 138, 52, 65).scaled(50, 50), QPixmap("Images/trumpBas2.png").copy(0, 138, 52, 65).scaled(50, 50),
                            QPixmap("Images/trumpBas1.png").copy(0, 138, 52, 65).scaled(50, 50), QPixmap("Images/trumpBas3.png").copy(0, 138, 52, 65).scaled(50, 50)],
                            [QPixmap("Images/trumpGauche1.png").copy(0, 138, 52, 65).scaled(50, 50), QPixmap("Images/trumpGauche2.png").copy(0, 138, 52, 65).scaled(50, 50),
                            QPixmap("Images/trumpGauche1.png").copy(0, 138, 52, 65).scaled(50, 50), QPixmap("Images/trumpGauche3.png").copy(0, 138, 52, 65).scaled(50, 50)],
                            [QPixmap("Images/trumpDroite1.png").copy(0, 138, 52, 65).scaled(50, 50), QPixmap("Images/trumpDroite2.png").copy(0, 138, 52, 65).scaled(50, 50),
                            QPixmap("Images/trumpDroite1.png").copy(0, 138, 52, 65).scaled(50, 50), QPixmap("Images/trumpDroite3.png").copy(0, 138, 52, 65).scaled(50, 50)]]
        
        self.texture = {
                    'bombe': QPixmap("Images/bombe.png").copy(0, 138, 52, 65).scaled(50, 50),
                    'brique': QPixmap("Images/block.png").copy(0, 138, 52, 65).scaled(50, 50),
                    'pierre': QPixmap("Images/pierre.png").copy(0, 138, 52, 65).scaled(50, 50),
                    'erenBomb': QPixmap("Images/erenBomb.png").copy(0, 138, 52, 65).scaled(50, 50),
                    'trumpBomb': QPixmap("Images/trumpBomb.png").copy(0, 138, 52, 65).scaled(50, 50),
                    'dkBomb': QPixmap("Images/dkBomb.png").copy(0, 138, 52, 65).scaled(50, 50),
                    'bomberBomb': QPixmap("Images/bomberBomb.png").copy(0, 138, 52, 65).scaled(50, 50),
                    'fire': QPixmap("Images/fire.png").copy(0, 138, 52, 65).scaled(50, 50),
                    'bomb': QPixmap("Images/bomb.png").copy(0, 138, 52, 65).scaled(50, 50),
                    'pyke': QPixmap("Images/pyke.png").copy(0, 138, 52, 65).scaled(50, 50),
                    'firedown': QPixmap("Images/firedown.png").copy(0, 138, 52, 65).scaled(50, 50),
                    'skull': QPixmap("Images/skull.png").copy(0, 138, 52, 65).scaled(50, 50),
                    'bombDown': QPixmap("Images/bombDown.png").copy(0, 138, 52, 65).scaled(50, 50),
                    'key': QPixmap("Images/key.png").copy(0, 138, 52, 65).scaled(50, 50),
                    'door': QPixmap("Images/door.png").copy(0, 138, 52, 65).scaled(50, 50),
                    

                }