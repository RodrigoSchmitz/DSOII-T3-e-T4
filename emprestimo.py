import time
import sys

telaLivro = uic.loadUiType("telaLivro.ui")[0]  

class Livro():
    def __init__(self):
        self.nome = ""
        self.editora = ""
        self.numPaginas = 0
        self.emprestado = False

    def insert(self, livro, livros):
        livros.append(livro)

    def remove(self, livro, livros):
        livros.remove(livro)

class Usuario():
    def __init__(self):
        self.nome = ""

    def insert(self, usuario, usuarios):
        usuarios.append(usuario)

    def remove(self, usuario, usuarios):
        usuarios.remove(usuario)

class Emprestimo():
    def __init__(self, dataEmprestimo, livro, usuario):
        self.dataEmprestimo = time.time().now
        self.dataDevolucao = None
        self.livro = livro
        self.usuario = usuario

    def emprestar(self, livro, usuario):
        livro.emprestado = True
        return Emprestimo(livro, usuario)

    def devolver(self, emprestimo):
        emprestimo.livro.emprestado = False
        emprestimo.dataDevolucao = time.time().now
        return emprestimo

class Biblioteca():
    def __init__(self):
        self.livro = Livro()
        self.usuario = Usuario()
        self.emprestimo = None
        self.livros = []
        self.usuarios = []
        self.emprestimos = []

    def insertLivro(self, livro):
        livro.insert(livro, self.livros)

    def removeLivro(self, livro):
        livro.remove(livro, self.livros)

    def insertUsuario(self, usuario):
        usuario.insert(usuario, self.usuarios)

    def removeUsuario(self, usuario):
        usuario.remove(usuario, self.usuarios)

    def emprestar(self, livro, usuario):
        self.emprestimo = Emprestimo(livro, usuario)
        self.emprestimos.append(self.emprestimo.emprestar(self.emprestimo.livro, self.emprestimo.usuario))

    def devolver(self, emprestimo):
        self.emprestimo.devolver(emprestimo)