# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Telas.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TelaUsuario(object):
    def setupUi(self, TelaUsuario):
        TelaUsuario.setObjectName("TelaUsuario")
        TelaUsuario.resize(640, 480)
        self.buttonBox = QtWidgets.QDialogButtonBox(TelaUsuario)
        self.buttonBox.setGeometry(QtCore.QRect(10, 440, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.tituloTelaUsuario = QtWidgets.QLabel(TelaUsuario)
        self.tituloTelaUsuario.setGeometry(QtCore.QRect(270, 20, 81, 16))
        self.tituloTelaUsuario.setObjectName("tituloTelaUsuario")
        self.inputNome = QtWidgets.QLineEdit(TelaUsuario)
        self.inputNome.setGeometry(QtCore.QRect(170, 170, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Sawasdee")
        font.setPointSize(18)
        self.inputNome.setFont(font)
        self.inputNome.setObjectName("inputNome")
        self.labelNome = QtWidgets.QLabel(TelaUsuario)
        self.labelNome.setGeometry(QtCore.QRect(60, 170, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.labelNome.setFont(font)
        self.labelNome.setObjectName("labelNome")

        self.retranslateUi(TelaUsuario)
        self.buttonBox.accepted.connect(TelaUsuario.accept)
        self.buttonBox.rejected.connect(TelaUsuario.reject)
        QtCore.QMetaObject.connectSlotsByName(TelaUsuario)

    def retranslateUi(self, TelaUsuario):
        _translate = QtCore.QCoreApplication.translate
        TelaUsuario.setWindowTitle(_translate("TelaUsuario", "Dialog"))
        self.tituloTelaUsuario.setText(_translate("TelaUsuario", "Tela Usuario"))
        self.labelNome.setText(_translate("TelaUsuario", "Nome:"))

