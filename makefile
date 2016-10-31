# Arquivo: Makefile
auto_telas.py : Telas.ui
	pyuic5 Telas.ui -o auto_telas.py
