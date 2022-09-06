from Usuarios import Usuarios
import menu

listaUsuarios = list()

class Ingresos ():
	
	def existeDNI(self, dniIngresado):
		for u in listaUsuarios:
				if u.dni == dniIngresado:
					return True
		return False

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
		# print(listaUsuarios)
	
	def listar(self):
		for u in listaUsuarios:
			u.imprimir()

	def modificar(self):
		dni = int(menu.obtenerDatos('Ingrese su dni: ', [0,1], 2))
		for u in listaUsuarios:
			if self.existeDNI(dni):
				depositar = menu.obtenerDatos('Ingrese monto a depositar: ', [0,1], 2)
				retirar = menu.obtenerDatos('Ingrese monto a retirar: ', [0,1], 2)
				u.editarSaldo(depositar, retirar)
		
		
