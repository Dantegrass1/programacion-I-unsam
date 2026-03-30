precios = {
    'Pera' : 490.1,
    'Lima' : 23.45,
    'Naranja' : 91.1,
    'Mandarina' : 34.23
}

print(precios.items())

lista_precios = list(zip(precios.values(), precios.keys()))

print(lista_precios)

print(min(lista_precios),max(lista_precios), sorted(lista_precios))

a = [1, 2, 3, 4]
b = ['w', 'x', 'y', 'z']
c = [0.2, 0.4, 0.6, 0.8]
print(list(zip(a, b, c)))

a = [1, 2, 3, 4, 5, 6]
b = ['x', 'y', 'z']
print(list(zip(a,b)))

camion = [
    ('Pera', 100, 490.1),
    ('Naranja', 50, 91.1),
    ('Caqui', 150, 83.44),
    ('Naranja', 100, 45.23),
    ('Pera', 75, 572.45),
    ('Lima', 50, 23.15)
]

from collections import Counter

total_cajones = Counter()

for nombre, n_cajones, precio in camion:
    total_cajones[nombre] += n_cajones

print(total_cajones['Naranja'])

