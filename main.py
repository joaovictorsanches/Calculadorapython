import os
class Calculadora:
	@classmethod
	def somar(cls, *nums):
		s = 0
		for n in nums:
			s += n
		return s
	@classmethod
	def subtrair(cls, *nums):
		sb = 0
		for n in nums:
			if (sb == 0):
				sb = n
			else:
				sb -= n
		return sb
	@classmethod
	def mutplicar(cls, *nums):
		m = 1
		for n in nums:
			m *= n
		return m
	@classmethod
	def dividir(cls, *nums):
		d = 1
		for n in nums:
			d /= n
		return d
class Menu:
	def __init__(self, op, fun):
		self.stop = False
		self.cal = Calculadora()
		self.opcoes_menu = op
		self.funs = fun

	def criar_menu(self, opcoes):
		for op, txt in opcoes.items():
			print(f"\033[33m(\033[m \033[32m{op}\033[m \033[33m)\033[m \033[31m-\033[m \033[34m{txt}\033[m")

	def des(self, res):
		if (not res == "00"):
			f = self.funs.get(res)
			if (not f == None):
				lista = []
				while (1):
					n = input("Digite um numero (REALIZAR OPERAÇÃO: 00): ")
					if (n == "00"):
						break
					else:
						lista.append(int(n))
				return f(*lista)
			else:
				return "Opção invalida!"
		else:
			self.stop = True
			return "quit"

	def menu(self):
		while (not (self.stop)):
			os.system("clear")
			self.criar_menu(self.opcoes_menu)
			ret = self.des(input("==>"))
			if (not ret == "quit"):
				print("Retorno:", ret)
				input("Next")
		print("Finalizado")
opcoes = {
                "1":"Somar",
		"2":"Subtrair",
                "3":"Dividir",
                "4":"Mutplicar",
                "00":"Sair"
}
cal = Calculadora()
funs = {
	"1":cal.somar,
	"2":cal.subtrair,
	"3":cal.dividir,
	"4":cal.mutplicar,
}

menu = Menu(opcoes, funs)
menu.menu()
