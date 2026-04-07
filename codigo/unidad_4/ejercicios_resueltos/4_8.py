import csv

def leer_camion(nombre_archivo):
    camion = {}  # Creamos una lista VACÍA para guardar los diccionarios
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezados = next(filas) # Saltamos la primera línea (nombre,cajones,precio)
        
        for n_fila, fila in enumerate(filas, start=1):
            if not fila: # Salta filas vacías
                continue
            try:
                nombre = fila[0]
                cajones = int(fila[1])
                precio = float(fila[2])
                camion[nombre] = [cajones, precio]
            except ValueError:
                print(f"Fila {n_fila}: No se pudo procesar los datos de {fila}")
    return camion # Devolvemos la lista de diccionarios

camion = leer_camion('/mnt/d/programacion-I-unsam/codigo/data/camion.csv')

def hacer_informe(cajon):
    #Usamos camion.csv como cajon
    for fruta in cajon:
        cajon[fruta] = list(cajon[fruta])
        ventaf = float(input(f'Ingresa el precio de venta de el/la {fruta}: '))
        cambio = ventaf - cajon[fruta][1]
        cajon[fruta].append(cambio)
    # Imprimir informe bonito
    print(f'{"Fruta":>10s} {"Cajones":>10s} {"Precio":>10s} {"Ganancia":>10s}')
    print('-'*45)
    for fruta, valores in cajon.items():
        print(f'{fruta:>10s} {valores[0]:>10d} {valores[1]:>10.2f} {valores[2]:>10.2f}')
    
    return cajon

camion = leer_camion('../Data/camion.csv')