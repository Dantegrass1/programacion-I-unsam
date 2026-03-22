def buscar_precio(fruta): #defino funcion con una variable dentro
    f = open('codigo/data/precios.csv', 'rt') #funcion para abrir dataset (modo lectura), guardandolo en la variable f.
    
    encontrada = False #inicio variable encontrada para mas tarde, en False.
    
    for line in f: #por cada fila del dataset
        
        row = line.split(',') # separa los datos por la coma.
        
        if len(row) >= 2: #define un minimo de datos para cada fila, en este caso tiene que tener dos datos cada fila.
            
            nombre = row[0] #guarda el primer dato de cada fila como nombre. NOTA!: estas dos variables se actualizan constantemente por cada fila. Si quisiera guardar todas las frutas en la misma variable, tendria que hacer una lista con ese msimo valor.
            
            precio = row[1] #guarda el segundo dato de cada fila como precio
            
            if nombre == fruta: #busca la fruta ingresada en el dataset
                
                print(f'el precio de la {fruta} es: {precio}') #Muestro el valor precio de la fruta buscada
                
                encontrada = True #guarda la variable para terminar el proceso.
    
    if not encontrada: #si la variable es False, ejecuta...
        
        print('La fruta que ingresaste no se encuentra en la lista')#aviso
    
    f.close()#Cierra el dataset.

buscar_precio(str(input('Ingresa el nombre de la fruta que desea buscar: ')).capitalize())#buscar una fruta especifica ingresada por el usuario, capitalize y str para manejo de errores de sintaxis.

#Fin. Dante Grassi. Ejercicio 2.7, Prog I.