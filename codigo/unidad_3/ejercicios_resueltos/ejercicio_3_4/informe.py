import csv

def leer_precios(archivo):
    
    diccionariof = {}
    
    with open(archivo) as f:
        
        rr = csv.reader(f)
        
        for row in rr:
            
            if not row:
                
                continue
            
            diccionariof[row[0]] = float(row[1])
            
    print(diccionariof)
    return diccionariof

diccionariof = leer_precios('/mnt/d/programacion-I-unsam/codigo/data/precios.csv')

print('---------------------')

def leer_camion(archivo):

    diccionarioc = {}
    
    with open(archivo) as f:
        
        rr = csv.reader(f)
        
        headers = next(rr) #Salteo la primera fila.
        
        total_camion = 0
        
        for row in rr:
            
            if not row:
                
                continue
            
            rows = int(row[1]) * float(row[2]) #Multiplica el segundo y tercer dato de la fila entre ellos, calculando el total pagado por ese cajon
            
            total_camion = total_camion + rows #Hace un total, para acumularlo por cada cajon
            
            diccionarioc[row[0]] = (int(row[1]), float(row[2]))
    print(diccionarioc)
    return total_camion
    return diccionarioc
total_camion = leer_camion('/mnt/d/programacion-I-unsam/codigo/data/camion.csv')
diccionarioc = leer_camion('/mnt/d/programacion-I-unsam/codigo/data/camion.csv')


print('-----------------')

print(total_camion)

recaudacion = 0
for fruta in diccionarioc:
    cantidad = diccionarioc[fruta][0]
    precio_venta = diccionariof[fruta]
    recaudacion += cantidad * precio_venta
print(recaudacion)