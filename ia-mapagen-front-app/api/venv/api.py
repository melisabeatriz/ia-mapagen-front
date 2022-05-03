#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request
import os, signal
import time
import json
import subprocess
import sys
import psutil
import asyncio
import platform
global currentProcess

app = Flask(__name__)
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
        pathVideoToAnalizer = 'C:/IA_MapaGen/Input/' + request.args['pathVideoToAnalizer'].replace('"', '').replace("'", '')
        #pathVideoOutput = request.args['pathVideoOutput']  # llega algo por paramatro?
        pathNeural = 'C:/IA_MapaGen/Input/' + request.args['pathNeural'].replace('"', '').replace("'", '')
        pathClassFile = 'C:/IA_MapaGen/Input/' + request.args['pathClassFile'].replace('"', '').replace("'", '')
        minPercentage = request.args['minPercentage']        
        numberOfFrames = request.args['numberOfFrames']       
        #parametros sin ingreso por pantalla
        pathVideoOutput = 'C:/IA_MapaGen/Output/VideoSalida.avi'
        pathCSVOutput = 'C:/IA_MapaGen/Output/OutputCsv.csv'
        
        print("Comienzo ejecucion de "+ "C:\IA_MapaGen\Proceso\IA_MapaGen_Proceso.exe "  + pathVideoToAnalizer + " TRUE " + pathVideoOutput 
              + " " + pathCSVOutput  + " " +  pathNeural  + " " + pathClassFile + " " + minPercentage+ " " + numberOfFrames + ' False False 213 179 "C:/IA_MapaGen/Output"')

##        tasks = []
##        #command = ["C:\\IA_MapaGen\\Proceso\\IA_MapaGen_Proceso.exe", "C:\\IA_MapaGen\\Input\\FragmentoAbrematePruebas.mp4", "True", "C:\\IA_MapaGen\\Output\\video_salida.avi", "C:\\IA_MapaGen\\Output\\output_csv.csv", "C:\\IA_MapaGen\\Input\\frozen_inference_graph_Adulto_Menor_roboflow_v10i.pb", "C:\\IA_MapaGen\\Input\\label_map_Adulto_Menor.pbtxt", "0.01","10", "True", "False", "213", "179","C:\\IA_MapaGen\\Output" ]
##        #tasks.append(run_command(*command))
##        
##        
##        command = 'C:\IA_MapaGen\Proceso\IA_MapaGen_Proceso.exe ' + pathVideoToAnalizer  + ' True '  + pathVideoOutput + ' ' + pathCSVOutput + ' ' +  pathNeural +  ' '  + pathClassFile  + ' ' + minPercentage + ' ' + numberOfFrames + ' True False 213 179 "C:/IA_MapaGen/Output/"'
##        tasks = [run_command_shell(command)]
##    
##        results = run_asyncio_commands(
##            tasks, max_concurrent_tasks=20
##        )

        #with open("C:/IA_MapaGen/Output/stdout.txt","wb") as out, open("C:/IA_MapaGen/Output/stderr.txt","wb") as err:
        p = subprocess.Popen('"C:\IA_MapaGen\Proceso\IA_MapaGen_Proceso.exe" ' +
                pathVideoToAnalizer  + ' True '  + pathVideoOutput + ' ' + pathCSVOutput + ' ' +  pathNeural +  ' '  + pathClassFile  + ' ' +
                minPercentage + ' ' + numberOfFrames + ' False False 213 179 "C:/IA_MapaGen/Output/"',
                shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

           
        #subprocess.run('echo %pythonPATH%', shell=True)
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







async def run_command(*args):
    """Run command in subprocess.

    Example from:
        http://asyncio.readthedocs.io/en/latest/subprocess.html
    """
    # Create subprocess
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )

    # Status
    print("Started: %s, pid=%s" % (args, process.pid), flush=True)

    # Wait for the subprocess to finish
    stdout, stderr = await process.communicate()

    # Progress
    if process.returncode == 0:
        print(
            "Done: %s, pid=%s, result: %s"
            % (args, process.pid, stdout.decode().strip()),
            flush=True,
        )
    else:
        print(
            "Failed: %s, pid=%s, result: %s"
            % (args, process.pid, stderr.decode().strip()),
            flush=True,
        )

    # Result
    result = stdout.decode().strip()

    # Return stdout
    return result


async def run_command_shell(command):
    """Run command in subprocess (shell).

    Note:
        This can be used if you wish to execute e.g. "copy"
        on Windows, which can only be executed in the shell.
    """
    # Create subprocess
    process = await asyncio.create_subprocess_shell(
        command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )

    # Status
    print("Started:", command, "(pid = " + str(process.pid) + ")", flush=True)

    # Wait for the subprocess to finish
    stdout, stderr = await process.communicate()

    # Progress
    if process.returncode == 0:
        print("Done:", command, "(pid = " + str(process.pid) + ")", flush=True)
    else:
        print(
            "Failed:", command, "(pid = " + str(process.pid) + ")", flush=True
        )

    # Result
    result = stdout.decode().strip()

    # Return stdout
    return result

def make_chunks(l, n):
    """Yield successive n-sized chunks from l.

    Note:
        Taken from https://stackoverflow.com/a/312464
    """
    if sys.version_info.major == 2:
        for i in xrange(0, len(l), n):
            yield l[i : i + n]
    else:
        # Assume Python 3
        for i in range(0, len(l), n):
            yield l[i : i + n]

def run_asyncio_commands(tasks, max_concurrent_tasks=0):
    """Run tasks asynchronously using asyncio and return results.

    If max_concurrent_tasks are set to 0, no limit is applied.

    Note:
        By default, Windows uses SelectorEventLoop, which does not support
        subprocesses. Therefore ProactorEventLoop is used on Windows.
        https://docs.python.org/3/library/asyncio-eventloops.html#windows
    """
    all_results = []

    if max_concurrent_tasks == 0:
        chunks = [tasks]
        num_chunks = len(chunks)
    else:
        chunks = make_chunks(l=tasks, n=max_concurrent_tasks)
        num_chunks = len(list(make_chunks(l=tasks, n=max_concurrent_tasks)))

##    if asyncio.get_event_loop().is_closed():
##        asyncio.set_event_loop(asyncio.new_event_loop())
##    else:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
        
##    if platform.system() == "Windows":
##        asyncio.set_event_loop(asyncio.ProactorEventLoop())
    #loop = asyncio.get_event_loop()

    chunk = 1
    for tasks_in_chunk in chunks:
        print(
            "Beginning work on chunk %s/%s" % (chunk, num_chunks), flush=True
        )
        commands = asyncio.gather(*tasks_in_chunk)  # Unpack list using *
        results = loop.run_until_complete(commands)
        all_results += results
        print(
            "Completed work on chunk %s/%s" % (chunk, num_chunks), flush=True
        )
        chunk += 1

    loop.close()
    return all_results




