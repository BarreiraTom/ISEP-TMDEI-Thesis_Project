#
# ONLY WORKS ON LINUX!!!!
#

from re import U
import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Ui_Client(object):
    def setupUi(self, Client):
        Client.resize(600, 100)
        Client.setWindowTitle('Keyboard Window Test')
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(40)
        Client.setFont(font)

        self.W = QtWidgets.QLabel(Client)
        self.W.setGeometry(QtCore.QRect(0, 0, 100, 100))
        self.W.setText("W")
        self.W.setVisible(False)

        self.A = QtWidgets.QLabel(Client)
        self.A.setGeometry(QtCore.QRect(100, 0, 100, 100))
        self.A.setText("A")
        self.A.setVisible(False)

        self.S = QtWidgets.QLabel(Client)
        self.S.setGeometry(QtCore.QRect(200, 0, 100, 100))
        self.S.setText("S")
        self.S.setVisible(False)

        self.D = QtWidgets.QLabel(Client)
        self.D.setGeometry(QtCore.QRect(300, 0, 100, 100))
        self.D.setText("D")
        self.D.setVisible(False)


class mywindow(QMainWindow, Ui_Client):
    def __init__(self):
        global timer
        super(mywindow, self).__init__()
        self.setupUi(self)

        self.Key_W = False
        self.Key_A = False
        self.Key_S = False
        self.Key_D = False

    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            pass
        else :
            if event.key() == Qt.Key_W:
                print('W')
                self.Key_W = True
            elif event.key() == Qt.Key_S:
                print('S')
                self.Key_S = True
            elif event.key() == Qt.Key_A:
                print('A')
                self.Key_A = True
            elif event.key() == Qt.Key_D:
                print('D')
                self.Key_D = True

        self.W.setVisible(self.Key_W)
        self.A.setVisible(self.Key_A)
        self.S.setVisible(self.Key_S)
        self.D.setVisible(self.Key_D)

    def keyReleaseEvent(self, event):

        if(event.key() == Qt.Key_W):
            time.sleep(0.05)
            if(event.key() == Qt.Key_W):
                if not(event.isAutoRepeat()) and self.Key_W == True:
                    print('-W')
                    self.Key_W = False
        elif(event.key() == Qt.Key_A):
            if not(event.isAutoRepeat()) and self.Key_A == True:
                print('-A')
                self.Key_A = False
        elif(event.key() == Qt.Key_S):
            if not(event.isAutoRepeat()) and self.Key_S == True:
                print('-S')
                self.Key_S = False
        elif(event.key() == Qt.Key_D):
            if not(event.isAutoRepeat()) and self.Key_D == True:
                print('-D')
                self.Key_D = False

        self.W.setVisible(self.Key_W)
        self.A.setVisible(self.Key_A)
        self.S.setVisible(self.Key_S)
        self.D.setVisible(self.Key_D)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
