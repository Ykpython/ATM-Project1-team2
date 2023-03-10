# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\yunus\OneDrive\Desktop\atmproject\deneme\balance.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
from PyQt5 import QtCore, QtGui, QtWidgets
__location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))


class Ui_balanceScreen(object):
    def setupUi(self, balanceScreen):
        balanceScreen.setObjectName("balanceScreen")
        balanceScreen.resize(400, 400)
        balanceScreen.setStyleSheet("background-color: rgb(102, 102, 102);")
        self.centralwidget = QtWidgets.QWidget(balanceScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.check_button = QtWidgets.QPushButton(self.centralwidget)
        self.check_button.setGeometry(QtCore.QRect(30, 30, 201, 51))
        self.check_button.setStyleSheet("background-color: rgb(254, 204, 102);")
        self.check_button.setObjectName("check_button")
        self.return1_button = QtWidgets.QPushButton(self.centralwidget)
        self.return1_button.setGeometry(QtCore.QRect(125, 260, 150, 51))
        self.return1_button.setStyleSheet("background-color: rgb(254, 204, 102);")
        icon = QtGui.QIcon()
        filelog = os.getcwd()
        icon.addPixmap(QtGui.QPixmap(os.path.join(__location__, "reply.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(os.path.join(__location__, "reply.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.return1_button.setIcon(icon)
        self.return1_button.setIconSize(QtCore.QSize(50, 50))
        self.return1_button.setObjectName("return1_button")
        self.balance_label = QtWidgets.QLabel(self.centralwidget)
        self.balance_label.setGeometry(QtCore.QRect(240, 30, 100, 20))
        self.balance_label.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.balance_label.setText("")
        self.balance_label.setObjectName("balance_label")
        self.balance_label.setAlignment(QtCore.Qt.AlignCenter)
        balanceScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(balanceScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 604, 24))
        self.menubar.setObjectName("menubar")
        balanceScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(balanceScreen)
        self.statusbar.setObjectName("statusbar")
        balanceScreen.setStatusBar(self.statusbar)

        self.retranslateUi(balanceScreen)
        QtCore.QMetaObject.connectSlotsByName(balanceScreen)

    def retranslateUi(self, balanceScreen):
        _translate = QtCore.QCoreApplication.translate
        balanceScreen.setWindowTitle(_translate("balanceScreen", "atm3"))
        self.check_button.setText(_translate("balanceScreen", "AVAIBLE BALANCE"))
        self.return1_button.setText(_translate("balanceScreen", "RETURN MENU"))
