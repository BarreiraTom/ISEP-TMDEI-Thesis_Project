#
# ONLY WORKS ON LINUX!!!!
#
import sys
from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets
from pydispatch import Dispatcher

# Remote Controlled Car
try:
    import Motor
    import ADC
except Exception as e:
    print("Car module import failed")
    print(e)

# Headset
try:
    import LiveAdvance
except Exception as e:
    print("Emotiv Headset import failed")
    print(e)


# General methods
def callMovement(_leftWheels, _rightWheels):
    try:
        Motor.PWM.setMotorModel(-_leftWheels, -_leftWheels,
                                -_rightWheels, -_rightWheels)
    except Exception:
        print('Motor not reached')

class emotivHandler(Thread, Dispatcher):

    _events_ = ['brainData']

    def run(self):
        try:
            print('Headset handler Loading...')

            try:
                clt = open('./cortexClient.txt', 'r').read()

                self.c_client_id = clt.split('\n')[0]
                self.c_client_secret = clt.split('\n')[1]
                self.c_profile_name = 'Tomas'
            except Exception as e:
                raise ValueError(
                    '\nThere is missing information about the client data. \nPlease insert the client id and client secret in a file named "cortexClient.txt" respectively in separate lines. Then restart the app')

            self.l = LiveAdvance(self.c_client_id, self.c_client_secret)
            self.l.bind(brainData=self.on_new_brain_data)
            self.l.start(self.c_profile_name)

        except Exception as e:
            print('Headset handler Error')
            print(e)

    def on_new_brain_data(self, *args, **kwargs):
        _brainValue = kwargs.get('data')
        self.emit('brainData', data=_brainValue)


class getBattery(Thread, Dispatcher):

    _events_ = ['batData']

    def run(self):
        try:
            _adc = ADC.Adc()
            ADC_Power = _adc.recvADC(2)*3
            self._batValue = str(int((float(ADC_Power)-7)/1.40*100))+'%'
            self.emit('batData', data=self._batValue)
        except Exception as e:
            print('Battery not reached')
            print(e)
            self._batValue = 'N/A'
            self.emit('batData', data=self._batValue)


# MAIN Class
class Ui_Client(object):
    def setupUi(self, Client):
        Client.resize(600, 100)
        Client.setWindowTitle('Car Controller')
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        Client.setFont(font)

        # self._battery = Thread(target=getBattery)
        # self._battery.start()
        self._battery = getBattery()
        self._battery.bind(batData=self.on_bat_change)
        self._battery.start()
        self._batValue = '---'
        self._keyboardInput = False
        self._brainInput = False
        self._brainHandler = emotivHandler()
        self._brainHandler.bind(brainData=self.on_new_brain_data)
        self._brainHandler.start()
        self._brainValue = '---'


        self.kBrdInpt = QtWidgets.QCheckBox(Client)
        self.kBrdInpt.setGeometry(QtCore.QRect(20, 0, 150, 25))
        self.kBrdInpt.setText("Keyboard Input")
        self.kBrdInpt.setChecked(False)
        self.kBrdInpt.stateChanged.connect(
            lambda: self.buttonHandler(self.kBrdInpt))

        self.brainInpt = QtWidgets.QCheckBox(Client)
        self.brainInpt.setGeometry(QtCore.QRect(170, 0, 150, 25))
        self.brainInpt.setText("Brainwave Input")
        self.brainInpt.setChecked(False)
        self.brainInpt.stateChanged.connect(
            lambda: self.buttonHandler(self.brainInpt))

        self.battery = QtWidgets.QLabel(Client)
        self.battery.setGeometry(QtCore.QRect(20, 25, 100, 25))
        self.battery.setText('Battery: ' + str(self._batValue))

        self.brnShow = QtWidgets.QLabel(Client)
        self.brnShow.setGeometry(QtCore.QRect(20, 45, 500, 25))
        self.brnShow.setText('TEST: ' + str(self._brainValue))

    def on_bat_change(self, *args, **kwargs):
        self._batValue = kwargs.get('data')
        self.battery.setText('Battery: ' + str(self._batValue))

    def on_new_brain_data(self, *args, **kwargs):
        self._brainValue = kwargs.get('data')
        self.brnShow.setText('Direction: ' + str(self._brainValue['action']))

        if self._brainValue['action'] == 'push':
            self._leftWheels = 1000
            self._rightWheels = 1000
        elif self._brainValue['action'] == 'pull':
            self._leftWheels = -1000
            self._rightWheels = -1000
        elif self._brainValue['action'] == 'left':
            self._leftWheels = -1500
            self._rightWheels = 2000
        elif self._brainValue['action'] == 'right':
            self._leftWheels = 2000
            self._rightWheels = -1500

        callMovement(self._leftWheels, self._rightWheels)

    def buttonHandler(self, btn):
        print(btn.text() + " button is being handled")

        if btn.text() == "Keyboard Input":
            if btn.isChecked():
                print(btn.text() + " is selected")
                self._keyboardInput = True
                self._brainInput = False
                self.brainInpt.setChecked(False)
                if self._brainHandler.is_alive:
                    print('yep')
            else:
                print(btn.text() + " is deselected")
                self._keyboardInput = False

        if btn.text() == "Brainwave Input":
            if btn.isChecked():
                print(btn.text() + " is selected")
                self._brainInput = True
                self._keyboardInput = False
                self.kBrdInpt.setChecked(False)
                if self._brainHandler.is_alive:
                    print('yep')
            else:
                print(btn.text() + " is deselected")
                self._brainInput = False


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
