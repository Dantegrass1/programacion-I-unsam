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
            total_camion += int(row[1]) * float(row[2])
            if row[0] in diccionarioc:
                diccionarioc[row[0]] = (diccionarioc[row[0]][0] + int(row[1]), float(row[2]))
            else:
                diccionarioc[row[0]] = (int(row[1]), float(row[2]))
    return total_camion, diccionarioc

diccionariof = leer_precios('/mnt/d/programacion-I-unsam/codigo/data/precios.csv')
total_camion, diccionarioc = leer_camion('/mnt/d/programacion-I-unsam/codigo/data/camion.csv')

recaudacion = 0
for fruta in diccionarioc:
    cantidad = diccionarioc[fruta][0]
    precio_venta = diccionariof[fruta]
    recaudacion += cantidad * precio_venta

ganancia = recaudacion - total_camion
print(f"Costo del camión: {total_camion}")
print(f"Recaudación: {recaudacion}")
print(f"Ganancia: {ganancia}")