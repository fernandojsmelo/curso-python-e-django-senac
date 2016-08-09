

idade = int(input("Informe sua Idade :"))

if idade >= 18:
	print("Pode entrar na Festa")
elif idade >= 16:
	atuldo = input("Você esta acompanhado de um Adulto? \n"
		           "S=SIM N=NAO : ")
	if atuldo == "S":
		print("Pode entrar na Festa")
	else:
		print("Lamento deve ir para casa")
else:
	print("Idade inverior a permitida, va durmir")