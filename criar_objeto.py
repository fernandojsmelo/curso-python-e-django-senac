from pessoa import Pessoa 
from filho import Filho 

p1 = Pessoa("Fernando Melo", "Maria", 40)

print("Dados da Pessoa")
print("Nome :",p1.nome)
print("Mae :", p1.mae)
print("Idade :",p1.idade)
print("metodo chamado a partir do medoto Pessoa()")
print(p1.pega_nome_pessoa())
print(p1.somar())
print()

f1 = Filho(nome="Pedro",mae="Mari", idade=30)

print("Dados do Filho")
print("Nome :",f1.nome)
print("Mae :", f1.mae)
print("Idade :",f1.idade)
print("metodo chamado a partir do medoto Filho()")
print(f1.pega_nome_pessoa())
print(f1.somar(10, 10))