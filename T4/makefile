# Arquivo: Makefile

#Traduzindo arquivos .ui gerados pela ferramenta de designer do pyqt para .py 
telas:
	pyuic5 telaLivro.ui -o telaLivro.py
	pyuic5 telaUsuario.ui -o telaUsuario.py
	pyuic5 telaEmprestimo.ui -o telaEmprestimo.py
	pyuic5 telaDevolucao.ui -o telaDevolucao.py

#Limpa os arquivos traduzidos
clean:
	@rm -f tela*.py
