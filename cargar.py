from navegador import Navegador
from Tabs import Tab
nave = Navegador("Navegador_Pirta", "9.11") 
print ("Bienvenido \n")
opcion = None
while opcion!= 7:
	print("1. Crear Nuevo Tab\n2. Cambiar Url y Tab\n3. Cerrar Tab\n4. Cerrar todos los tabs\n5. Mostar mis Tabs\n6. Guardar mis Tabs\n7. Salir\n")
	opcion=int (input(": "))
	if opcion == 1:
		nombre = input("Ingrese Nombre: ")
		url = input ("Ingrese URL: ")
		nave.crear_tab(nombre, url)
	elif opcion == 2:
		numero_tab = int(input("Ingrese numero del tab: "))
		nombre = input("Ingrese Nuevo Nombre: ")
		url = input ("Ingrese Nuevo URL: ")
		nave.cambiar_tab(numero_tab, nombre, url)
	elif opcion == 3:
		numero_tab = int(input("Ingrese numero del tab: "))
		nave.cerrar_tab(numero_tab)
	elif opcion == 4: 
		nave.cerrar_todos()
	elif opcion == 5:
		for i in range(len(nombre)):
			print(i + ") " + nombres[i] + " " + tabs[i])
	elif opcion == 6:
		doc = open("tabs.txt", "w")
		for i in range(len(nombre)):
			print(i + ") " + nombres[i] + " " + tabs[i])
		doc.close()
print( "-----------------------------------")