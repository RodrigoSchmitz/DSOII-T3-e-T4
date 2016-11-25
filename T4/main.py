from telaLivro import Ui_TelaLivro
from telaUsuario import Ui_TelaUsuario
from telaEmprestimo import Ui_TelaEmprestimo
import telaEmprestimo
import telaDevolucao
import emprestimo
from emprestimo import Livro, Usuario, Emprestimo
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

b = emprestimo.Biblioteca()

class TelaUsuario(Ui_TelaUsuario):
	def __init__(self, dialog):
		Ui_TelaUsuario.__init__(self)
		self.setupUi(dialog)

		self.addUser.clicked.connect(self.printName)

	def printName(self):
		user = User()
		user.nome = self.inputNome.text()
		b.insertUsuario(user)

class TelaLivro(Ui_TelaLivro):
	def __init__(self, dialog):
		Ui_TelaLivro.__init__(self)
		self.setupUi(dialog)

		self.addLivro.clicked.connect(self.printName)

	def printName(self):
		livro = Livro()
		livro.nome = self.inputNome.text()
		b.insertLivro(livro)

class TelaEmprestimo(Ui_TelaEmprestimo):
	def __init__(self, dialog):
		Ui_TelaEmprestimo.__init__(self)
		self.setupUi(dialog)

		self.addLivro.clicked.connect(self.adicionaLivro)
		self.addUser.clicked.connect(self.adicionaUser)
		self.addEmprestimo.clicked.connect(self.adicionaEmprestimo)
		self.devolver.clicked.connect(self.devolveLivro)

	def adicionaLivro(self):
		livro = Livro()
		livro.nome = self.novoLivro.text()
		b.insertLivro(livro)
		self.novoLivro.setText("")
		self.comboLivro.clear()
		for livro in b.livros:
			self.comboLivro.addItem(str(livro.nome))
	
	def adicionaUser(self):
		user = Usuario()
		user.nome = self.novoUser.text()
		b.insertUsuario(user)
		self.novoUser.setText("")
		self.comboUsuario.clear()
		for user in b.usuarios:
			self.comboUsuario.addItem(str(user.nome))

	def adicionaEmprestimo(self):
		livro = b.localizarLivro(self.comboLivro.currentText())
		usuario = b.localizarUsuario(self.comboUsuario.currentText())
		b.emprestar(livro, usuario)
		self.comboLivro.removeItem(self.comboLivro.currentIndex())
		self.comboEmprestimo.clear()
		for emp in b.emprestimos:
			self.comboEmprestimo.addItem(str(emp.livro.nome) + " - " + str(emp.usuario.nome))


	def devolveLivro(self):
		emp = self.comboEmprestimo.currentText().split(" - ")
		livro = b.localizarLivro(emp[0])
		usuario = b.localizarUsuario(emp[1])
		emprestimo = b.localizarEmprestimo(livro, usuario)
		b.devolver(emprestimo)
		b.emprestimos.remove(emprestimo)
		self.comboEmprestimo.removeItem(self.comboEmprestimo.currentIndex())
		self.comboLivro.addItem(str(livro.nome))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = TelaEmprestimo(dialog)

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