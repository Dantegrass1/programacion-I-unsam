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

#Si, anda bien en todos los casos de prueba.

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

def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")