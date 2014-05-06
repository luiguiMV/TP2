"""Tarea Programada 2
	Andres Fernandez
	Luigui Madrigal
	Jose Maria Rojas"""

#se importan las librerias necesarias de Flask
from flask import Flask, render_template, request, redirect, url_for, abort, session
from backend import *

app = Flask("HUNGRY?")#instancia de Flask

#pagina inicial
@app.route('/')
def home():
    return render_template('index.html')
    
""""---------------------------------------------------------CONSULTA"""

"""---------------------------CONSULTA DE RESTAURANTES-----------------"""

#pagina consultar todos los restaurante
@app.route('/Ver_todos')
def ver_todos():
	lista= mostrarRestaurantes()
	return render_template('ver_todos.html', lista=lista, item="")
	
@app.route('/Por_tipo')
def ver_por_tipo():
	return render_template('por_tipo.html', lista=[], item="")
	
@app.route('/Por_tipo_2', methods=['POST'])
def res_por_tipo():
	tipo = request.form['tipo_comida']
	lista= buscarRestaurantePorComida(tipo)
	return render_template('por_tipo.html', lista=lista, item="")
	
@app.route('/Buscar_res')
def buscar_res():
	return render_template('buscar_res.html', lista=[], item="")
	
@app.route('/Buscar_res2', methods=['POST'])
def buscar_res2():
	nombre=request.form['nombre_res']
	lista=buscarRestaurantePorNombre(nombre)
	return render_template('buscar_res.html', lista=lista, item="")
	
@app.route('/Por_pais')
def ver_por_pais():
	return render_template('por_pais.html', lista=[], item="")
	
@app.route('/Por pais2', methods = ['POST'])
def ver_por_pais2():
	pais= request.form['pais_plat']
	lista = restaurantesPorPais(pais)
	return render_template('por_pais.html', lista=lista, item="")
	
"""---------------------------CONSULTA DE PLATILLOS-----------------"""
@app.route('/Platillo_por_restaurante')
def ver_plat_por_res():
	return render_template('ver_plat_por_res.html', lista=[], item="")
	
@app.route('/Platillo_por_restaurante2', methods=['POST'])
def ver_plat_por_res2():
	restaurante= request.form['restaurante']
	lista=platillosPorRestaurante(restaurante)
	return render_template('ver_plat_por_res.html',  lista=lista, item="")
	
@app.route('/Platillo_por_ingrediente')
def ver_plat_por_ing():
	return render_template('ver_plat_por_ing.html', lista=[], item="")
	
@app.route('/Platillo_por_ingrediente2', methods=['POST'])
def ver_plat_por_ing2():
	ingrediente=request.form['ingrediente']
	rest=request.form['rest']
	lista=platillosPorIngredientes(rest,ingrediente)
	return render_template('ver_plat_por_ing.html', lista=lista, item="")
	

""""---------------------------------------------------------AGREGAR"""
	
"""Funciones de RESTAURANTE"""	
#pagina agregar restaurante
@app.route('/AgregarRestaurante')
def agregar_restaurante():
	return render_template('agregar_restaurante.html')
	
#pagina que indica exito al agregar el restaurante
@app.route('/RestauranteAgregado', methods=['POST'])
def res_agregado_correctamente():
	nombre_res = request.form['nombre_res']
	tipo_comida_res = request.form['tipo_comida_res']
	ubicacion_res = request.form['ubicacion_res']
	telefono_res = request.form['telefono_res']
	horario_res = request.form['horario_res']
	restaurante(nombre_res, tipo_comida_res, ubicacion_res, telefono_res, horario_res)
	return render_template('res_agregado.html', nombre_res=nombre_res)
	
"""Funciones de AGREGAR PLATILLO"""	
#pagina agregar platillo
@app.route('/AgregarPlatillo')
def agregar_platillo():
	return render_template('agregar_platillo.html')

#pagina platillo agregado correctamente
@app.route('/PlatilloAgregado', methods=['POST'])
def plat_agregado_correctamente():
	nombre_plat = request.form['nombre_plat']
	res_plat = request.form['res_plat']
	sabor_plat = request.form['sabor_plat']
	pais_plat = request.form['pais_plat']
	ingredientes_plat = request.form['ingredientes_plat']
	platillo(nombre_plat, res_plat, sabor_plat, pais_plat, ingredientes_plat)
	return render_template('plat_agregado.html', nombre_plat=nombre_plat)
	
	
"""MAIN"""
#para correr la app
if __name__ == '__main__':
    app.run(host='192.168.0.125')
