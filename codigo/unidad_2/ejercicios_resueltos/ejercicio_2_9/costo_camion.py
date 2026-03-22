#Version 2.2

f = open('codigo/data/camion.csv', 'rt') #Leeo el archivo csv

headers = next(f).split(',') #Salteo la primera fila.

total = 0 #Inicio variable

for line in f: #Por cada linea en el dataset...

    row = line.split(',') #separa los datos de las filas por coma

    rows = float(row[1]) * float(row[2]) #Multiplica el segundo y tercer dato de la fila entre ellos, calculando el total pagado por ese cajon

    total = total + rows #Hace un total, para acumularlo por cada cajon
f.close() #Cierra el dataset

print(f'el costo total es: {total}') #Muestra el total

#Version 2.6

def costo_camion(archivo):

    f = open(archivo, 'rt') #Leeo el archivo csv

    headers = next(f).split(',') #Salteo la primera fila.

    total = 0 #Inicio variable

    for line in f: #Por cada linea en el dataset...

        row = line.split(',') #separa los datos de las filas por coma

        rows = float(row[1]) * float(row[2]) #Multiplica el segundo y tercer dato de la fila entre ellos, calculando el total pagado por ese cajon

        total = total + rows #Hace un total, para acumularlo por cada cajon

    f.close() #Cierra el dataset

    print(f'el costo total es: {total}') #Muestra el total

costo_camion(str(input('Ingresa la direccion del archivo para analizarlo: ')))

#Version 2.9

import csv

def costo_camion(archivo):

    f = open(archivo)#Leeo el archivo csv

    rr = csv.reader(f)

    headers = next(rr) #Salteo la primera fila.

    total = 0 #Inicio variable

    for row in rr: #Por cada linea en el dataset...

        rows = float(row[1]) * float(row[2]) #Multiplica el segundo y tercer dato de la fila entre ellos, calculando el total pagado por ese cajon

        total = total + rows #Hace un total, para acumularlo por cada cajon

    f.close() #Cierra el dataset

    print(f'el costo total es: {total}') #Muestra el total

costo_camion(str(input('Ingresa la direccion del archivo para analizarlo: ')))

#Fin. Dante Grassi, Lic. Ciencia de Datos, UNSAM. Programacion I.