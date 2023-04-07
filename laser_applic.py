from PyQt5 import QtWidgets
from PyQt5.QtCore import QTime, QTimer
import os.path
import sys
import laser_gui
import laser_functions


class App(QtWidgets.QMainWindow, laser_gui.Ui_MainWindow):
    def __init__(self):

        super().__init__()
        self.setupUi(self)

        self.timer = QTimer()
        self.timer.timeout.connect(self.lcd_number)

        self.server_address = ('192.168.10.110', 4001)

        #self.ArmButton.clicked.connect(self.Arm_laser)
        self.ArmButton.clicked.connect(self.count_start)
        self.DisarmButton.clicked.connect(self.Arm_laser)



    def Arm_laser(self):
        laser_functions.arm(self.server_address)

    def Disarm_laser(self):
        laser_functions.disarm(self.server_address)


    def count_start(self):
        self.time2 = 0
        laser_functions.test()
        self.timer.start(1000)

    def lcd_number(self):

        self.time2 += 1
        self.Clock.setDigitCount(2)
        self.Clock.display('%d' %self.time2)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()