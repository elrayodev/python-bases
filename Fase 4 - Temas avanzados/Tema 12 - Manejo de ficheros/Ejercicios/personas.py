from io import open

import codecs
with codecs.open('personas.txt', 'r', encoding='utf-8', errors='ignore') as fdata:
	lineas = fdata.readlines()
	fdata.close()

personas = []

for linea in lineas:
	campos = linea.replace("\n", "").split(";") # borramos los saltos de línea
	persona = {"id" : campos[0], "nombre" : campos[1], "apellido" : campos[2], "nacimiento" : campos[3]}
	personas.append(persona)

for p in personas:
	print("(id={}) {} {} => {} ".format(p['id'],p['nombre'], p['apellido'], p['nacimiento']))