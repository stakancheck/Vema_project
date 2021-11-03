 # -*- coding: utf8 -*-

import argparse
import os
import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap, QFont

data = {
    1: "Жил был Робин Найс. Однажды король позвал его и попросил найти волшебное сокровище, спрятанное в лесу. Он рассказал о страшном драконе, который охраняет это сокровище. Робин испугался, но очень хотел заслужить признание короля. Он должен подписать документ о согласии выполнить такое опасное поручение.",
    2: "Робин отправился в путь. Наконец, он добрался до леса. Зайдя в густую чащу, он восхитился окружающей его волшебной красотой. Он долго шёл, пока не наткнулся на торговца. Он попытался заговорить с ним, и спросил о драконе и сокровищах. Торговец не ответил. Тогда Робин решил объяснить ему с помощью жестов, что он ищет. Торговец направил его в сторону поляны и пожелал удачи.",
    3: "Робин попал на широкую поляну. В самом центре поляны он увидел маленькую хижину, и направился к ней. Рядом с хижиной он встретил волшебника, и попросил его о помощи. Волшебник разозлился и отказал в просьбе, сказав оставить пещеру с драконом в покое. Робин решил предложить заключить сделку. Волшебник согласился, и дал бумажку с заклинанием. Если Робин сможет его произнести, то появится тропинка, ведущая к пещере дракона. Если не сможет, то он навсегда останется служить волшебнику.",
    4: "Лес становится всё мрачнее и темнее. Робин Найс доходит до пещеры, и внезапно появляется огромный дракон. Он громко рычит, но затем успокаивается. Он тихо смотрит на Робина.",
    5: "Робину становиться жалко дракона. Он смотрит на него и улыбается и кладёт меч на землю. Дракон превращается в маленького мальчика. Оказывается, это хозяин леса, который защищает его. Недавно люди узнали о сокровище, и стали охотиться на дракона, чтобы заполучить желаемое. Мальчик видит, что Робин Найс – хороший человек, способный преодолеть множество препятствий и дойти до своей цели. В награду он отдаёт ему сокровище – свой волшебный меч. Робин забирает его, прощается с мальчиком и уходит из леса.",
}

data_pic = {
    1: 'pic\menu_pic.png',
    2: 'pic\seller.png',
    3: 'pic\mage.png',
    4: 'pic\dragon.png',
    5: 'pic\\boy.png'
}


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1115, 900)

        parser = argparse.ArgumentParser()
        parser.add_argument('--index', type=str)
        args = parser.parse_args()
        self.index = args.index
        print(self.index)

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

        if self.index != '5':
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

        if self.index != '5':
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
        self.exit.clicked.connect(self.close_w)

        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def next_level(self):
        self.close()
        os.system(f'python main.py --index {self.index}')

    def close_w(self):
        sys.exit()


def start():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


if __name__ == "__main__":
    start()
