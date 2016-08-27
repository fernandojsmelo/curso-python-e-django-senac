from pessoa import Pessoa 

class Filho(Pessoa):

	def __init__(self, **kwargs):
		super(Filho, self).__init__(**kwargs)

	def aniversario(self):
		self.idade += 1

	def caminhar(self):
		print("Aprentendo a caminhar")

	def chorar(self):
		print("Muleque chorando")

	def caminhar(self):
		print("Aprendendo a caminhar")

	def pega_nome_pessoa(self):
		return self.nome

	def somar(self,n1, n2):
		return n1 + n2
