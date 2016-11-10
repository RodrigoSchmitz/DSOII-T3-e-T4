import telaLivro
import telaUsuario
import telaEmprestimos
import telaDevolucao
import emprestimo


b = Biblioteca()
    
   

def adicionarLivro():
	l = Livro(telaLivro.retornaLabelNome())
	self.b.insertLivro(l)

def adicionarUsuario():
	u = Usuario(telaUsuario.retornarNome())
    self.b.insertUsuario(u)

def fazerEmprestimo():
	l = b.localizarLivro(telaEmprestimo.retornaLabelNome())
	u = b.localizarUsuario(telaEmprestimo.retornarNome())
	self.b.emprestimo(l,u)

def fazerDevolucao():
	l = b.localizarLivro(telaDevolucao.retornaLabelNome())
	u = b.localizarUsuario(telaDevolucao.retornarNome())
	e = b.localizarEmprestimo(l,u)
	self.b.devolver(e)