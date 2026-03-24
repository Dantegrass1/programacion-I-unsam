# camion_commandline.py
import csv
import sys  # Importa el módulo sys, que permite interactuar con el intérprete de Python (argumentos, rutas, etc.)

def costo_camion(nombre_archivo):
    total = 0
    with open(nombre_archivo) as f:
        rr = csv.reader(f)
        headers = next(rr)
        for row in rr:
            total += float(row[1]) * float(row[2])
    return total

# sys.argv es una lista con los argumentos que se pasan al ejecutar el script.
# sys.argv[0] siempre es el nombre del archivo .py que se esta ejecutando.
# sys.argv[1] seria el primer argumento que el usuario pasa, en este caso la ruta del csv.
if len(sys.argv) == 2:  # Si el usuario paso exactamente un argumento (ademas del nombre del script)
    nombre_archivo = sys.argv[1]  # usa ese argumento como ruta del archivo.
else:  # Si no paso ningun argumento
    nombre_archivo = '/mnt/d/programacion-I-unsam/codigo/data/camion.csv'  # usa esta ruta.

costo = costo_camion(nombre_archivo)
print(f'Costo total: {costo}')