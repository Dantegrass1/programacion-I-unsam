import csv

from codigo.unidad_2.ejercicios_resueltos.ejercicio_2_13.diccionario_geringoso import diccionario

#Compra

def costo_camion(archivo):

    f = open(archivo)#Leeo el archivo csv

    rr = csv.reader(f)

    headers = next(rr) #Salteo la primera fila.

    total_compra = 0 #Inicio variable

    for row in rr: #Por cada linea en el dataset...

        rows = float(row[1]) * float(row[2]) #Multiplica el segundo y tercer dato de la fila entre ellos, calculando el total pagado por ese cajon

        total_compra = total + rows #Hace un total, para acumularlo por cada cajon

    f.close() #Cierra el dataset

    print(f'el costo total es: {total_compra}') #Muestra el total

costo_camion(str(input('Ingresa la direccion del archivo para analizarlo: ')))

#Fin. Dante Grassi, Lic. Ciencia de Datos, UNSAM. Programacion I.

#Venta

def leer_archivo(file):
    import csv

    diccionario = {}

    fruta = ''

    precio = 0.0

    f = open(file)#Leeo el archivo csv

    rr = csv.reader(f)

    for row in rr: #Por cada linea en el dataset...

        if len(row) >= 2:

            fruta = row[0]

            precio = row[1]

        diccionario[fruta] = float(precio)

    print(diccionario)

    f.close() #Cierra el dataset

leer_archivo(str(input('Ingresa la direccion del archivo para analizarlo: ')))

#Fin. Dante Grassi, Lic. Ciencia de Datos, UNSAM. Programacion I.

total_venta = 0
for fruta in diccionario:
    #precio * 

ganancia = total_venta - total_compra

#Tengo que seguir con la variable que muestra la ganancia. Se tiene que multiplicar el precio de el precios.csv por la cantidad de cajones en la que fruta(precios) == fruta(camion). Eso por cada fruta.