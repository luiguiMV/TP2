#Se importa la libreria pyswip para el manejo de prolog

from pyswip.prolog import Prolog
#Se inicializa la variable P para prolog
p=Prolog()

#Funcion para cargar las reglas y algunos hechos a la base de conocimientos
def cargarBaseConocimiento():
	p.assertz("restaurante(hot_chicken,chatarra,tres_rios,89493450,jueves_lunes)")
	p.assertz("restaurante(kanalu,chatarra,sanjose,34567890,miercoles_sabado)")
	p.assertz("restaurante(burgerKing,chatarra,sanjose,34567890,miercoles_sabado)")
	p.assertz("restaurante(subway,saludable,cartago,111111,viernes_lunes)")
	p.assertz("restaurante(kentucky,chatarra,cartago,553321,viernes_lunes)")
	p.assertz("platillos(quesadilla,subway,dulce,costa_rica,chile_pan_leche)")
	p.assertz("platillos(pinto,spoon,dulce,costa_rica,azucar_pan_queso)")
	p.assertz("platillos(guacamole,el_Fogon,dulce,costa_rica,azucar_chile_leche)")
	p.assertz("platillos(chileguaro,spoon,dulce,costa_rica,azucar_cerveza_leche)")
	p.assertz("restaurante(quiznos,saludable,sanjose,34567890,miercoles_sabado)")
	p.assertz("restaurante(kentucky,chatarra,sanJose,54637,viernes_lunes)")
	p.assertz("restaurante(mcDonalds,chatarra,sanjose,34567890,miercoles_sabado)")
	p.assertz("restaurante(kentucky,chatarra,cartago,2222,viernes_lunes)")
	p.assertz("listaRestaurante(X):-restaurante(X,_,_,_,_)")
	p.assertz("tipo_comida(Y,X):-restaurante(Y,X,_,_,_)")
	p.assertz("listaPaises(Y,X):-platillos(_,Y,_,X,_)")
	p.assertz("listaRestaurantePorPlatillo(Y,X):-platillos(Y,X,_,_,_)")
	p.assertz("listaPlatillosPorIngrediente(Y,X,Z):-platillos(Y,X,_,_,Z)")
	p.assertz("listaNombre(V,W,X,Y,Z):-restaurante(V,W,X,Y,Z)")


	
#Metodo para agregar nuevos platillos a la base de conocimientos
def platillo(nombreplatillo, restaurate, sabor,pais,ingre):
	ingredientes=auxIngredientes(ingre)
	nuevo="platillos("+nombreplatillo.lower()+","+restaurate.lower()+","+sabor.lower()+","+pais.lower()+","+ingredientes.lower()+")"
	p.assertz(nuevo)
	

#Metodo para acomodar los ingredientes separados por _ para buscarlos posteriormente mejor
def auxIngredientes(ingre):
	plat=ingre.split(",")
	cadena=""
	cont=0
	while(cont!=len(plat)-1):
		cadena+=plat[cont]+"_"
		cont+=1
	cadena+=plat[cont]
	print (cadena)
	return cadena
	
#Metodo para buscar restaurantes por paises
def restaurantesPorPais(pais):
	lista=[]
	for result in p.query("listaPaises(X," + pais +")"):
		if result["X"] in lista:
			pass
		else:
			lista.append(result["X"])
	return lista 

#Metodo para buscar platillos por Restaurantes
def platillosPorRestaurante(rest):
	lista=[]
	for result in p.query("listaRestaurantePorPlatillo(X," + rest +")"):
		r = result["X"]
		lista.append(r)
	return lista

#Metodo para buscar platillos por ingredientes y restaurante
def platillosPorIngredientes(rest,ingrediente):
	lista=[]
	for result in p.query("listaPlatillosPorIngrediente(X"+","+ rest + "," + "Z" +")"):
		r = result["X"]
		h= result["Z"]
		temp=auxingrediente(h)
		if ingrediente in temp:
			lista.append(r)
	return lista

#Metodo para acomodar la cadena de string de ingrediente a ingrediente en cada indice de una lista
def auxingrediente(ing):
	plat=ing.split("_")
	return plat
	
#Metodo para agregar un nuevo restaurante a base.pl
def restaurante(nombre,tipocomida,ubicacion,telefono,horario):
	nuevo="restaurante("+nombre.lower()+","+tipocomida.lower()+","+ubicacion.lower()+","+telefono.lower()+","+horario.lower()+")"
	p.assertz(nuevo)


#Metodo que busca restaurantes filtrados por tipo comida
def buscarRestaurantePorComida(tipoDeComida):
	lista=[]
	for result in p.query("tipo_comida(X," + tipoDeComida +")"):
		if result["X"] in lista:
			pass
		else:
			lista.append(result["X"])
	return lista

#Metodo que busca restaurantes filtrados por el nombre
def buscarRestaurantePorNombre(nombre):
	lista=[]
	for result in p.query("listaNombre("+nombre +","+"W"+","+"X"+","+"Y"+","+"Z"")"):
		a="Se ubica en "+result["X"]+" el telefono de servicio al cliente es "+str(result["Y"])+" con un horario de atencion de "+result["Z"]
		lista.append(a)
	lista.append("El nombre del restaurante solicitado es: "+nombre+". El tipo de comida es "+result["W"])
	return lista
	
	
#Metodo que busca todos los restaurantes 
def mostrarRestaurantes():
	lista=[]
	for result in p.query("listaRestaurante(X)"):
		r = result["X"]
		lista.append(r)
	return lista

#Metodo para combrobar que las listas que se van a mostrar en la aplicacion web esten correctas
def imprimir(lista):
	cont=0
	while(cont!=len(lista)):
		print(lista[cont])
		cont+=1


cargarBaseConocimiento()
#buscarRestaurantePorNombre("kentucky")
#platillo("pinto","spoon","dulce","costa_rica","luigui,se,la,come,azucar,pan,queso")
#platillosPorIngredientes("spoon","leche")
#platillosPorRestaurante("spoon")
#restaurantesPorPais("costa_rica")
#mostrarRestaurantes()
#buscarRestaurantePorComida("saludable")

