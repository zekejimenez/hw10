import sys
import RPi.GPIO as GPIO
from PyQt5.QtWidgets import *
# from PyQt5.uic import loadUi

from hw10_ui import *

led = 18
button = 17
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.out,initial=GPIO.LOW)

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)

        def my_callback():
            if GPIO.read(button) == 0:
                self.radioButton.nextCheckState()
            else:
                pass

        GPIO.add_event_detect(button, GPIO.RISING)
        GPIO.add_event_detect(button, GPIO.FALLING)
        GPIO.add_event_callback(button, my_callback)

    def connectsignalslots(self):
        self.pushButton.clicked.connect(lambda: self.switch_LED())
        

    def switch_LED(self):
        if GPIO.read(led) == 0:
            GPIO.output(led,GPIO.HIGH)
        else:
            GPIO.output(led,GPIO.LOW)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())