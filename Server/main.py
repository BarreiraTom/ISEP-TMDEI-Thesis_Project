#
# ONLY WORKS ON LINUX!!!!
#

import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from Motor import *


class Ui_Client(object):
    def setupUi(self, Client):
        Client.resize(600, 100)
        Client.setWindowTitle('Car Controller')
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(40)
        Client.setFont(font)

        self.kBrdInpt = QtWidgets.QCheckBox(Client)
        self.kBrdInpt.setGeometry(QtCore.QRect(0, 0, 20, 20))
        self.kBrdInpt.setText("Keyboard Input")
        self.kBrdInpt.setChecked(False)


class mywindow(QMainWindow, Ui_Client):
    def __init__(self):
        global timer
        super(mywindow, self).__init__()
        self.setupUi(self)

        self._keyboardInput = False
        self._leftWheels = self._rightWheels = 0

    def keyPressEvent(self, event):
        if self._keyboardInput:
            if not event.isAutoRepeat():
                if event.key() == Qt.Key_W:
                    self._leftWheels = 1000
                    self._rightWheels = 1000
                elif event.key() == Qt.Key_S:
                    self._leftWheels = -1000
                    self._rightWheels = -1000
                elif event.key() == Qt.Key_A:
                    self._leftWheels = -1500
                    self._rightWheels = 2000
                elif event.key() == Qt.Key_D:
                    self._leftWheels = 2000
                    self._rightWheels = -1500

            PWM.setMotorModel(self._leftWheels, self._leftWheels,
                              self._rightWheels, self._rightWheels)

    def keyReleaseEvent(self, event):
        if self._keyboardInput:
            if not event.isAutoRepeat():
                if (event.key() == Qt.Key_W
                    or event.key() == Qt.Key_S
                    or event.key() == Qt.Key_A
                        or event.key() == Qt.Key_D):
                    self._leftWheels = 0
                    self._rightWheels = 0

            PWM.setMotorModel(self._leftWheels, self._leftWheels,
                              self._rightWheels, self._rightWheels)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
