#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request
import os, signal
import time
import json
import subprocess
import sys
import psutil
import platform
global currentProcess

app = Flask(__name__)

#Para que muestre menos logs
#import logging
#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)

@app.route('/actualizarPorcentaje')
def actualizarPorcentaje():

    arrVal = [0] * 5

    with open("C:/IA_MapaGen/web/frontend/ia-mapagen-front/ia-mapagen-front-app/api/venv/status_process.txt", "r") as fp:
            var = ""
            val = ""
            for i, line in enumerate(fp):
                var, val = line.split(": ")
                arrVal[i] = val.replace("\n", "")

    resultado = {
      "transcurrido": arrVal[0],
      "restante": arrVal[1],
      "porcentaje": float(arrVal[2]),
      "estado": arrVal[3],
    }

    print("Leo valor: " + str(resultado))

    
    return  resultado

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
     
        p = subprocess.Popen('"C:/IA_MapaGen/Proceso/HeatMap.exe" ' +
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
    file = open("C:/IA_MapaGen/web/frontend/ia-mapagen-front/ia-mapagen-front-app/api/venv/status_process.txt", "w")    

    resultado = {
      "transcurrido": "0",
      "restante": "0",
      "porcentaje": 0.0,
      "estado": "Iniciando",
    }

    file.write("transcurrido: 0\n")
    file.write("restante: 0\n")
    file.write("porcentaje: 0.0\n")
    file.write("estado: Iniciando")

    file.close()

    return resultado

@app.route('/finalizarActualizarPorcentaje')
def finalizarActualizarPorcentaje():
    file = open("C:/IA_MapaGen/web/frontend/ia-mapagen-front/ia-mapagen-front-app/api/venv/status_process.txt", "w")    

    resultado = {
      "transcurrido": "0",
      "restante": "0",
      "porcentaje": 0.0,
      "estado": "Detenido",
    }

    file.write("transcurrido: 0\n")
    file.write("restante: 0\n")
    file.write("porcentaje: 0.0\n")
    file.write("estado: Detenido")

    file.close()

    return resultado
    
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
    p = subprocess.Popen('"C:/IA_MapaGen/Proceso/HeatMap.exe" parametro',shell=True,
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
    proceso = -1
    pid = -1
    
    try:      
        pathVideoToAnalizer = 'C:\\IA_MapaGen\\Input\\' + request.args['pathVideoToAnalizer'].replace('"', '').replace("'", '')
        #pathVideoOutput = request.args['pathVideoOutput']  # llega algo por paramatro?
        pathNeural = 'C:\\IA_MapaGen\\Input\\' + request.args['pathNeural'].replace('"', '').replace("'", '')
        pathClassFile = 'C:\\IA_MapaGen\\Input\\' + request.args['pathClassFile'].replace('"', '').replace("'", '')
        minPercentage = request.args['minPercentage'].replace('"', '').replace("'", '')
        minPercentage = str(int(minPercentage) / 100);
        
        numberOfFrames = request.args['numberOfFrames'].replace('"', '').replace("'", '')      
        #parametros sin ingreso por pantalla
        pathVideoOutput = 'C:\\IA_MapaGen\\Output\\VideoSalida.avi'
        pathCSVOutput = 'C:\\IA_MapaGen\\Output\\OutputCsv.csv'
        
        print("Comienzo ejecucion de "+ "C:\\IA_MapaGen\\Proceso\\IA_MapaGen_Proceso.py "  + pathVideoToAnalizer + " TRUE " + pathVideoOutput 
              + " " + pathCSVOutput  + " " +  pathNeural  + " " + pathClassFile + " " + minPercentage+ " " + numberOfFrames + ' False True 213 179 "C:/IA_MapaGen/Output"')

        command = ["C:\\IA_MapaGen\\Proceso\\IA_MapaGen_Proceso.py", pathVideoToAnalizer, "True", pathVideoOutput, pathCSVOutput, pathNeural, pathClassFile, minPercentage, numberOfFrames, "False", "True", "213", "179","C:\\IA_MapaGen\\Output" ]

        p = subprocess.Popen(command, shell=True) #stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

        print("Iniciada la ejecucion")

        pid = p.pid
        print("PID --->>>>" + str(p.pid))
    except Exception as e:
        print("Excepcion: " + str(e))
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
    p = subprocess.Popen('"C:\IA_MapaGen\Proceso\HeatMap.exe" parametro',shell=True,
           stdin=None, stdout=None, stderr=None, close_fds=True)
    #subprocess.run('echo %pythonPATH%', shell=True)
    pid = p.pid
    print( p.pid)
    return {'proceso': pid}
