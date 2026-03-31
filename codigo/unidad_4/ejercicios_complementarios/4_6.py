import csv
from collections import Counter

def leer_camion(nombre_archivo):
    camion = []  # Creamos una lista VACÍA para guardar los diccionarios
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezados = next(filas) # Saltamos la primera línea (nombre,cajones,precio)
        
        for n_fila, fila in enumerate(filas, start=1):
            if not fila: # Salta filas vacías
                continue
            try:
                # Creamos el diccionario para ESTA fila
                lote = {
                    'nombre'  : fila[0],
                    'cajones' : int(fila[1]),
                    'precio'  : float(fila[2])
                }
                camion.append(lote) # Lo agregamos a nuestra lista
            except ValueError:
                print(f"Fila {n_fila}: No se pudo procesar los datos de {fila}")
            print(lote)
    return camion # Devolvemos la lista de diccionarios

camion = leer_camion('/mnt/d/programacion-I-unsam/codigo/data/camion.csv')

tenencias = Counter()
for s in camion:
    tenencias[s['nombre']] += s['cajones']

print(tenencias)
