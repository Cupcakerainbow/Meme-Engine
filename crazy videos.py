from PyQt4 import QtGui, QtCore
from PyQt4.phonon import Phonon
import os
class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.media = Phonon.MediaObject(self)
        # self.media.stateChanged.connect(self.handleStateChanged)
        self.video = Phonon.VideoWidget(self)
        self.video.setMinimumSize(400, 400)
        self.audio = Phonon.AudioOutput(Phonon.VideoCategory, self)
        Phonon.createPath(self.media, self.video)
        print(help(Phonon.createPath(self.media, self.audio)))
        self.btn_pepe = QtGui.QPushButton('Pepe',self)
        self.btn_pepe.clicked.connect(self.pepe)
        self.button = QtGui.QPushButton('Thomas', self)
        self.button.clicked.connect(self.thomas)
        self.btn_surreal = QtGui.QPushButton('Surreal Guy',self)
        self.btn_surreal.clicked.connect(self.surreal)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.video, 1)
        layout.addWidget(self.button)
        layout.addWidget(self.btn_pepe)
        layout.addWidget(self.btn_surreal)
    def thomas(self):
        if self.media.state() == Phonon.PlayingState:
            self.media.stop()
        else:
            self.media.setCurrentSource(Phonon.MediaSource(
                './thomas.avi'))
            self.media.play()
    def surreal(self):
        if self.media.state() == Phonon.PlayingState:
            self.media.stop()
        else:
            self.media.setCurrentSource(Phonon.MediaSource(
                './Surreal.avi'))
            self.media.play()

    def pepe(self):
        if self.media.state() == Phonon.PlayingState:
            self.media.stop()
        else:
            self.media.setCurrentSource(Phonon.MediaSource(
                'pepe.avi'))
            self.media.play()

    def handleButton(self):
        if self.media.state() == Phonon.PlayingState:
            self.media.stop()
        else:
            path = QtGui.QFileDialog.getOpenFileName(self, self.button.text())
            if path:
                print(path)
                self.media.setCurrentSource(Phonon.MediaSource('C:/Users/Cupcake Rainbow/Videos/avatar/Avatar - the last Airbender - Season 1 Complete - NXOR/S01E01 - S01E02 Avatar - The Last Airbender 101 102.avi'))
                self.media.play()



if __name__ == '__main__':

    import sys

    print(os.curdir+'xxx')
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('Meme Engine')
    window = Window()
    window.show()


    app.exec_()
