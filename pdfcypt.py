# -*- coding: UTF-8 -*-
'''
@Project ：pdfmian.py
@File    ：pdfcypt.py
@Function: Encrypt PDF
@Author  ：Frank Y
@Date    ：2021/11/3 16:35
'''

from PyPDF2 import PdfFileWriter, PdfFileReader
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QFileDialog
import os

def add_encryption(input_pdf, output_pdf, password):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(input_pdf)

    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))

    pdf_writer.encrypt(user_pwd=password, owner_pwd=None,
                       use_128bit=True)

    with open(output_pdf, 'wb') as fh:
        pdf_writer.write(fh)

class Ui_Diacypt(object):
    def setupUi(self, Diacypt):
        Diacypt.setObjectName("Diacypt")
        Diacypt.resize(400, 300)
        self.PBselectfile = QtWidgets.QPushButton(Diacypt)
        self.PBselectfile.setGeometry(QtCore.QRect(290, 260, 75, 23))
        self.PBselectfile.setObjectName("PBselectfile")
        self.LWcypt = QtWidgets.QListWidget(Diacypt)
        self.LWcypt.setGeometry(QtCore.QRect(30, 50, 331, 192))
        self.LWcypt.setObjectName("LWcypt")
        self.LBcypt = QtWidgets.QLabel(Diacypt)
        self.LBcypt.setGeometry(QtCore.QRect(50, 20, 111, 16))
        self.LBcypt.setObjectName("LBcypt")

        self.retranslateUi(Diacypt)
        QtCore.QMetaObject.connectSlotsByName(Diacypt)
        self.PBselectfile.clicked.connect(self.encryFile)

    def retranslateUi(self, Diacypt):
        _translate = QtCore.QCoreApplication.translate
        Diacypt.setWindowTitle(_translate("Diacypt", "加密PDF"))
        self.PBselectfile.setText(_translate("Diacypt", "选择文件"))
        self.LBcypt.setText(_translate("Diacypt", "以下文件已被加密："))

    def encryFile(self):
        dir = QFileDialog()
        dir.setFileMode(QFileDialog.ExistingFile)
        dir.setDirectory('D:\pyprojects\pythonProject2')
        dir.setNameFilter('PDF(*.pdf)')
        if dir.exec_():
            name, ok = QInputDialog.getText(self, "password", "Plz input PWD", )
            self.LWcypt.addItems(dir.selectedFiles())
            Infile = os.path.basename(dir.selectedFiles()[0])
            FT, ED= os.path.splitext(Infile)

            add_encryption(input_pdf= Infile,
                           output_pdf= (FT + '加密' + ED),
                           password= name)
