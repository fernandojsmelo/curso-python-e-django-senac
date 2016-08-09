import random

n = int(input("Quantos Nomes Voce Tem na lista :"))

lista = []
cont = 1

while cont <= n:
    nome = input("Informe {} Nome : ".format(cont))
    lista.append(nome)
    cont += 1

random.choice(lista)
print ("O Nome Sorteado : ",random.choice(lista))