class Usuarios():

	def __init__(self, dni, nombre, apellido, depositar, retirar):
		self.dni = dni
		self.nombre = nombre
		self.apellido = apellido
		self.depositar = depositar
		self.retirar = retirar
		self.saldo = (depositar - retirar)
		self.historial = []
	
	def imprimir(self):

		print('DNI: {}\nNombre: {}\nApellido: {}\nSaldo: {}'.format(self.dni, self.nombre, self.apellido, self.saldo))
	
	def estadoCuenta(self):
		print('''
		DNI: {}
		Nombre: {}
		Apellido: {}
		'''.format(self.dni, self.nombre, self.apellido))

	def editarSaldo(self, depositar, retirar):
		self.depositar = depositar
		self.saldo += depositar 
		self.retirar = retirar
		self.saldo -= retirar
		print(f'Su saldo ahora es de: {self.saldo}')

	def modificacion(self, deposito, retiro):
		return f'deposito {deposito}, retiro {retiro}'
