class Personaje:

	def __init__(self, nombre, vida, ataque, defensa, alcance):
		self.nombre = nombre
		self.vida = vida
		self.ataque = ataque
		self.defensa = defensa
		self.alcance = alcance
		print("Se ha creado el personaje")

	def __str__(self):
		return """
				Vida: {}\n
				Ataque: {}\n
				Defensa: {}\n
				Alcance: {}\n
		""".format(self.vida, self.ataque, self.defensa, self.alcance)




