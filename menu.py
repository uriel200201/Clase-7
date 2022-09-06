from Ingresos import Ingresos

ingresos = Ingresos()
while True:
	query = 0

	# Pasamos el valor a numero
	def pasarANumero(valor, tipoNumero: int):

			if tipoNumero == 1:
					valorConvertido = int(valor)
			elif tipoNumero == 2:
					valorConvertido = float(valor)

			return valorConvertido

	# Verificamos si el valor puede pasarse a número (ya sea int o float)
	def noEsNumerico(valor, tipoNumero):
			try:
					pasarANumero(valor, tipoNumero)
					return False
			except ValueError:
					return True

	#verificamos si esta en un rango de números
	def estaEnRango(rango, numero):
			return numero in range(*rango)

	# Obtenemos los datos y los verificamos
	def obtenerDatos(mensaje:str, rango, tipoNumero):

			error = 1

			valor = input(mensaje)

			# Nos vuelve a pedir que seleccionemos una de las opciones si fue erronea la elección
			while noEsNumerico(valor, tipoNumero) or error == 1:
					if noEsNumerico(valor, tipoNumero):
							print('Caracter u opción incorrecta')
							valor = input(mensaje)

					elif estaEnRango(rango, pasarANumero(valor, tipoNumero)) and tipoNumero == 1:
							valor = pasarANumero(valor, tipoNumero)
							error = 0
					elif tipoNumero == 2:
							valor = pasarANumero(valor, tipoNumero)
							error = 0
					else: 
							print('Caracter u opción incorrecta')
							valor = input(mensaje)
							
			return pasarANumero(valor, tipoNumero)

	# Pedimos que ingrese una opcion
	query = obtenerDatos('Que desea hacer\n1- Registrar\n2- Listar Usuarios\n3- Editar Saldo\n', [1,4], 1)

	if query == 1:
		ingresos.registrarUsuarios()
	elif query == 2:
		ingresos.listar()
	elif query == 3:
		ingresos.modificar()

