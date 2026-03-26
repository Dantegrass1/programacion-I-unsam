import csv

def costo_camion(archivo):

    f = open(archivo)

    rows = csv.reader(f)

    headers = next(rows)

    lista = []

    costo_total = 0

#Codigo 2_9

    for n_row, row in enumerate(rows, start=1):
        record = dict(zip(headers, row))#Enumera las filas
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
