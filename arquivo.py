arquivo = open("numeros.txt", "w")

for x in range(0,101):
	if x%2 == 0:
		arquivo.write('{} \n'.format(x))
arquivo.close()
