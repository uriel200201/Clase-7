from Usuarios import Usuarios
from colorama import init, Fore,Back, Style
import menu

init()
listaUsuarios = list()

class Ingresos ():

	msj = Fore.RED+'No hay usuarios registrados'+Fore.RESET
	
	def existeDNI(self, dniIngresado):
		for u in listaUsuarios:
				if u.dni == dniIngresado:
					return True
		return False
	
	def listaVacia(self):
		if len(listaUsuarios) == 0:
			return True
	
	def registrarUsuarios(self):
		print("Registro de Usuarios\n")
		dni = int(menu.obtenerDatos('Ingrese su dni: ', [0,1], 2))
		if len(listaUsuarios) > 0:
			while self.existeDNI(dni):
				print('El DNI ya existe porfavor ingrese uno diferente')
				dni = int(menu.obtenerDatos('Ingrese su dni: ', [0,1], 2))

		nombre = str(input('Ingrese su nombre: '))
		apellido = str(input('Ingrese su apellido: '))
		depositar = menu.obtenerDatos('Ingrese monto a depositar: ', [0,1], 2)
		retirar = menu.obtenerDatos('Ingrese monto a retirar: ', [0,1], 2)
		usuarioOBJ = Usuarios(dni, nombre, apellido, depositar, retirar)
		listaUsuarios.append(usuarioOBJ)
		recibo = usuarioOBJ.modificacion(depositar, retirar)
		usuarioOBJ.historial.append(recibo)
		# print(listaUsuarios)
	
	def listar(self):
		if self.listaVacia():
			return print(self.msj)
		for u in listaUsuarios:
			u.imprimir()

	def buscar(self):
		if self.listaVacia():
			return print(self.msj)
		dni = int(menu.obtenerDatos('Ingrese el dni del usuario que desea buscar: ', [0,1], 2))
		for u in listaUsuarios:
			if self.existeDNI(dni):
				u.imprimir()

	def modificar(self):
		if self.listaVacia():
			return print(self.msj)
		dni = int(menu.obtenerDatos('Ingrese el dni del usuario al que desea modificar: ', [0,1], 2))
		for u in listaUsuarios:
			if self.existeDNI(dni):
				depositar = menu.obtenerDatos('Ingrese monto a depositar: ', [0,1], 2)
				retirar = menu.obtenerDatos('Ingrese monto a retirar: ', [0,1], 2)
				u.editarSaldo(depositar, retirar)
				recibo = u.modificacion(depositar, retirar)
				u.historial.append(recibo)
		
	def historial(self):
		if self.listaVacia():
			return print(self.msj)
		dni = int(menu.obtenerDatos('Ingrese el dni del usuario del que desea ver el historial: ', [0,1], 2))
		for u in listaUsuarios:
			if self.existeDNI(dni):
				for msj in u.historial:
					print(f"recibo {u.historial.index(msj) + 1}: {msj}")
	
	def eliminar(self):
		if self.listaVacia():
			return print(self.msj)
		dni = int(menu.obtenerDatos('Ingrese el dni del usuario que desea eliminar: ', [0,1], 2))
		for u in listaUsuarios:
			if self.existeDNI(dni):
				listaUsuarios.remove(u)
				print('El usuario se ha eliminado correctamente')