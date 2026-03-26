'''
import csv

def costo_camion(archivo):

    f = open(archivo)

    rows = csv.reader(f)

    headers = next(rows)

    lista = []

    costo_total = 0

#Codigo 2_9

    for n_row, row in enumerate(rows, start=1): #enumera las filas
        record = dict(zip(headers, row)) #crea un diccionario con las filas
        try: #Prueba el codigo de 2_9
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            costo_total += ncajones * precio
        except ValueError:
            print(f' Fila {n_row}: no pude interpretar: {row}')
    f.close() #Cierra el dataset
    print(costo_total)

costo_camion('/home/tareas/04_Datos/camion.csv')
print("-------------")
costo_camion('/home/tareas/04_Datos/fecha_camion.csv')
print("-------------")
costo_camion('/home/tareas/04_Datos/missing.csv')
'''


#INFORME.PY


import csv

def leer_precios(archivo):
    diccionariof = {}
    with open(archivo) as f:
        rr = csv.reader(f)
        for row in rr:
            if not row:
                continue
            diccionariof[row[0]] = float(row[1])
    return diccionariof

def leer_camion(archivo):
    diccionarioc = {}
    with open(archivo) as f:
        rr = csv.reader(f)
        headers = next(rr)
        total_camion = 0

        for row in rr:
            if not row:
                continue

            try:

                record = dict(zip(headers, row))

                nombre = record['nombre']
                cajones = int(record['cajones'])
                precio = float(record['precio'])

                total_camion += cajones * precio

                if nombre in diccionarioc:
                    diccionarioc[nombre] = (diccionarioc[nombre][0] + cajones, precio)
                else:
                    diccionarioc[nombre] = (cajones, precio)
            except ValueError:
                print(f"No pude interpretar la fila: {row}")
                continue

    return total_camion, diccionarioc

diccionariof = leer_precios('/mnt/d/programacion-I-unsam/codigo/data/precios.csv')
total_camion, diccionarioc = leer_camion('/mnt/d/programacion-I-unsam/codigo/data/fecha_camion.csv')

recaudacion = 0
for fruta in diccionarioc:
    cantidad = diccionarioc[fruta][0]
    precio_venta = diccionariof[fruta]
    recaudacion += cantidad * precio_venta

ganancia = recaudacion - total_camion
print(f"Costo del camión: {total_camion}")
print(f"Recaudación: {recaudacion}")
print(f"Ganancia: {ganancia}")

#Fin. Dante Grassi, Lic. Ciencia de Datos, UNSAM. Programacion I.