#
# ONLY WORKS ON LINUX!!!!
#

import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtCore import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *

try:
    import Motor
except Exception:
    pass

# General methods


def callMovement(_leftWheels, _rightWheels):
    try:
        Motor.PWM.setMotorModel(_leftWheels, _leftWheels,
                                _rightWheels, _rightWheels)
    except Exception:
        print('Motor not reached')


class Ui_Client(object):
    def setupUi(self, Client):
        Client.resize(600, 100)
        Client.setWindowTitle('Car Controller')
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        Client.setFont(font)

        self._keyboardInput = False

        self.kBrdInpt = QtWidgets.QCheckBox(Client)
        self.kBrdInpt.setGeometry(QtCore.QRect(0, 0, 200, 25))
        self.kBrdInpt.setText("Keyboard Input")
        self.kBrdInpt.setChecked(False)
        self.kBrdInpt.stateChanged.connect(lambda:self.buttonHandler(self.kBrdInpt))

    def buttonHandler(self, btn):
        print(btn.text() + " button is being handled")

        if btn.text() == "Keyboard Input":
            if btn.isChecked():
                print(btn.text() + " is selected")
                self._keyboardInput = True
            else:
                print(btn.text() + " is deselected")
                self._keyboardInput = False
				

class mywindow(QtWidgets.QMainWindow, Ui_Client):
    def __init__(self):
        global timer
        super(mywindow, self).__init__()
        self.setupUi(self)

        self._leftWheels = self._rightWheels = 0

    def keyPressEvent(self, event):
        if self._keyboardInput:
            if not event.isAutoRepeat():
                if event.key() == QtCore.Qt.Key_W:
                    self._leftWheels = 1000
                    self._rightWheels = 1000
                elif event.key() == QtCore.Qt.Key_S:
                    self._leftWheels = -1000
                    self._rightWheels = -1000
                elif event.key() == QtCore.Qt.Key_A:
                    self._leftWheels = -1500
                    self._rightWheels = 2000
                elif event.key() == QtCore.Qt.Key_D:
                    self._leftWheels = 2000
                    self._rightWheels = -1500

            callMovement(self._leftWheels, self._rightWheels)

    def keyReleaseEvent(self, event):
        if self._keyboardInput:
            if not event.isAutoRepeat():
                if (event.key() == QtCore.Qt.Key_W
                    or event.key() == QtCore.Qt.Key_S
                    or event.key() == QtCore.Qt.Key_A
                        or event.key() == QtCore.Qt.Key_D):
                    self._leftWheels = 0
                    self._rightWheels = 0

            callMovement(self._leftWheels, self._rightWheels)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
