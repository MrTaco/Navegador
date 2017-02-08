class Navegador(object):
	def __init__(self, nombre, version):
		self.nombre = nombre
		self.version = version
		self.tabs = []
		self.nombres = []
	def crear_tab(self, nombre, url):
		self.tabs.append(url)
		self.nombres.append(nombre)

	def cambiar_url(self, numero_tab, nombre, url):
		self.tabs[numero_tab] = url
		self.nombre [numero_tab] = nombre

	def cerrar_tab(self, numero_tab):
		self.tabs.pop[numero_tab]
		self.nombres.pop[numero_tab]

	def cerrar_todos(self):
		self.tabs = []
		self.nombres = []

	


