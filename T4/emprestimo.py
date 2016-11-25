import telaUsuario
import datetime

class Livro():
    def __init__(self):
        self.nome = ""
        self.emprestado = False

    def set_nome(nome):
        self.nome = nome

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
    def __init__(self, livro, usuario):
        self.dataEmprestimo = datetime.datetime.now()
        self.dataDevolucao = None
        self.livro = livro
        self.usuario = usuario

    def emprestar(self, livro, usuario):
        livro.emprestado = True
        return Emprestimo(livro, usuario)

    def devolver(self, emprestimo):
        emprestimo.livro.emprestado = False
        emprestimo.dataDevolucao = datetime.datetime.now()
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

    def localizarLivro(self, nome):
        for x in self.livros:
            if(x.nome == nome):
                return x
        return None

    def localizarUsuario(self, nome):
        for x in self.usuarios:
            if(x.nome == nome):
                return x
        return None

    def localizarEmprestimo(self, livro, usuario):
        for x in self.emprestimos:
            if(x.livro == livro and x.usuario == usuario):
                return x
        return None

    def emprestar(self, livro, usuario):
        self.emprestimo = Emprestimo(livro, usuario)
        self.emprestimos.append(self.emprestimo.emprestar(self.emprestimo.livro, self.emprestimo.usuario))

    def devolver(self, emprestimo):
        self.emprestimo.devolver(emprestimo)
