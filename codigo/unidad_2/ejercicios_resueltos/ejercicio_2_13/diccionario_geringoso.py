#Version 1.18

cadena = 'Geringoso' #cadena a convertir
capadepenapa = '' #cadena convertida
for c in cadena: #bucle para recorrer la cadena
    if c in 'aeiou': #recorre cada letra de la cadena y si es una vocal:
        capadepenapa += c + 'p' + c #agrega a la variable capadepenapa la letra de la cadena, la letra 'p' y la letra de la cadena nuevamente
    else: #si no es una vocal, agrega a la variable capadepenapa la letra de la cadena sola
        capadepenapa += c #agrega a la variable capadepenapa la letra de la cadena sola
print(capadepenapa) #imprime la cadena convertida

#Corre Correctamente :)
#Dante Grassi, Programacion I, Lic. Ciencia de Datos.

'''
output:
Geperipingoposopo
'''

#Version 2.13

diccionario = {} #Crea un diccionario

def diccionario_geringoso(lista): #Crea la funcion y se ejecuta con la variable lista

    for palabra in lista: #Por cada palabra en la lista

        palabra = palabra.capitalize()

        palabra_g = '' #crea una variable que se reinicie a vacio para cada palabra

        for c in palabra: #para cada letra en la palabra

            if c in 'aeiou': #Analiza si tiene vocal

                palabra_g += c + 'p' + c  #agrega si es vocal

            else: #contrario

                palabra_g += c 

        diccionario[palabra] = palabra_g #agrega la palabra geringosa y la palabra como clave y valor al diccionario

diccionario_geringoso(input('Ingresa palabras separadas por espacio EJ:Manzana Banana Mandarina...: ').split()) #ejecuta la funcion con una lista

print(diccionario) #muestra el diccionario

#Fin. Dante Grassi, Lic. Ciencia de Datos, UNSAM. Programacion I.