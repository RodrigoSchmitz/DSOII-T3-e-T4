from telaLivro import Ui_TelaLivro
import telaUsuario
import telaEmprestimo
import telaDevolucao
import emprestimo
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

b = emprestimo.Biblioteca()

def __init__(self):
    def retornaLabelNome():
        telaDevolucao.inputNome.getText()

    def retornaLivroNome():
        return Ui_TelaLivro


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = Ui_TelaLivro(dialog)

    dialog.show()
    sys.exit(app.exec_())

def adicionarLivro():
	l = emprestimo.Livro(telaLivro.retornaLabelNome())
	b.insertLivro(l)

def adicionarUsuario():
	u = emprestimo.Usuario(telaUsuario.retornarNome())
	b.insertUsuario(u)

def fazerEmprestimo():
	l = b.localizarLivro(telaEmprestimo.retornaLabelNome())
	u = b.localizarUsuario(telaEmprestimo.retornarNome())
	b.emprestimo(l,u)

def fazerDevolucao():
	l = b.localizarLivro(telaDevolucao.retornaLabelNome())
	u = b.localizarUsuario(telaDevolucao.retornarNome())
	e = b.localizarEmprestimo(l,u)
	b.devolver(e)