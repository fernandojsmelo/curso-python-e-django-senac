import string

entrada = open("mensagem.txt", "r")

saida = entrada.replace("a","*")
print (saida)
saida = saida.replace("e","*")
saida = saida.replace("i","*")
saida = saida.replace("o","*")
saida = saida.replace("u","*")

novo = open("resposta.txt", "w")

novo.write(novo)
