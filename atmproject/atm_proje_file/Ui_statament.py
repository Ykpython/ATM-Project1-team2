# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\yunus\OneDrive\Desktop\atmproject\deneme\statament.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_statementScreen(object):
    def setupUi(self, statementScreen):
        statementScreen.setObjectName("statementScreen")
        statementScreen.resize(673, 602)
        statementScreen.setStyleSheet("background-color: rgb(127, 127, 127);")
        self.centralwidget = QtWidgets.QWidget(statementScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.account_lable = QtWidgets.QLabel(self.centralwidget)
        self.account_lable.setGeometry(QtCore.QRect(210, 10, 261, 41))
        self.account_lable.setStyleSheet("background-color: rgb(102, 204, 255);")
        self.account_lable.setObjectName("account_lable")
        self.return4_button = QtWidgets.QPushButton(self.centralwidget)
        self.return4_button.setGeometry(QtCore.QRect(250, 490, 191, 51))
        self.return4_button.setStyleSheet("background-color: rgb(254, 204, 102);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\yunus\\OneDrive\\Desktop\\atmproject\\deneme\\../gümüst/icons/reply.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\yunus\\OneDrive\\Desktop\\atmproject\\deneme\\../../gümüst/icons/icns/reply.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.return4_button.setIcon(icon)
        self.return4_button.setIconSize(QtCore.QSize(50, 50))
        self.return4_button.setObjectName("return4_button")
        self.date_button = QtWidgets.QPushButton(self.centralwidget)
        self.date_button.setGeometry(QtCore.QRect(20, 71, 131, 41))
        self.date_button.setStyleSheet("background-color: rgb(254, 204, 102);")
        self.date_button.setObjectName("date_button")
        self.logins_button = QtWidgets.QPushButton(self.centralwidget)
        self.logins_button.setGeometry(QtCore.QRect(520, 70, 131, 41))
        self.logins_button.setStyleSheet("background-color: rgb(254, 204, 102);")
        self.logins_button.setObjectName("logins_button")
        self.aktivites_button = QtWidgets.QPushButton(self.centralwidget)
        self.aktivites_button.setGeometry(QtCore.QRect(20, 250, 131, 41))
        self.aktivites_button.setStyleSheet("background-color: rgb(254, 204, 102);")
        self.aktivites_button.setObjectName("aktivites_button")
        self.check4_button = QtWidgets.QPushButton(self.centralwidget)
        self.check4_button.setGeometry(QtCore.QRect(520, 250, 131, 41))
        self.check4_button.setStyleSheet("background-color: rgb(254, 204, 102);")
        self.check4_button.setObjectName("check4_button")
        self.date_label = QtWidgets.QLabel(self.centralwidget)
        self.date_label.setGeometry(QtCore.QRect(20, 120, 221, 101))
        self.date_label.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.date_label.setText("")
        self.date_label.setObjectName("date_label")
        self.logins_label = QtWidgets.QLabel(self.centralwidget)
        self.logins_label.setGeometry(QtCore.QRect(430, 120, 221, 101))
        self.logins_label.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.logins_label.setText("")
        self.logins_label.setObjectName("logins_label")
        self.aktivites_label = QtWidgets.QLabel(self.centralwidget)
        self.aktivites_label.setGeometry(QtCore.QRect(20, 300, 221, 101))
        self.aktivites_label.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.aktivites_label.setText("")
        self.aktivites_label.setObjectName("aktivites_label")
        self.check_label = QtWidgets.QLabel(self.centralwidget)
        self.check_label.setGeometry(QtCore.QRect(430, 300, 221, 101))
        self.check_label.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.check_label.setText("")
        self.check_label.setObjectName("check_label")
        statementScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(statementScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 673, 24))
        self.menubar.setObjectName("menubar")
        statementScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(statementScreen)
        self.statusbar.setObjectName("statusbar")
        statementScreen.setStatusBar(self.statusbar)

        self.retranslateUi(statementScreen)
        QtCore.QMetaObject.connectSlotsByName(statementScreen)

    def retranslateUi(self, statementScreen):
        _translate = QtCore.QCoreApplication.translate
        statementScreen.setWindowTitle(_translate("statementScreen", "statement"))
        self.account_lable.setText(_translate("statementScreen", "             ACCOUNT TRANSACTIONS"))
        self.return4_button.setText(_translate("statementScreen", "RETURN MENU"))
        self.date_button.setText(_translate("statementScreen", "CREATING DATE"))
        self.logins_button.setText(_translate("statementScreen", "LOGINS"))
        self.aktivites_button.setText(_translate("statementScreen", "MONEY ACTIVITES"))
        self.check4_button.setText(_translate("statementScreen", "CHECK BALANCE"))