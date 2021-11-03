# -*- coding: UTF-8 -*-
'''
@Project ：pdfmian.py
@File    ：pdfcut.py
@Function: Cut PDF
@Author  ：Frank Y
@Date    ：2021/11/3 16:35
'''

from PyPDF2 import PdfFileWriter, PdfFileReader
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QMessageBox
from PyQt5.QtWidgets import QFileDialog
import os
import time


def cutPdfmore(infn, pagenum, outname):
    pdf_out = PdfFileWriter()
    pdf_in = PdfFileReader(open(infn, 'rb'))
    pdf_out.addPage(pdf_in.getPage(pagenum - 1))
    pdf_out.write(open(str(outname) + 'cut.pdf', 'wb'))


def cutPdfonly1(infn, pagenum, outname):
    pdf_out = PdfFileWriter()
    pdf_in = PdfFileReader(open(infn, 'rb'))
    pages = pdf_in.getNumPages()
    plist = list(range(pages))
    plist.remove(pagenum - 1)
    for i in plist:
        pdf_out.addPage(pdf_in.getPage(i))
    pdf_out.write(open(str(outname) + 'cut.pdf', 'wb'))


class Ui_Diacut(object):
    def setupUi(self, Diacut):
        Diacut.setObjectName("Diacut")
        Diacut.resize(347, 314)
        self.LCDnum = QtWidgets.QLCDNumber(Diacut)
        self.LCDnum.setGeometry(QtCore.QRect(180, 20, 101, 31))
        self.LCDnum.setObjectName("LCDnum")
        self.LBtallnum = QtWidgets.QLabel(Diacut)
        self.LBtallnum.setGeometry(QtCore.QRect(40, 20, 181, 31))
        self.LBtallnum.setObjectName("LBtallnum")
        self.PBcutfile = QtWidgets.QPushButton(Diacut)
        self.PBcutfile.setGeometry(QtCore.QRect(230, 160, 75, 23))
        self.PBcutfile.setObjectName("PBcutfile")
        self.LBcutedfile = QtWidgets.QLabel(Diacut)
        self.LBcutedfile.setGeometry(QtCore.QRect(20, 180, 101, 21))
        self.LBcutedfile.setObjectName("LBcutedfile")
        self.PBselcutfile = QtWidgets.QPushButton(Diacut)
        self.PBselcutfile.setGeometry(QtCore.QRect(140, 160, 75, 23))
        self.PBselcutfile.setObjectName("PBselcutfile")
        self.LWnewfile = QtWidgets.QListWidget(Diacut)
        self.LWnewfile.setGeometry(QtCore.QRect(20, 200, 311, 101))
        self.LWnewfile.setObjectName("LWnewfile")
        self.widget = QtWidgets.QWidget(Diacut)
        self.widget.setGeometry(QtCore.QRect(60, 70, 241, 61))
        self.widget.setObjectName("widget")
        self.GridL = QtWidgets.QGridLayout(self.widget)
        self.GridL.setContentsMargins(0, 0, 0, 0)
        self.GridL.setObjectName("GridL")
        self.RBsave = QtWidgets.QRadioButton(self.widget)
        self.RBsave.setObjectName("RBsave")
        self.RBsave.setChecked(True)
        self.GridL.addWidget(self.RBsave, 0, 0, 1, 1)
        self.SBsave = QtWidgets.QSpinBox(self.widget)
        self.SBsave.setObjectName("SBsave")
        self.SBsave.setRange(0, 999)
        self.GridL.addWidget(self.SBsave, 0, 1, 1, 1)
        self.RBremove = QtWidgets.QRadioButton(self.widget)
        self.RBremove.setObjectName("RBremove")
        self.GridL.addWidget(self.RBremove, 1, 0, 1, 1)
        self.SBremove = QtWidgets.QSpinBox(self.widget)
        self.SBremove.setObjectName("SBremove")
        self.SBremove.setEnabled(False)
        self.SBremove.setRange(0, 999)
        self.GridL.addWidget(self.SBremove, 1, 1, 1, 1)

        self.retranslateUi(Diacut)
        QtCore.QMetaObject.connectSlotsByName(Diacut)

        self.filena = 0
        self.pagenumber = 0
        self.filesl = []
        self.PBselcutfile.clicked.connect(self.slectFile)
        self.RBremove.clicked.connect(self.shiftInput2)
        self.RBsave.clicked.connect(self.shiftInput1)
        self.PBcutfile.clicked.connect(self.starCut)

    def retranslateUi(self, Diacut):
        _translate = QtCore.QCoreApplication.translate
        Diacut.setWindowTitle(_translate("Diacut", "切割PDF"))
        self.LBtallnum.setText(_translate("Diacut", "选中的PDF总页数为："))
        self.PBcutfile.setText(_translate("Diacut", "开始切割"))
        self.LBcutedfile.setText(_translate("Diacut", "切割后的文件为："))
        self.PBselcutfile.setText(_translate("Diacut", "选择文件"))
        self.RBsave.setText(_translate("Diacut", "只留下该页："))
        self.RBremove.setText(_translate("Diacut", "只去掉该页"))

    def starCut(self):

        now = int(time.time())

        if self.RBsave.isChecked() and self.SBsave.value() and self.SBsave.value() <= self.pagenumber:
            cutPdfmore(self.filesl[0], self.SBsave.value(), now)
            self.filena = 0
            self.pagenumber = 0
            self.filesl = []
            self.LWnewfile.addItem(str(str(now) + 'cut.pdf'))

        elif self.RBremove.isChecked() and self.SBremove.value() and self.SBremove.value() <= self.pagenumber:
            cutPdfonly1(self.filesl[0], self.SBremove.value(), now)
            self.filena = 0
            self.pagenumber = 0
            self.filesl = []
            self.LWnewfile.addItem(str(str(now) + 'cut.pdf'))

        else:
            QMessageBox.warning(None, '警告', '输入的数值不能为0或大于总页码', QMessageBox.Ok)
            #print('no one is ready')

    def shiftInput2(self):
        self.SBremove.setEnabled(True)
        self.SBsave.setEnabled(False)

    def shiftInput1(self):
        self.SBremove.setEnabled(False)
        self.SBsave.setEnabled(True)

    def slectFile(self):
        slect = QFileDialog()
        slect.setFileMode(QFileDialog.ExistingFiles)
        slect.setDirectory('D:\pyprojects\pythonProject2')
        slect.setNameFilter('PDF(*.pdf)')
        if slect.exec_():
            self.filena = os.path.basename(slect.selectedFiles()[0])
            new_file = open(self.filena, 'rb')
            pdf_reader = PdfFileReader(new_file, strict=False)
            self.pagenumber = pdf_reader.getNumPages()
            self.filesl = slect.selectedFiles()
            self.LCDnum.setProperty('value', self.pagenumber)
