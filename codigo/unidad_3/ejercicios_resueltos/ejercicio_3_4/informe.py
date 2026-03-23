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

leer_precios('/mnt/d/programacion-I-unsam/codigo/data/precios.csv')

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
leer_camion('/mnt/d/programacion-I-unsam/codigo/data/camion.csv')

print('-----------------')

from informe import total_camion

print(total_camion)