
import random

#comandos para informa o inicio e o fim da lista
num  = int(input("Informe um Numero para o inicio da lista :"))
num1 = 1 + int(input("Informe um Numero para o final da lista :"))

#gerarando a lista com todos os elementos 
lista = list(range(num,num1))

#metodo para escolher um munero aleatorio
num2 = random.choice(lista)
num3 = 1

#loop geral para verificação de acerto 
while num3 != 0:

	#comando para receber numero digitado pelo usuário
    num3 = int(input("Tende adivinha o numero escolhido pelo Sistema \n"+
    	         " Ou informe 0 para sair : "))

    #teste de acerto do número
    if num2	 == num3 :
        print("Numero Correto {} :".format(num3))
        break

    #saida opcional do loop
    if num3 == 0:
    	print("O Numero Correto seria : {}".format(num2))
