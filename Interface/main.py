import argparse
import os
import cv2
import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap, QFont

CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480

data = {
    1: 'ЗАДАНИЕ НОМЕР 1',
    2: 'ЗАДАНИЕ НОМЕР 2',
    3: 'ЗАДАНИЕ НОМЕР 3',
    4: 'ЗАДАНИЕ НОМЕР 4',
}

data_pic = {
    1: 'pic\menu_pic.png',
    2: 'pic\menu_pic.png',
    3: 'pic\menu_pic.png',
    4: 'pic\menu_pic.png',
}


class Thread(QThread):
    changePixmap = pyqtSignal(QImage)

    def run(self):
        if mode == 0:
            cap = cv2.VideoCapture(0)
            while True:
                ret, frame = cap.read()
                if ret:
                    rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    h, w, ch = rgbImage.shape
                    bytesPerLine = ch * w
                    convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                    p = convertToQtFormat.scaled(CAMERA_WIDTH, CAMERA_HEIGHT, Qt.KeepAspectRatio)
                    self.changePixmap.emit(p)


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Video'
        self.left = 100
        self.top = 100
        self.width = CAMERA_WIDTH
        self.height = CAMERA_HEIGHT
        self.setFixedSize(1340, 700)

        parser = argparse.ArgumentParser()
        parser.add_argument('--index', type=str)
        args = parser.parse_args()
        self.index = args.index

        text = data[int(args.index)]
        pic_name = data_pic[int(args.index)]

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.textEdit = QtWidgets.QLabel(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 1340, 110))
        self.textEdit.setObjectName("textEdit")

        self.exit_l = QtWidgets.QLabel(self.centralwidget)
        self.exit_l.setGeometry(QtCore.QRect(220, 620, 186, 60))
        self.exit_l.setText("")
        self.exit_l.setObjectName("exit_l")
        self.exit_l.setPixmap(QPixmap('pic/exit.png'))

        self.menu_l = QtWidgets.QLabel(self.centralwidget)
        self.menu_l.setGeometry(QtCore.QRect(20, 620, 186, 60))
        self.menu_l.setText("")
        self.menu_l.setObjectName("menu_l")
        self.menu_l.setPixmap(QPixmap('pic/menu.png'))

        self.next_l = QtWidgets.QLabel(self.centralwidget)
        self.next_l.setGeometry(QtCore.QRect(420, 620, 186, 60))
        self.next_l.setText("")
        self.next_l.setObjectName("next_l")
        self.next_l.setPixmap(QPixmap('pic/next.png'))

        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(220, 620, 186, 60))
        self.exit.setText("")
        self.exit.setObjectName("exit")

        self.menu = QtWidgets.QPushButton(self.centralwidget)
        self.menu.setGeometry(QtCore.QRect(20, 620, 186, 60))
        self.menu.setText("")
        self.menu.setObjectName("menu")

        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(420, 620, 186, 60))
        self.next.setText("")
        self.next.setObjectName("next")

        self.exercise = QtWidgets.QLabel(self.centralwidget)
        self.exercise.setGeometry(QtCore.QRect(20, 120, 640, 480))
        self.exercise.setText("")
        self.exercise.setObjectName("exercise")
        self.exercise.setPixmap(QPixmap(pic_name))

        self.camera = QtWidgets.QLabel(self.centralwidget)
        self.camera.setGeometry(QtCore.QRect(680, 120, 640, 480))
        self.camera.setText("")
        self.camera.setObjectName("camera")

        self.menu.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.setStyleSheet("background-color: #cc7b63;")
        self.exit.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.next.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        self.textEdit.setText(text)
        self.textEdit.setFont(QFont('Arial', 30))
        self.textEdit.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.textEdit.setStyleSheet("background-color: #cc7b63;"
                                    "border: 10px solid rgb(128, 57, 57);"
                                    "color: rgb(128, 57, 57);")

        self.exercise.setStyleSheet("border: 5px solid rgb(128, 57, 57);")
        self.camera.setStyleSheet("border: 5px solid rgb(128, 57, 57);")

        self.exit.clicked.connect(self.close_w)
        self.menu.clicked.connect(self.menu_start)
        self.next.clicked.connect(self.next_level)
        self.initUI()
        QtCore.QMetaObject.connectSlotsByName(self)

    def next_level(self):
        self.close()
        os.system(f"python history.py --index {str(int(self.index) + 1)}")

    def menu_start(self):
        self.close()
        os.system("python menu.py")

    def close_w(self):
        sys.exit()

    @pyqtSlot(QImage)
    def setImage(self, image):
        self.camera.setPixmap(QPixmap.fromImage(image))

    def initUI(self):
        # self.camera_pic = QLabel(self)
        self.camera.resize(640, 480)
        # self.camera_pic.move(300, 300)

        th = Thread(self)
        th.changePixmap.connect(self.setImage)
        th.start()
        self.show()


def start():
    app = QApplication(sys.argv)
    global mode
    mode = 0
    ex = App()
    sys.exit(app.exec_())


if __name__ == "__main__":
    start()
