# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\yunus\OneDrive\Desktop\atmproject\deneme\insert.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_insertScreen(object):
    def setupUi(self, insertScreen):
        insertScreen.setObjectName("insertScreen")
        insertScreen.resize(540, 509)
        insertScreen.setStyleSheet("background-color: rgb(127, 127, 127);")
        self.centralwidget = QtWidgets.QWidget(insertScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.return2_button = QtWidgets.QPushButton(self.centralwidget)
        self.return2_button.setGeometry(QtCore.QRect(190, 370, 181, 51))
        self.return2_button.setStyleSheet("background-color: rgb(254, 204, 102);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\yunus\\OneDrive\\Desktop\\atmproject\\deneme\\../gümüst/icons/reply.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\yunus\\OneDrive\\Desktop\\atmproject\\deneme\\../../gümüst/icons/icns/reply.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.return2_button.setIcon(icon)
        self.return2_button.setIconSize(QtCore.QSize(50, 50))
        self.return2_button.setObjectName("return2_button")
        self.balance_label = QtWidgets.QLabel(self.centralwidget)
        self.balance_label.setGeometry(QtCore.QRect(10, 30, 151, 31))
        self.balance_label.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"background-color: rgb(254, 204, 102);")
        self.balance_label.setObjectName("balance_label")
        self.clear2_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear2_button.setGeometry(QtCore.QRect(420, 30, 113, 41))
        self.clear2_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\yunus\\OneDrive\\Desktop\\atmproject\\deneme\\../../gümüst/icons/Küçük indir (2) .png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\yunus\\OneDrive\\Desktop\\atmproject\\deneme\\../../gümüst/icons/icns/Küçük indir (2) .png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.clear2_button.setIcon(icon1)
        self.clear2_button.setIconSize(QtCore.QSize(90, 70))
        self.clear2_button.setObjectName("clear2_button")
        self.enter2_button = QtWidgets.QPushButton(self.centralwidget)
        self.enter2_button.setGeometry(QtCore.QRect(420, 100, 113, 31))
        self.enter2_button.setStyleSheet("background-color: rgb(127, 127, 127);")
        self.enter2_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\yunus\\OneDrive\\Desktop\\atmproject\\deneme\\../../gümüst/icons/Küçük images (1) .png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\yunus\\OneDrive\\Desktop\\atmproject\\deneme\\../../gümüst/icons/icns/Küçük images (1) .png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.enter2_button.setIcon(icon2)
        self.enter2_button.setIconSize(QtCore.QSize(100, 50))
        self.enter2_button.setObjectName("enter2_button")
        self.deposit_label = QtWidgets.QLabel(self.centralwidget)
        self.deposit_label.setGeometry(QtCore.QRect(10, 100, 151, 31))
        self.deposit_label.setStyleSheet("background-color: rgb(254, 204, 102);")
        self.deposit_label.setObjectName("deposit_label")
        self.balance2_label = QtWidgets.QLabel(self.centralwidget)
        self.balance2_label.setGeometry(QtCore.QRect(220, 30, 161, 31))
        self.balance2_label.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.balance2_label.setText("")
        self.balance2_label.setObjectName("balance2_label")
        self.insert_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.insert_edit.setGeometry(QtCore.QRect(220, 100, 161, 31))
        self.insert_edit.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.insert_edit.setText("")
        self.insert_edit.setObjectName("insert_edit")
        self.mesaj_button = QtWidgets.QPushButton(self.centralwidget)
        self.mesaj_button.setGeometry(QtCore.QRect(160, 190, 261, 161))
        self.mesaj_button.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.mesaj_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\yunus\\OneDrive\\Desktop\\atmproject\\deneme\\../../gümüst/icons/icns/money.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mesaj_button.setIcon(icon3)
        self.mesaj_button.setIconSize(QtCore.QSize(50, 50))
        self.mesaj_button.setObjectName("mesaj_button")
        insertScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(insertScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 24))
        self.menubar.setObjectName("menubar")
        insertScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(insertScreen)
        self.statusbar.setObjectName("statusbar")
        insertScreen.setStatusBar(self.statusbar)

        self.retranslateUi(insertScreen)
        QtCore.QMetaObject.connectSlotsByName(insertScreen)

    def retranslateUi(self, insertScreen):
        _translate = QtCore.QCoreApplication.translate
        insertScreen.setWindowTitle(_translate("insertScreen", "insert"))
        self.return2_button.setText(_translate("insertScreen", "RETURN MENU"))
        self.balance_label.setText(_translate("insertScreen", "   AVAIBLE BALANCE"))
        self.deposit_label.setText(_translate("insertScreen", "DEPOSIT"))
