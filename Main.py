import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import *
from Solo import *
from Joueurs2 import *
from Joueurs3 import *
from Joueurs4 import *
from variable import *


class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.initWindow()
        self.playlist()
        self.stackedLayout()

    def initWindow(self):
        desktop = QDesktopWidget()
        self.setMinimumSize(desktop.screenGeometry().width(), desktop.screenGeometry().height())
        self.setMaximumSize(desktop.screenGeometry().width(), desktop.screenGeometry().height())
        self.setWindowFlags(Qt.FramelessWindowHint)

        image = QImage("Images/fond.png")
        size = image.scaled(QSize(self.frameGeometry().width(), self.frameGeometry().height()))

        palette = QPalette()
        palette.setBrush(10, QBrush(size))
        self.setPalette(palette)

        self.styleSheet = "QPushButton {background: #e4c934; border-radius: 10px; color: white; font: bold 30px; border: 1.5px " \
                                "solid black; height: 85; width: 305; margin: 8px;}"

        cursor = QCursor(QPixmap("Images/CURSOR_.png"))
        self.setCursor(cursor)
        self.setWindowIcon(QIcon("Images/Bomberman.ico"))

    def playlist(self):
        self.playlist = QMediaPlaylist()
        url1 = QUrl.fromLocalFile(os.getcwd() + "/Musiques/Bomberman.wav")
        url2 = QUrl.fromLocalFile(os.getcwd() + "/Musiques/Battle.wav")
        url3 = QUrl.fromLocalFile(os.getcwd() + "/Musiques/Boss.wav")
        url4 = QUrl.fromLocalFile(os.getcwd() + "/Musiques/win.wav")
        url5 = QUrl.fromLocalFile(os.getcwd() + "/Musiques/egalite.wav")

        self.playlist.addMedia(QMediaContent(url1))
        self.playlist.addMedia(QMediaContent(url2))
        self.playlist.addMedia(QMediaContent(url3))
        self.playlist.addMedia(QMediaContent(url4))
        self.playlist.addMedia(QMediaContent(url5))
        self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)

        self.music = QMediaPlayer()
        self.music.setPlaylist(self.playlist)

    def stackedLayout(self):
        self.stackedLayout = QStackedLayout()
        self.stackedLayout.addWidget(self.mainMenu())
        self.stackedLayout.addWidget(self.levelMenu())
        self.stackedLayout.addWidget(self.optionsMenu())
        self.stackedLayout.addWidget(self.soloMode())
        self.stackedLayout.addWidget(self.nbPlayer2Mode())
        self.stackedLayout.addWidget(self.nbPlayer3Mode())
        self.stackedLayout.addWidget(self.nbPlayer4Mode())

        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.stackedLayout)
        self.setCentralWidget(self.mainWidget)
        self.widget = QWidget()



    def onClickedMenu(self):
        self.stackedLayout.setCurrentIndex(0)

    def onClickedLevels(self):
        self.stackedLayout.setCurrentIndex(1)

    def onClickedOptions(self):
        self.stackedLayout.setCurrentIndex(2)

    def onClickedSolo(self):
        self.stackedLayout.setCurrentIndex(3)
        self.music.stop()
        self.playlist.setCurrentIndex(1)
        self.music.play()
    
    def onClicked2Joueurs(self):
        self.stackedLayout.setCurrentIndex(4)
        self.music.stop()
        self.playlist.setCurrentIndex(1)
        self.music.play()
    
    def onClicked3Joueurs(self):
        self.stackedLayout.setCurrentIndex(5)
        self.music.stop()
        self.playlist.setCurrentIndex(1)
        self.music.play()
    
    def onClicked4Joueurs(self):
        self.stackedLayout.setCurrentIndex(6)
        self.music.stop()
        self.playlist.setCurrentIndex(1)
        self.music.play()



    def mainMenu(self):
        self.widget = QWidget()
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)

        self.start = QPushButton("Jouer", clicked = self.onClickedLevels)
        self.options = QPushButton("Options", clicked = self.onClickedOptions)
        self.quit = QPushButton("Quitter", clicked = self.closeGame)

        self.layout.addWidget(self.start)
        self.layout.addWidget(self.options)
        self.layout.addWidget(self.quit)

        self.widget.setStyleSheet(self.styleSheet)
        self.widget.setLayout(self.layout)

        return self.widget

    def optionsMenu(self):
        self.playlist.setCurrentIndex(0)
        self.music.play()

        self.widget = QWidget()
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)

        self.mute = QPushButton("MUTE", clicked = self.music.setMuted)
        self.back = QPushButton("RETOUR", clicked = self.onClickedMenu)
        self.mute.setCheckable(True)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.frameGeometry()
        self.slider.setRange(0, 100)
        self.slider.setValue(50)
        self.slider.valueChanged.connect(self.music.setVolume)

        self.label = QLabel("Volume")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("background: #e4c934; border-radius: 10px; color: white; font: bold 30px; border: 1.5px " \
                                 "solid black; height: 100; width: 305; margin: 8px;")

        sliderStyleSheet = """
                QSlider::groove:horizontal {
                    border: 2px solid #A0A5B2;
                    border-radius: 2px;
                    height: 4px;
                    background: #E8E8E8;}

                QSlider::handle:horizontal {
                    background: #e4c934;
                    width: 20px;
                    border-top: 1px solid #000000;
                    border-left: 1px solid #000000;
                    border-right: 1px solid #000000;
                    border-bottom: 2px solid #000000;
                    border-radius: 2px;
                    margin: -3px 0;}
                    """

        self.slider.setFixedWidth(320)
        self.slider.setStyleSheet(sliderStyleSheet)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.slider)
        self.layout.addWidget(self.mute)
        self.layout.addWidget(self.back)

        self.widget.setStyleSheet(self.styleSheet)
        self.widget.setLayout(self.layout)

        return self.widget


    def levelMenu(self):
        self.widget = QWidget()
        self.layout = QHBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)

        self.solo = QPushButton("1 joueur", clicked = self.onClickedSolo)
        self.p2 = QPushButton("2 Joueurs", clicked = self.onClicked2Joueurs)
        self.p3 = QPushButton("3 Joueurs", clicked = self.onClicked3Joueurs)
        self.p4 = QPushButton("4 Joueurs", clicked = self.onClicked4Joueurs)
        self.back = QPushButton("Retour", clicked = self.onClickedMenu)

        self.layout.addWidget(self.solo)
        self.layout.addWidget(self.p2)
        self.layout.addWidget(self.p3)
        self.layout.addWidget(self.p4)
        self.layout.addWidget(self.back)

        self.widget.setStyleSheet(self.styleSheet)
        self.widget.setLayout(self.layout)

        return self.widget

    def soloMode(self):
        self.widget = QWidget()
        self.layout = QHBoxLayout()

        self.widget.setStyleSheet("background-image: url(Images/gazon.jpg);")

        self.level = Solo(self)
        self.layout.addWidget(self.level)
        self.widget.setLayout(self.layout)

        return self.widget
    
    def nbPlayer2Mode(self):
        self.widget = QWidget()
        self.layout = QHBoxLayout()

        self.widget.setStyleSheet("background-image: url(Images/gazon.jpg);")

        self.level = Joueurs2(self)
        self.layout.addWidget(self.level)
        self.widget.setLayout(self.layout)

        return self.widget

    def nbPlayer3Mode(self):
        self.widget = QWidget()
        self.layout = QHBoxLayout()

        self.widget.setStyleSheet("background-image: url(Images/gazon.jpg);")

        self.level = Joueurs3(self)
        self.layout.addWidget(self.level)
        self.widget.setLayout(self.layout)

        return self.widget

    def nbPlayer4Mode(self):
        self.widget = QWidget()
        self.layout = QHBoxLayout()

        self.widget.setStyleSheet("background-image: url(Images/gazon.jpg);")

        self.level = Joueurs4(self)
        self.layout.addWidget(self.level)
        self.widget.setLayout(self.layout)

        return self.widget

    def closePauseMenu(self):
        self.layout.removeWidget(self.widget)

    def closeGame(self):
        message = QMessageBox.question(self, 'Quitter', "<b> Voulez-vous quitter le jeu ? </b>", QMessageBox.Yes |
                                       QMessageBox.No, QMessageBox.Yes)

        if message == QMessageBox.Yes:
            quit()

    
    def menuPause(self):
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)
        self.continuer = QPushButton("Continuer", clicked=self.stopPause)
        self.mute = QPushButton(clicked=self.music.setMuted)
        self.quit = QPushButton("Menu Principal", clicked=self.musique1)
        self.quit.setStyleSheet("background: #e4c934; border-radius: 10px; color: white; font: bold 27px; border: 1.5px " \
                                "solid black; height: 85; width: 305; margin: 8px;")

        self.mute.setCheckable(True)
        self.layout.addWidget(self.continuer)
        self.layout.addWidget(self.mute)
        self.layout.addWidget(self.quit)
        self.mute.setStyleSheet("background: #e4c934; border-radius: 10px; color: white; font: bold 27px; border: 1.5px " \
                          "solid black; height: 85; width: 305; margin: 8px;")

        self.continuer.setStyleSheet("background: #e4c934; border-radius: 10px; color: white; font: bold 27px; border: 1.5px " \
                          "solid black; height: 85; width: 305; margin: 8px;")
    
        icon = QIcon("Images/mute.png")
        self.mute.setIcon(icon)
        self.mute.setIconSize(QSize(90, 90))
        self.widget.setLayout(self.layout)
        self.widget.setStyleSheet("background: transparent")
        self.widget.show()

        
    def stopPause(self):
        self.widget.close()
  

    def musique1(self):
        message = QMessageBox.question(self, 'Menu', "<b> Voulez-vous retourner sur le menu ? </b>", QMessageBox.Yes |
                                       QMessageBox.No, QMessageBox.Yes)

        if message == QMessageBox.Yes:
            self.music.stop()
            self.playlist.setCurrentIndex(0)
            self.music.play()
            self.onClickedMenu()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Main()
    win.show()
    sys.exit(app.exec_())
