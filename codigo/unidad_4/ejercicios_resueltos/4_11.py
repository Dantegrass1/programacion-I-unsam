import csv

def leer_camion(nombre_archivo):
    camion = []  # Creamos una lista VACÍA para guardar los diccionarios
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
                
                camion.append({
                    'nombre': nombre,
                    'cajones': cajones,
                    'precio': precio
                })
            except ValueError:
                print(f"Fila {n_fila}: No se pudo procesar los datos de {fila}")
    return camion # Devolvemos la lista de diccionarios

camion = leer_camion('/mnt/d/programacion-I-unsam/codigo/data/camion.csv')

def hacer_informe(cajon):
    #Usamos camion.csv como cajon
    for fruta in cajon:
        ventaf = float(input(f'Precio de venta de {fruta['nombre']}: '))
        cambio = round(ventaf - fruta['precio'],2)
        fruta['cambio'] = cambio
    # Imprimir informe bonito
    print(f'{"Fruta":>10s} {"Cajones":>10s} {"Precio":>10s} {"Ganancia":>10s}')
    print(f'{"-"*10} {"-"*10} {"-"*10} {"-"*10}')
    for fruta in camion:
        precio = f'${fruta['precio']}'
        cambio = f'{fruta['cambio']:.2f}'
        
        print(f"{fruta['nombre']:>10s} {fruta['cajones']:>10d} {precio:>10s} {cambio:>10s}")
    
    return cajon

cajon = hacer_informe(camion)