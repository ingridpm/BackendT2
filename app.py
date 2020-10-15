from flask import Flask, request, jsonify
import json
from flask_cors import CORS, cross_origin
from Funcion import Funcion

app = Flask(__name__)
CORS(app)
funciones = []

@app.route('/', methods=['GET'])
def inicio():
    return "Bienvenido"

@app.route('/agregarFuncion', methods=['POST'])
def agregarFuncion():
    cuerpo = request.get_json()
    nombre = cuerpo['nombre']
    horario = cuerpo['horario']
    nueva_funcion = Funcion(nombre,horario)
    global funciones
    funciones.append(nueva_funcion)
    return jsonify({'mensaje':'Agregado correctamente'})

@app.route('/obtenerFunciones', methods=['GET'])
def obtenerFunciones():
    json_funciones = []
    global funciones
    for funcion in funciones:
        json_funciones.append({"nombre":funcion.nombre, "horario":funcion.horario, "disponible":funcion.disponible()})
    return jsonify(json_funciones)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=4000)
