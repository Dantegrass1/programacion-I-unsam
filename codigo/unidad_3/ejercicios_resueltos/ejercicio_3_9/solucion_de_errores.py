#3.5
'''
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1
    return i
'''
#i = tiene_a('La novela 1984 de George Orwell')
#tiene_a('abracadabra')
#tiene_a('La novela 1984 de George Orwell')
#print(i)

#El error de semantica aca se debe a que el programa busca devolver el valor de i, pero no lo hace.

#3.6
'''
def tiene_a(expresion)
    n = len(expresion)
    i = 0
    while i<n
        if expresion[i] = 'a'
            return True
        i += 1
    return Falso

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')
'''
#En este programa anda mal en ambos casos de prueba, ya que el programa esta mal escrito(error de sintaxis.)

#3.7
'''
def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)
'''
#En este caso, el ultimo(1984) Da error de tipo traceback TypeError: Int object of type int has no len(), que se refiera a que la entrada de dato entero no se puede usar con la funcion len, hecha para leer una cadena.



#3.8
'''
def suma(a,b):
    c = a + b
    #return c

a = 2
b = 3
c = suma(a,b)
'''
#print(f"La suma da {a} + {b} = {c}")

#El error aca tambien es de semantica, ya que el programa funciona, pero no de forma correcta. Devuelve NONE como C, ya que dentro de la funcion, la variable no se retorna(return), por lo que queda "atrapada" dentro de suma.

#3.9

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    #registro={} #ESTO ESTA MAL UBICADO(PROBLEMA)
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={} #Asi se soluciona. AHORA HACE UN DICCIONARIO POR CADA FILA
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro) #ACA ESTA EL PROBLEMA, YA QUE ANTES HACIA UN MISMO DICCIONARIO, DONDE LOOPEABA Y AGREGABA LA ULTIMA FILA (CUANDO TERMINABA DE RECORRER EL DATASET, POR LO QUE AGREGABA CADA FILA AL DICCIONARIO, PERO SIEMPRE SE ACTUALIZABA CON LA ULTIMA,Y LUEGO SE GUARDABA EN CAMION)
    return camion

camion = leer_camion('/mnt/d/programacion-I-unsam/codigo/data/camion.csv')
pprint(camion)

#El problema es que solo guarda la ultima fila dentro del diccionario.