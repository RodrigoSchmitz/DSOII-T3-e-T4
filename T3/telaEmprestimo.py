# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaEmprestimo.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TelaEmprestimo(object):
    def setupUi(self, TelaEmprestimo):
        TelaEmprestimo.setObjectName("TelaEmprestimo")
        TelaEmprestimo.resize(640, 480)
        self.buttonBox = QtWidgets.QDialogButtonBox(TelaEmprestimo)
        self.buttonBox.setGeometry(QtCore.QRect(10, 440, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.labelTitulo = QtWidgets.QLabel(TelaEmprestimo)
        self.labelTitulo.setGeometry(QtCore.QRect(210, 10, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setObjectName("labelTitulo")
        self.comboUsuario = QtWidgets.QComboBox(TelaEmprestimo)
        self.comboUsuario.setGeometry(QtCore.QRect(110, 110, 79, 22))
        self.comboUsuario.setObjectName("comboUsuario")
        self.labelUsuario = QtWidgets.QLabel(TelaEmprestimo)
        self.labelUsuario.setGeometry(QtCore.QRect(40, 110, 59, 14))
        self.labelUsuario.setObjectName("labelUsuario")
        self.labeilLivro = QtWidgets.QLabel(TelaEmprestimo)
        self.labeilLivro.setGeometry(QtCore.QRect(40, 290, 41, 16))
        self.labeilLivro.setObjectName("labeilLivro")
        self.comboLivro = QtWidgets.QComboBox(TelaEmprestimo)
        self.comboLivro.setGeometry(QtCore.QRect(110, 290, 79, 22))
        self.comboLivro.setObjectName("comboLivro")
        self.dataEmprestimo = QtWidgets.QCalendarWidget(TelaEmprestimo)
        self.dataEmprestimo.setGeometry(QtCore.QRect(320, 100, 272, 149))
        self.dataEmprestimo.setObjectName("dataEmprestimo")

        self.retranslateUi(TelaEmprestimo)
        self.buttonBox.accepted.connect(TelaEmprestimo.accept)
        self.buttonBox.rejected.connect(TelaEmprestimo.reject)
        QtCore.QMetaObject.connectSlotsByName(TelaEmprestimo)

    def retranslateUi(self, TelaEmprestimo):
        _translate = QtCore.QCoreApplication.translate
        TelaEmprestimo.setWindowTitle(_translate("TelaEmprestimo", "Dialog"))
        self.labelTitulo.setText(_translate("TelaEmprestimo", "Tela Emprestimo"))
        self.labelUsuario.setText(_translate("TelaEmprestimo", "Usuario: "))
        self.labeilLivro.setText(_translate("TelaEmprestimo", "Livro: "))

