# asingo valor inicial de altura
altura_pelota = 100
#asigno valor de rebote
rebote = 3/5
#inicio la variable de saltos en 0
saltos=0
#Creo el bucle para que actualice la variable de altura y saltos, simulando un salto de pelota, hasta que llegue a los 10 saltos.
while saltos < 10: #mientras que saltos sea menor a 10...
    altura_pelota = altura_pelota * rebote #multiplica la altura por el valor del rebote
    saltos = saltos + 1 #agrega cantidad de saltos cada vez que la condicion se cumple.
    print (saltos, 'altura: ', altura_pelota) #muestra la lista de saltos

#Corre Correctamente :)
#Dante Grassi, Programacion I, Lic. Ciencia de Datos.

'''
output:
1 altura:  60.0
2 altura:  36.0
3 altura:  21.599999999999998
4 altura:  12.959999999999999
5 altura:  7.775999999999999
6 altura:  4.6655999999999995
7 altura:  2.7993599999999996
8 altura:  1.6796159999999998
9 altura:  1.0077695999999998
10 altura:  0.6046617599999998
'''
