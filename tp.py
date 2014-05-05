"""Tarea Programada 2
	Andres Fernandez
	Luigui Madriga"""

#se importan las librerias necesarias de Flask
from flask import Flask, render_template, request, redirect, url_for, abort, session

app = Flask("HUNGRY?")#instancia de Flask

#pagina inicial
@app.route('/')
def home():
    return render_template('index.html')

#pagina agregar    
@app.route('/Agregar')
def agregar():
	return render_template('agregar.html')

#pagina consultar	
@app.route('/Consultar')
def consultar():
	return render_template('consultar.html')

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
	return render_template('res_agregado.html', nombre_res=nombre_res)
	
#pagina agregar platillo
@app.route('/AgregarPlatillo')
def agregar_platillo():
	return render_template('agregar_platillo.html')
	
#pagina platillo agregado correctamente
@app.route('/PlatilloAgregado', methods=['POST'])
def plat_agregado_correctamente():
	nombre_plat = request.form['nombre_plat']
	sabor_plat = request.form['sabor_plat']
	pais_plat = request.form['pais_plat']
	ingredientes_plat = request.form['ingredientes_plat']
	return render_template('plat_agregado.html', nombre_plat=nombre_plat)
	
#para correr la app
if __name__ == '__main__':
    app.run()
