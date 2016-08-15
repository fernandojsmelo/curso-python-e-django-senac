#-*- coding: utf-8 -*-

import os

tarefa = int(input("Informe 1=Limpar Tela 2=Criar Diretorio 3=Iprimir Local Corrente : "))

if tarefa == 1:
	os.system("clear")
elif tarefa == 2:
	Diretorio = input("Informe o local e diretorio : ")
	os.mkdir (Diretorio)
elif tarefa == 3:
	local = os.path.abspath("")
	print(local)
else:
	print("ERRO")