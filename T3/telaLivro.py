# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaLivro.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TelaLivro(object):
    def setupUi(self, TelaLivro):
        TelaLivro.setObjectName("TelaLivro")
        TelaLivro.resize(640, 480)
        self.inputNome = QtWidgets.QLineEdit(TelaLivro)
        self.inputNome.setGeometry(QtCore.QRect(240, 180, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.inputNome.setFont(font)
        self.inputNome.setObjectName("inputNome")
        self.labelTitulo = QtWidgets.QLabel(TelaLivro)
        self.labelTitulo.setGeometry(QtCore.QRect(250, 40, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setObjectName("labelTitulo")
        self.labelNome = QtWidgets.QLabel(TelaLivro)
        self.labelNome.setGeometry(QtCore.QRect(70, 180, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.labelNome.setFont(font)
        self.labelNome.setObjectName("labelNome")
        self.addLivro = QtWidgets.QPushButton(TelaLivro)
        self.addLivro.setGeometry(QtCore.QRect(290, 260, 111, 31))
        self.addLivro.setObjectName("addLivro")

        self.retranslateUi(TelaLivro)
        self.inputNome.textChanged['QString'].connect(self.inputNome.setText)
        QtCore.QMetaObject.connectSlotsByName(TelaLivro)

    def retranslateUi(self, TelaLivro):
        _translate = QtCore.QCoreApplication.translate
        TelaLivro.setWindowTitle(_translate("TelaLivro", "Dialog"))
        self.labelTitulo.setText(_translate("TelaLivro", "TelaLivro"))
        self.labelNome.setText(_translate("TelaLivro", "Nome Livro: "))
        self.addLivro.setText(_translate("TelaLivro", "Adicionar"))

