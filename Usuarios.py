class Usuarios():

	def __init__(self, dni, nombre, apellido, depositar, retirar):
		self.dni = dni
		self.nombre = nombre
		self.apellido = apellido
		self.depositar = depositar
		self.retirar = retirar
		self.saldo = (depositar - retirar)
		self.cuenta = []
	
	def imprimir(self):

		print('DNI: {}\nNombre: {}\nApellido: {}\nSaldo: {}'.format(self.dni, self.nombre, self.apellido, self.saldo))
	
	def estadoCuenta(self):
		print('''
		DNI: {}
		Nombre: {}
		Apellido: {}
		'''.format(self.dni, self.nombre, self.apellido,))

	def editarSaldo(self, depositar, retirar):
		self.depositar = depositar
		self.retirar = retirar
		self.saldo -= depositar - retirar
		print(f'Su saldo ahora es de: {self.saldo}')

