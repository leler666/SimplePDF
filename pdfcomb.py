# -*- coding: UTF-8 -*-
'''
@Project ：pdfmian.py
@File    ：pdfcomb.py
@Function: Combine PDF
@Author  ：Frank Y
@Date    ：2021/11/3 16:35
'''

from PyPDF2 import PdfFileWriter, PdfFileReader
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import time
import sys
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")


def merPdf(inplist,outname):
    pdf_out=PdfFileWriter()

    for infile in inplist:
        pdf_input=PdfFileReader(open(infile, 'rb'))
        pdf_pages=pdf_input.getNumPages()
        for page in range(pdf_pages):
            pdf_out.addPage(pdf_input.getPage(page))
    pdf_out.write(open(str(outname)+'.pdf','wb'))


class Ui_Diacomb(object):
    def setupUi(self, Diacomb):
        Diacomb.setObjectName("Diacomb")
        Diacomb.resize(399, 438)
        self.PBselet = QtWidgets.QPushButton(Diacomb)
        self.PBselet.setGeometry(QtCore.QRect(140, 260, 75, 23))
        self.PBselet.setObjectName("PBselet")
        self.LBcomb = QtWidgets.QLabel(Diacomb)
        self.LBcomb.setGeometry(QtCore.QRect(40, 290, 131, 16))
        self.LBcomb.setObjectName("LBcomb")
        self.PBcomb = QtWidgets.QPushButton(Diacomb)
        self.PBcomb.setGeometry(QtCore.QRect(300, 260, 75, 23))
        self.PBcomb.setObjectName("PBcomb")
        self.LBselect = QtWidgets.QLabel(Diacomb)
        self.LBselect.setGeometry(QtCore.QRect(40, 20, 121, 16))
        self.LBselect.setObjectName("LBselect")
        self.LWpicked = QtWidgets.QListWidget(Diacomb)
        self.LWpicked.setGeometry(QtCore.QRect(30, 40, 341, 171))
        self.LWpicked.setObjectName("LWpicked")
        self.LWmerged = QtWidgets.QListWidget(Diacomb)
        self.LWmerged.setGeometry(QtCore.QRect(30, 320, 341, 101))
        self.LWmerged.setObjectName("LWmerged")
        self.LBtip = QtWidgets.QLabel(Diacomb)
        self.LBtip.setGeometry(QtCore.QRect(60, 220, 221, 16))
        self.LBtip.setObjectName("LBtip")
        self.PBclear = QtWidgets.QPushButton(Diacomb)
        self.PBclear.setGeometry(QtCore.QRect(220, 260, 75, 23))
        self.PBclear.setObjectName("PBclear")

        self.retranslateUi(Diacomb)
        QtCore.QMetaObject.connectSlotsByName(Diacomb)

        self.PBselet.clicked.connect(self.pickPdf)
        self.PBcomb.clicked.connect(self.combPdf)
        self.PBclear.clicked.connect(self.clearPdf)

        self.inlist = []

    def retranslateUi(self, Diacomb):
        _translate = QtCore.QCoreApplication.translate
        Diacomb.setWindowTitle(_translate("Diacomb", "合并PDF"))
        self.PBselet.setText(_translate("Diacomb", "选择文件"))
        self.LBcomb.setText(_translate("Diacomb", "合并后新文件："))
        self.PBcomb.setText(_translate("Diacomb", "合并文件"))
        self.LBselect.setText(_translate("Diacomb", "待合并文件："))
        self.LBtip.setText(_translate("Diacomb", "Tip:按住Ctrl可以一次选择多个文件"))
        self.PBclear.setText(_translate("Diacomb", "清除文件"))

    def pickPdf(self):

        dir = QFileDialog()
        dir.setFileMode(QFileDialog.ExistingFiles)
        dir.setDirectory('D:\pyprojects\pythonProject2')
        dir.setNameFilter('PDF(*.pdf)')
        if dir.exec_():
            for i in dir.selectedFiles():
                self.inlist.append(i)
            self.LWpicked.addItems(dir.selectedFiles())

    def combPdf(self):
        now=int(time.time())
        merPdf(self.inlist, now)
        self.LWmerged.addItem(str(str(now)+'.pdf'))
        self.LWpicked.clear()
        self.inlist=[]

    def clearPdf(self):
        self.inlist=[]
        self.LWpicked.clear()