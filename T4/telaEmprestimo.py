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
        self.labeilLivro.setGeometry(QtCore.QRect(60, 160, 41, 16))
        self.labeilLivro.setObjectName("labeilLivro")
        self.comboLivro = QtWidgets.QComboBox(TelaEmprestimo)
        self.comboLivro.setGeometry(QtCore.QRect(110, 160, 79, 22))
        self.comboLivro.setObjectName("comboLivro")
        self.dataEmprestimo = QtWidgets.QCalendarWidget(TelaEmprestimo)
        self.dataEmprestimo.setGeometry(QtCore.QRect(320, 100, 272, 149))
        self.dataEmprestimo.setObjectName("dataEmprestimo")
        self.addLivro = QtWidgets.QPushButton(TelaEmprestimo)
        self.addLivro.setGeometry(QtCore.QRect(300, 390, 131, 27))
        self.addLivro.setObjectName("addLivro")
        self.addUser = QtWidgets.QPushButton(TelaEmprestimo)
        self.addUser.setGeometry(QtCore.QRect(490, 390, 131, 27))
        self.addUser.setObjectName("addUser")
        self.novoLivro = QtWidgets.QLineEdit(TelaEmprestimo)
        self.novoLivro.setGeometry(QtCore.QRect(300, 360, 131, 27))
        self.novoLivro.setObjectName("novoLivro")
        self.novoUser = QtWidgets.QLineEdit(TelaEmprestimo)
        self.novoUser.setGeometry(QtCore.QRect(490, 360, 131, 27))
        self.novoUser.setObjectName("novoUser")
        self.addEmprestimo = QtWidgets.QPushButton(TelaEmprestimo)
        self.addEmprestimo.setGeometry(QtCore.QRect(80, 220, 98, 27))
        self.addEmprestimo.setObjectName("addEmprestimo")
        self.comboEmprestimo = QtWidgets.QComboBox(TelaEmprestimo)
        self.comboEmprestimo.setGeometry(QtCore.QRect(150, 300, 191, 27))
        self.comboEmprestimo.setObjectName("comboEmprestimo")
        self.devolver = QtWidgets.QPushButton(TelaEmprestimo)
        self.devolver.setGeometry(QtCore.QRect(360, 300, 98, 27))
        self.devolver.setObjectName("devolver")
        self.labelEmprestimo = QtWidgets.QLabel(TelaEmprestimo)
        self.labelEmprestimo.setGeometry(QtCore.QRect(50, 300, 101, 20))
        self.labelEmprestimo.setObjectName("labelEmprestimo")

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
        self.addLivro.setText(_translate("TelaEmprestimo", "Adicionar Livro"))
        self.addUser.setText(_translate("TelaEmprestimo", "Adicionar Usuário"))
        self.addEmprestimo.setText(_translate("TelaEmprestimo", "Emprestimo"))
        self.devolver.setText(_translate("TelaEmprestimo", "Devolver"))
        self.labelEmprestimo.setText(_translate("TelaEmprestimo", "Empréstimo:"))

