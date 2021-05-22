import pickle

class Personaje:

	def __init__(self, nombre, vida, ataque, defensa, alcance):
		self.nombre = nombre
		self.vida = vida
		self.ataque = ataque
		self.defensa = defensa
		self.alcance = alcance
		print("Se ha creado el personaje")

	def __str__(self):
		return """Nombre: {}
Vida: {}
Ataque: {}
Defensa: {}
Alcance: {}
		""".format(self.nombre, self.vida, self.ataque, self.defensa, self.alcance)

class Gestor:

	personajes = []

	def __init__(self):
		self.cargar()

	def add(self, personaje):
		for pTemp in self.personajes:
			if pTemp.nombre == personaje.nombre:
				return
		self.personajes.append(personaje)
		self.guardar()

	def borrar(self, nombre):
		for pTemp in self.personajes:
			if pTemp.nombre == nombre:
				self.personajes.remove(pTemp)
				self.guardar()
				print("\nPersonaje {} borrado".format(nombre))
				return

	def mostrar(self):
		if len(self.personajes) == 0:
			print("El gestor de personajes está vacío")
			return
		for p in self.personajes:
			print(p)

	def cargar(self):
		f = open('personajes.pkl', 'ab+')
		f.seek(0)
		try:
			self.personajes = pickle.load(f)
		except:
			print("El fichero está vacío")
		finally:
			f.close()
			print("Se ha cargado {} personajes".format(len(self.personajes)))

	def guardar(self):
		f = open('personajes.pkl','wb')
		pickle.dump(self.personajes, f)
		f.close()


G = Gestor()

#G.add(Personaje("Caballero", 4, 2, 4, 2))
#G.add(Personaje("Guerrero", 2, 4, 2, 4))
#G.add(Personaje("Arquero", 2, 4, 1, 8))
#G.add(Personaje("Tanque", 5, 3, 2, 2))

G.mostrar()
#G.borrar("Arquero")
#G.borrar("Tanque")