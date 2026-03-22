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
