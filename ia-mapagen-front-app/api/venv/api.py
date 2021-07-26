#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
import os
import time
import json

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

    
@app.route('/resetPorcentaje')
def resetPorcentaje():
    json_object = {}
    
    json_object["archivosRestantes"] = 100
    json_object["porcentaje"] = 0
    
    file = open("../salidaPython.json", "w")
    json.dump(json_object, file)
    file.close()
    
    return {'porcentaje': json_object["porcentaje"] }

