
'''
a = 'Hello'               # String o cadena
b = [1, 4, 5]             # Lista
c = ('Pera', 100, 490.1)  # Tupla

# Orden indexado
a[0]                      # 'H'
b[-1]                     # 5
c[1]                      # 100

# Longitud de secuencias
len(a)                    # 5
len(b)                    # 3
len(c)                    # 3

a = 'Hello'
a * 3
'HelloHelloHello'
b = [1, 2, 3]
b * 2
[1, 2, 3, 1, 2, 3]

a = (1, 2, 3)
b = (4, 5)
a + b
(1, 2, 3, 4, 5)

c = [1, 5]
a + c
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: can only concatenate tuple (not "list") to tuple

a = [0,1,2,3,4,5,6,7,8]

a[2:5]    # [2,3,4]
a[-5:]    # [4,5,6,7,8]
a[:3]     # [0,1,2]



# Reasignación
a = [0,1,2,3,4,5,6,7,8]
a[2:4] = [10,11,12]       # [0,1,10,11,12,4,5,6,7,8]


# Eliminación
a = [0,1,2,3,4,5,6,7,8]
del a[2:4]                # [0,1,4,5,6,7,8]


s = [1, 2, 3, 4]
sum(s)
#10
min(s)
#1
max(s)
#4
t = ['Hello', 'World']
max(t)
#'World'

'''

s = [1, 4, 9, 16]
for i in s:
    print(i)
#1
#4
#9
#16

'''
for x in s:         # `x` es una variable iteradora
'''
"""
for name in namelist:
    if name == 'Juana':
        break

for line in lines:
    if line == '\n':    # Salteo las instrucciones que procesan líneas
        continue
    # Instrucciones que procesan líneas

'''for i in range(100):'''
    # i = 0,1,...,99

"""

lista = [0, 2, 4, "Hola"]

a = sum(lista[0:3]) + 1

print(a)
print(lista.index)
"""
for i in range(100):
    # i = 0,1,...,99
for j in range(10,20):
    # j = 10,11,..., 19
for k in range(10,50,2):
    # k = 10,12,...,48
    # Observá que va de a dos.
"""
"""
nombres = ['Edmundo', 'Juana', 'Rosita']
for i, nombre in enumerate(nombres):
    # i = 0, nombre = 'Edmundo'
    # i = 1, nombre = 'Juana'
    # i = 2, nombre = 'Rosita'
"""
"""
with open(nombre_archivo) as f:
    for nlinea, line in enumerate(f, start=1):
        ...

i = 0
for x in s:
    instrucciones
    i += 1
"""



"""
nombres = ['Edmundo', 'Juana', 'Rosita']
for i, nombre in enumerate(nombres):
"""
"""
points = [
  (1, 4),(10, 40),(23, 14),(5, 6),(7, 8)
]
for x, y in points:
    #   x = 1, y = 4
    #   x = 10, y = 40
    #   x = 23, y = 14
    ...

columnas = ['nombre', 'cajones', 'precio']
valores = ['Pera', 100, 490.1 ]
pares = zip(columnas, valores)
# ('nombre','Pera'), ('cajones',100), ('precio',490.1)

for columna, valor in pares:
    ...
"""

d = dict(zip(["Nombre"], ["Juan"]))

print(d)
