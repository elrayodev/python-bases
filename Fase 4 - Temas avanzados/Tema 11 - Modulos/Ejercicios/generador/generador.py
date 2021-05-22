import random
import math

def leer_numero(ini, fin, mensaje):
	while True:
		try:
			numero = int(input(mensaje))
		except:
			print("Dato invalido. Rango de valores validos [{}-{}]".format(ini,fin))
		else:
			if numero >= ini and numero <= fin:
				break
	return numero

def generador():
	numeros = leer_numero(1,20,'¿Cuantos números quieres generar? [1-20]: ')
	modo = leer_numero(1,3,'¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ')

	numAleatorios = []

	if modo == 1:
		print("\nREDONDEANDO AL ALZA CON MATH.CEIL\n")
	elif modo == 2:
		print("\nREDONDEANDO A LA BAJA CON MATH.FLOOR\n")
	else:
		print("\nREDONDEANDO NORMALMENTE CON ROUND\n")

	for i in range(numeros):
		r = random.uniform(0,101)
		if modo == 1:
			rRedondeado = math.ceil(r)
			print("{}=>{}".format(r, rRedondeado))
		elif modo == 2:
			rRedondeado = math.floor(r)
			print("{}=>{}".format(r, rRedondeado))
		else:
			rRedondeado = round(r)
			print("{}=>{}".format(r, rRedondeado))
		numAleatorios.append(rRedondeado)

	return numAleatorios
	
g = generador()

print(g)