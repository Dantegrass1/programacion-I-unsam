def buscar_precio(fruta):
    f = open('codigo/data/precios.csv', 'rt')
    
    encontrada = False
    
    for line in f:
        
        row = line.split(',')
        
        if len(row) >= 2:
            
            nombre = row[0]
            
            precio = row[1]
            
            if nombre == fruta:
                
                print(f'el precio de la {fruta} es: {precio}')
                
                encontrada = True
    
    if not encontrada:
        
        print('La fruta que ingresaste no se encuentra en la lista')
    
    f.close()

buscar_precio(str(input('Ingresa el nombre de la fruta que desea buscar: ')).capitalize())