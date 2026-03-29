import csv

def costo_camion(archivo):

    f = open(archivo)

    rows = csv.reader(f)

    headers = next(rows)

    lista = []

    total = 0

#Codigo 2_9

    for n_row, row in enumerate(rows, start=1): #Enumera las filas
        try: #Prueba el codigo de 2_9
            for row in rows: #Por cada linea en el dataset...

                row_o = float(row[1]) * float(row[2]) #Multiplica el segundo y tercer dato de la fila entre ellos, calculando el total pagado por ese cajon

                total = total + row_o #Hace un total, para acumularlo por cada cajon
            f.close() #Cierra el dataset

            print(f'el costo total es: {total}') #Muestra el total
        
        except ValueError:
            print(f' Fila {n_row}: no pude interpretar: {row}')

costo_camion('/home/tareas/04_Datos/missing.csv')

#Fin. Dante Grassi, Lic. Ciencia de Datos, UNSAM. Programacion I.


