#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
import os
import time
import json
import subprocess
import sys

app = Flask(__name__)
@app.route('/actualizarPorcentaje')
def actualizarPorcentaje():
    json_object = {}
    file = open("../salidaPython.json", "r+")
    json_object = json.load(file)
    print(json_object["porcentaje"])

    json_object["archivosRestantes"] = json_object["archivosRestantes"] - 1
    json_object["porcentaje"] = json_object["porcentaje"] + 1
    file.close()

    file = open("../salidaPython.json", "w")
    json.dump(json_object, file)
    file.close()
    
    return {'porcentaje': json_object["porcentaje"] }

@app.route('/runHeatMap')
def runHeatMap(): 
    #file = open('C:\Proyecto\HeatMap UNLa\HeatMap_UNLa_Abremate_v2.2_sin_parametros.py', 'r').read()
    #return exec(file)
    #["python", "programa.py"] subprocess.run('python C:\Proyecto\HeatMap UNLa\HeatMap_UNLa_Abremate_v2.2_sin_parametros.py', shell=True)
    #p = subprocess.call('python "C:\Proyecto\HeatMap UNLa\HeatMap_UNLa_Abremate_v2.2_sin_parametros.py"', shell=True)
    
    
    subprocess.run('C:\Proyecto\HeatMap UNLa\HeatMap_UNLa_Abremate_v2.2_sin_parametros.py', shell=True)
    subprocess.run('echo %pythonPATH%', shell=True)
    return {'proceso': 'iniciado'}

    
@app.route('/resetPorcentaje')
def resetPorcentaje():
    json_object = {}
    
    json_object["archivosRestantes"] = 100
    json_object["porcentaje"] = 0
    
    file = open("../salidaPython.json", "w")
    json.dump(json_object, file)
    file.close()
    
    return {'porcentaje': json_object["porcentaje"] }



    
