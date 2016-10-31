# Arquivo: Makefile

#Traduzindo arquivos .ui gerados pela ferramenta de designer do pyqt para .py 
telas:
	pyuic5 telaLivro.ui -o telaLivro.py
	pyuic5 telaUsuario.ui -o telaUsuario.py

#Limpa os arquivos traduzidos
clean:
	@rm -f tela*.py
