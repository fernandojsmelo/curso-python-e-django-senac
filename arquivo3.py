resultado = open("saida.txt", "w")
with open('mensagem.txt') as f:
	entrada = f.readlines()

	for linha in entrada:
		for letra in linha:
			if letra in "AaEeIiOoUu":
				resultado.write("*")
			else:
				resultado.write(letra)

print(resultado)


