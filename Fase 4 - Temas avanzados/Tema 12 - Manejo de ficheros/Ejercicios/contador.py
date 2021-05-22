import os
import sys

if os.path.isfile('contador.txt'):
	print("El archivo existe")
	f = open('contador.txt', 'a+')
	f.seek(0)
	if os.stat('contador.txt').st_size == 0:
		print("El archivo se encuentra vacío")
		contenido = "0"
		f.write(contenido)
	else:
		contenido = f.readlines()
else:
	print("Archivo no existe")
	f = open('contador.txt','a')
	print("El archivo a sido creado")


try:
	contador = int(contenido)

	if len(sys.argv) == 2:
		if sys.argv[1] == "inc":
			contador += 1
		elif sys.argv[1] == "dec":
			contador -= 1

	print(contador)

	f = open('contador.txt','w')
	f.write(str(contador))
	f.close()
except:
	print("Error: Fichero corrupto")

