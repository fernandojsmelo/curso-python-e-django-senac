import os

arquivo = open("mensagem.txt", "w")
arquivo.close()

arquivo = open("mensagem.txt", "a")

arquivo.write("Eu Amo a Mamae \n")
arquivo.write("E o Papai")

arquivo.close()

arquivo = open("mensagem.txt", "r")
for linha in arquivo:
	print(linha)

arquivo.close()
