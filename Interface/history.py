import argparse
import os
import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap, QFont

data = {
    1: "Король говорит главному герою, что он узнал от советника о секретном сокровище, спрятанном в тёмном лесу, окружающем королевство. Герой соглашается найти его любой ценой. Король уходит, и советник предупреждает главного героя о том, что в лесу есть огромная пещера, в которой живёт дракон и охраняет то самое сокровище => дракона нужно убить. У главного героя внутренний конфликт – желание заслужить признание короля, но нежелание погибнуть. Герой решил согласится и должен поставить галочку в документе.",
    2: "Главный герой отправился в путь. Наконец, он добрался до леса. Зайдя в густую чащу, он восхищается окружающей его волшебной красотой. Он долго шёл, пока не наткнулся на торговца. Герой пытается заговорить с ним, и спрашивает о драконе и сокровищах. Торговец не отвечает. Тогда герой объясняет ему с помощью жестов, что он ищет. Торговец направляет его в сторону поляны и желает удачи.",
    3: "Главный герой попадает на широкую поляну. В самом центре поляны он видит маленькую хижину, и направляется к ней. Рядом с хижиной он встречает волшебника, и просит его о помощи. Тот злится и отказывает в просьбе. Главный герой предлагает договориться. Волшебник соглашается, и даёт бумажку с заклинанием. Если герой сможет его произнести, то появится тропинка, ведущая к пещере дракона. Если не сможет, то он навсегда останется служить волшебнику.",
    4: "Лес становится всё мрачнее и темнее. Главный герой доходит до пещеры, и появляется огромный дракон. Сначала он громко рычит, но затем успокаивается, наклоняется к главному герою и тихо смотрит на него.",
}
data_pic = {
    1: 'pic\menu_pic.png',
    2: 'pic\menu_pic.png',
    3: 'pic\menu_pic.png',
    4: 'pic\menu_pic.png',
}


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1115, 900)

        parser = argparse.ArgumentParser()
        parser.add_argument('--index', type=str)
        args = parser.parse_args()
        self.index = args.index

        text = data[int(self.index)]
        pic_name = data_pic[int(self.index)]

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.exit_l = QtWidgets.QLabel(self.centralwidget)
        self.exit_l.setGeometry(QtCore.QRect(890, 640, 186, 60))
        self.exit_l.setText("")
        self.exit_l.setObjectName("exit_l")
        self.exit_l.setPixmap(QPixmap('pic/exit.png'))
        self.exit_l.setStyleSheet('background-color: rgba(255, 255, 255, 0);')

        self.next_l = QtWidgets.QLabel(self.centralwidget)
        self.next_l.setGeometry(QtCore.QRect(890, 710, 186, 60))
        self.next_l.setText("")
        self.next_l.setObjectName("next_l")
        self.next_l.setPixmap(QPixmap('pic//next.png'))
        self.next_l.setStyleSheet('background-color: rgba(255, 255, 255, 0);')

        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(890, 640, 186, 60))
        self.exit.setText("")
        self.exit.setObjectName("exit")
        self.exit.setStyleSheet('background-color: rgba(255, 255, 255, 0);')

        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(890, 710, 186, 60))
        self.next.setText("")
        self.next.setObjectName("next")
        self.next.clicked.connect(self.next_level)
        self.next.setStyleSheet('background-color: rgba(255, 255, 255, 0);')

        self.pic = QtWidgets.QLabel(self.centralwidget)
        self.pic.setGeometry(QtCore.QRect(10, 10, 1095, 615))
        self.pic.setText("")
        self.pic.setObjectName("pic")
        self.pic.setPixmap(QPixmap(pic_name))

        self.text = QtWidgets.QLabel(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(10, 630, 861, 355))
        self.text.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.text.setWordWrap(True)
        self.text.setFont(QFont('Arial Rounded MT', 15, italic=True))
        self.text.setText(text)
        self.text.setObjectName("text")
        self.text.setStyleSheet('color: rgb(128, 57, 57);'
                                'font-weight: bold;')

        self.setStyleSheet("background-color: #cc7b63;")

        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def next_level(self):
        self.close()
        os.system(f'python main.py --index {self.index}')


def start():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


if __name__ == "__main__":
    start()
