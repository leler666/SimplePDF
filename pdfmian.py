#!/usr/bin/python3
# -*- coding: UTF-8 -*-
'''
@Project ：pdfmian.py
@File    ：pdfmain.py
@Function: Main interface
@Author  ：Frank Y
@Date    ：2021/11/3 16:35
'''


from PyQt5 import QtCore, QtGui, QtWidgets
from pdflogin import Ui_Dialogmain as Log_ui
from pdfcut import Ui_Diacut as Cut_ui
from pdfcypt import Ui_Diacypt as Cypt_ui
from pdfcomb import Ui_Diacomb as Comb_ui
import sys


class Logui(QtWidgets.QDialog, Log_ui):
    switch_window1=QtCore.pyqtSignal()
    switch_window2=QtCore.pyqtSignal()
    switch_window3=QtCore.pyqtSignal()

    def __init__(self):
        super(Logui, self).__init__()
        self.setupUi(self)
        self.Bboxmain.accepted.connect(self.detect)

    def gocypt(self):
        self.switch_window1.emit()

    def gocut(self):
        self.switch_window2.emit()

    def gocomb(self):
        self.switch_window3.emit()

    def detect(self):
        if self.RBcypt.isChecked():
            self.switch_window1.emit()

        elif self.RBcut.isChecked():
            self.switch_window2.emit()

        else:
            self.switch_window3.emit()

class Cyptui (QtWidgets.QDialog, Cypt_ui):
    def __init__(self):
        super(Cyptui, self).__init__()
        self.setupUi(self)

class Cutui(QtWidgets.QDialog, Cut_ui):
    def __init__(self):
        super(Cutui, self).__init__()
        self.setupUi(self)

class Combui(QtWidgets.QDialog,Comb_ui):
    def __init__(self):
        super(Combui, self).__init__()
        self.setupUi(self)


class Controller:
    def __init__(self):
        pass

    def show_login(self):
        self.login=Logui()
        self.login.switch_window1.connect(self.show_cypt)
        self.login.switch_window2.connect(self.show_cut)
        self.login.switch_window3.connect(self.show_comb)
        self.login.show()

    def show_cypt(self):
        self.cypt=Cyptui()
        self.login.close()
        self.cypt.show()

    def show_cut(self):
        self.cut=Cutui()
        self.login.close()
        self.cut.show()

    def show_comb(self):
        self.comb=Combui()
        self.login.close()
        self.comb.show()

QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


