#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request
import os, signal
import time
import json
import subprocess
import sys
import psutil


global currentProcess

app = Flask(__name__)
@app.route('/actualizarPorcentaje')
def actualizarPorcentaje():
    json_object = {}
    #file = open("../salidaPython.json", "r+")
    file = open("C:/Proyecto/web/frontend/ia-mapagen-front/ia-mapagen-front-app/api/venv/Scripts/remaining.txt", "r")
    #json_object = json.load(file)
    #print(json_object["porcentaje"])
    lectura = file.read()
    print("leo" + lectura)
    
    #json_object["archivosRestantes"] = json_object["archivosRestantes"] - 1
    #json_object["porcentaje"] = json_object["porcentaje"] + 1
    file.close()

    #file = open("../salidaPython.json", "w")
    #json.dump(json_object, file)
    #file.close()
    
    #return {'porcentaje': json_object["porcentaje"] }
    return {'porcentaje': lectura  }

#Generador de mapa de calor

#para invocar usar 
# http://localhost:5000/runHeatMap?pathCSVFile="C:\pathCSVFile.csv"&pathVideoToAnalizer="C:\pathVideoToAnalizer.avi"&squaresQuantity=10&radiusH=5&pathHeatMapGenerate="C:\pathHeatMapGenerate.csv"
# si logra ejecutar devuelve PID de proceso, sino devuelve -1
# HeatMap_UNLa_Abremate_v3.01 C:\Proyecto\Inputs\FragmentoAbrematePruebas_LowFrames.mp4 C:\Proyecto\Output\video_salida.avi C:\Proyecto\Output\output_csv.csv True C:/Proyecto/Inputs/RED_NEURONAL/frozen_inference_graph.pb C:\Proyecto\Inputs\RED_NEURONAL\mscoco_label_map.pbtxt 0.01 10 False False 90
#                       
@app.route('/runHeatMap')
def runHeatMap(): 
    #Ubicación y nombre del archivo CSV a utilizar - pathCSVFile (ruta absoluta incluye nombre y extension)
    #Ubicación y nombre del archivo de Video analizado (Para tomar el primer Frame) - pathVideoToAnalizer (ruta absoluta incluye nombre y extension)
    #Cantidad de cuadrados en la grilla - squaresQuantity
    #Radio H - radiusH
    #Ubicación y nombre para guardar el mapa de calor generado - pathHeatMapGenerate (ruta absoluta incluye nombre y extension)
    proceso = -1
    try: 
        pathCSVFile = request.args['pathCSVFile']
        pathVideoToAnalizer = request.args['pathVideoToAnalizer']
        squaresQuantity = request.args['squaresQuantity']
        radiusH = request.args['radiusH']
        pathHeatMapGenerate = request.args['pathHeatMapGenerate']
     
        p = subprocess.Popen('"c:\Proyecto\HeatMap UNLa\HeatMap_UNLa_Abremate_v2.2_sin_parametros.py" ' +
                pathCSVFile + ' ' + pathVideoToAnalizer + ' ' + squaresQuantity + ' ' + radiusH
               + ' ' + pathHeatMapGenerate, shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
    
        #subprocess.run('echo %pythonPATH%', shell=True)
        pid = p.pid
        print(p.pid)
    except:
        proceso = -1

    return {'proceso': pid}

@app.route('/resetPorcentaje')
def resetPorcentaje():
    file = open("C:/Proyecto/web/frontend/ia-mapagen-front/ia-mapagen-front-app/api/venv/Scripts/remaining.txt", "w")    
    file.close()
    return {'porcentaje': 0  }

@app.route('/finalizarActualizarPorcentaje')
def finalizarActualizarPorcentaje():
    file = open("C:/Proyecto/web/frontend/ia-mapagen-front/ia-mapagen-front-app/api/venv/Scripts/remaining.txt", "w")    
    file.write(str(100))
    file.close()
    return {'porcentaje': 100  }
    


#para invocar usar http://localhost:5000/stopHeatMap?pidToKill=15140
@app.route('/stopHeatMap')
def stopHeatMap():
    status = 'error'
    pidToKill = request.args['pidToKill']
    try:
        print(pidToKill)
        process_pid = psutil.Process(int(pidToKill))

        if (process_pid.name()).find("cmd") != -1: #para evitar matar cualquier proceso, solo detiene si es una consola
            print(process_pid)
            subprocess.call(['taskkill', '/F', '/T', '/PID',  str(pidToKill)])
            status = 'detenido'
            #NO status = os.kill(pidToKill, 9)
    except:
        status = 'no existe proceso'
    return {'status': status}

@app.route('/runHeatMapWithParameters')
def runHeatMapWithParameters():
    p = subprocess.Popen('"C:\Proyecto\HeatMap UNLa\HeatMap_UNLa_Abremate_v2.2_sin_parametros.py" parametro',shell=True,
           stdin=None, stdout=None, stderr=None, close_fds=True)
    #subprocess.run('echo %pythonPATH%', shell=True)
    pid = p.pid
    print( p.pid)
    return {'proceso': pid}
    
@app.route('/showHeatMap')
def showHeatMap():
    json_object = {}     
    return {'status': json_object["200"] }
    
# Procesador de video
    
    # http://localhost:5000/runVideoProcessor?pathVideoToAnalizer=C:\pathVideoToAnalizer.csv&pathVideoOutput=C:\pathVideoOutput.avi&pathNeural=C:\pathNeural&pathClassFile=C:\pathClassFile&minPercentage=100&numberOfFrames=20
# si logra ejecutar devuelve PID de proceso, sino devuelve -1
@app.route('/runVideoProcessor')
def runVideoProcessor(): 
    #Ubicación y nombre del archivo de video a analizar - pathVideoToAnalizer (ruta absoluta incluye nombre y extension)
    #Ubicación y nombre del archivo de salida (Con detecciones) (Opcional) - pathVideoOutput (ruta absoluta incluye nombre y extension)
    #Ubicación y nombre del archivo de red neuronal pre-entrenada  - pathNeural
    #Ubicación y nombre del archivo de clases a detectar (mscoco_label_map.pbtxt) - pathClassFile
    #Porcentaje mínimo de coincidencia para detecciones (Entre 0.01 y 0.99. Por defecto 0.01) - minPercentage
    #Cada cuantos frames analizar - numberOfFrames
# HeatMap_UNLa_Abremate_v3.01 C:\Proyecto\Inputs\FragmentoAbrematePruebas_LowFrames.mp4 C:\Proyecto\Output\video_salida.avi 
# C:\Proyecto\Output\output_csv.csv True C:/Proyecto/Inputs/RED_NEURONAL/frozen_inference_graph.pb C:\Proyecto\Inputs\RED_NEURONAL\mscoco_label_map.pbtxt 0.01 10 False False 90
    proceso = -1
    pid = -1
    
    try:      
        pathVideoToAnalizer = 'E:\Outputs\ABREMATE_PRUEBA\\' + request.args['pathVideoToAnalizer'].replace('"', '').replace("'", '')
        #pathVideoOutput = request.args['pathVideoOutput']  # llega algo por paramatro?
        pathNeural = 'E:\Outputs\ABREMATE_PRUEBA\\' + request.args['pathNeural'].replace('"', '').replace("'", '')
        pathClassFile = 'E:\Outputs\ABREMATE_PRUEBA\\' + request.args['pathClassFile'].replace('"', '').replace("'", '')
        minPercentage = request.args['minPercentage']        
        numberOfFrames = request.args['numberOfFrames']       
        #parametros sin ingreso por pantalla
        pathVideoOutput = 'E:\Outputs\ABREMATE_PRUEBA\Salida.avi'
        pathCSVOutput = 'E:\Outputs\ABREMATE_PRUEBA\output_csv.csv'
        
        print("Comienzo ejecucion de "+ "C:\Proyecto\HeatMap UNLa\HeatMap_UNLa_Abremate_v3.3.py "  + pathVideoToAnalizer + " TRUE " + pathVideoOutput 
              + " " + pathCSVOutput  + " " +  pathNeural  + " " + pathClassFile + " " + minPercentage+ " " + numberOfFrames + ' False False 90')
            #pathVideoToAnalizer + " " + pathVideoOutput + " " + pathNeural + " " + pathClassFile
             #   + " " + minPercentage, + " " + numberOfFrames)

        p = subprocess.Popen('"C:\Proyecto\HeatMap UNLa\HeatMap_UNLa_Abremate_v3.3.py" ' +
            pathVideoToAnalizer  + ' True '  + pathVideoOutput + ' ' + pathCSVOutput + ' ' +  pathNeural +  ' '  + pathClassFile  + ' ' +
                 minPercentage + ' ' + numberOfFrames + ' False True 213 179 E:/Outputs/ABREMATE_PRUEBA', shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
        #subprocess.run('echo %pythonPATH%', shell=True)
        pid = p.pid
        print("PID --->>>>" + p.pid)
    except:
        print("Excepcion")
        proceso = -1

    return {'proceso': pid}

#para invocar usar http://localhost:5000/stopVideoProcessor?pidToKill=15140
@app.route('/stopVideoProcessor')
def stopVideoProcessor(): 
    status = 'error'
    pidToKill = request.args['pidToKill']
    try:
        print(pidToKill)
        process_pid = psutil.Process(int(pidToKill))

        if (process_pid.name()).find("cmd") != -1: #para evitar matar cualquier proceso, solo detiene si es una consola
            print(process_pid)
            subprocess.call(['taskkill', '/F', '/T', '/PID',  str(pidToKill)])
            status = 'detenido'
            #NO status = os.kill(pidToKill, 9)
    except:
        status = 'no existe proceso'
    return {'status': status}

@app.route('/runVideoProcessorWithParameters')
def runVideoProcessorWithParameters():
    p = subprocess.Popen('"C:\Proyecto\HeatMap UNLa\HeatMap_UNLa_Abremate_v2.2_sin_parametros.py" parametro',shell=True,
           stdin=None, stdout=None, stderr=None, close_fds=True)
    #subprocess.run('echo %pythonPATH%', shell=True)
    pid = p.pid
    print( p.pid)
    return {'proceso': pid}
