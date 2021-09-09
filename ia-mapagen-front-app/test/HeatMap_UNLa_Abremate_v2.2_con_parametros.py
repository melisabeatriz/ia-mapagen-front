import sys, time

# Comprobación de seguridad, ejecutar sólo si se reciben 2 
# argumentos realemente
if len(sys.argv) == 6:  #ejemplo tres argumentos (+ nombre)
    print('parametros para: ' + sys.argv[0])
    print('Ubicación y nombre del archivo CSV a utilizar: ' +  sys.argv[1])
    print('Ubicación y nombre del archivo de Video analizado: ' +  sys.argv[2])
    print('Cantidad de cuadrados en la grilla: ' +  sys.argv[3])
    print('Radio H: ' +  sys.argv[4])
    print('Ubicación y nombre para guardar el mapa de calor generado: ' +  sys.argv[5])
else:    
    print('Faltan parametros')

while 1:
    print('working..') 
    time.sleep(5)
 
    
    