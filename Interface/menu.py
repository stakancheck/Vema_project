import os
import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from PyQt5.QtGui import QPixmap


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1280, 718)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1280, 718))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.setPixmap(QPixmap('pic/menu_pic.png'))

        self.exit_l = QLabel(self.centralwidget)
        self.exit_l.setGeometry(QtCore.QRect(220, 640, 186, 60))
        self.exit_l.setText("")
        self.exit_l.setObjectName("exit")
        self.exit_l.setPixmap(QPixmap('pic/exit.png'))
        self.start_l = QLabel(self.centralwidget)
        self.start_l.setGeometry(QtCore.QRect(20, 640, 186, 60))
        self.start_l.setText("")
        self.start_l.setObjectName("start")
        self.start_l.setPixmap(QPixmap('pic/start.png'))
        self.start_l.setStyleSheet("background-color: red;")

        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(220, 640, 186, 60))
        self.exit.setText("")
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(self.close_w)
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(20, 640, 186, 60))
        self.start.setText("")
        self.start.setObjectName("start")
        self.start.clicked.connect(self.game_start)
        self.exit.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.start.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def game_start(self):
        self.close()
        os.system("python history.py --index 1")

    def close_w(self):
        sys.exit()


def start():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


if __name__ == "__main__":
    start()
