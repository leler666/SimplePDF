# -*- coding: UTF-8 -*-
'''
@Project ：pdfmian.py
@File    ：pdflogin.py
@Function: Login Window
@Author  ：Frank Y
@Date    ：2021/11/3 16:35
'''

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialogmain(object):

    def setupUi(self, Dialogmain):
        Dialogmain.setObjectName("Dialogmain")
        Dialogmain.resize(476, 191)

        self.Bboxmain = QtWidgets.QDialogButtonBox(Dialogmain)
        self.Bboxmain.setGeometry(QtCore.QRect(80, 140, 341, 32))
        self.Bboxmain.setOrientation(QtCore.Qt.Horizontal)
        self.Bboxmain.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.Bboxmain.setObjectName("Bboxmain")
        self.RBcypt = QtWidgets.QRadioButton(Dialogmain)
        self.RBcypt.setGeometry(QtCore.QRect(60, 90, 89, 16))
        self.RBcypt.setObjectName("RBcypt")
        self.RBcypt.setChecked(True)
        self.RBcut = QtWidgets.QRadioButton(Dialogmain)
        self.RBcut.setGeometry(QtCore.QRect(190, 90, 89, 16))
        self.RBcut.setObjectName("RBcut")
        self.RBcomb = QtWidgets.QRadioButton(Dialogmain)
        self.RBcomb.setGeometry(QtCore.QRect(320, 90, 89, 16))
        self.RBcomb.setObjectName("RBcomb")
        self.LBtitle = QtWidgets.QLabel(Dialogmain)
        self.LBtitle.setGeometry(QtCore.QRect(190, 30, 141, 31))
        self.LBtitle.setObjectName("LBtitle")
        self.LBversion = QtWidgets.QLabel(Dialogmain)
        self.LBversion.setGeometry(QtCore.QRect(30, 150, 191, 20))
        self.LBversion.setObjectName("LBversion")
        self.retranslateUi(Dialogmain)

        self.Bboxmain.accepted.connect(Dialogmain.accept)
        self.Bboxmain.rejected.connect(Dialogmain.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialogmain)


    def retranslateUi(self, Dialogmain):
        _translate = QtCore.QCoreApplication.translate
        Dialogmain.setWindowTitle(_translate("Dialogmain", "PDF简易编辑器"))
        self.RBcypt.setText(_translate("Dialogmain", "加密PDF"))
        self.RBcut.setText(_translate("Dialogmain", "切割PDF"))
        self.RBcomb.setText(_translate("Dialogmain", "合并PDF"))
        self.LBtitle.setText(_translate("Dialogmain", "请选择PDF操作"))
        self.LBversion.setText(_translate("Dialogmain", "Copyright 2021 Frank,  Ver  0.1"))


    



