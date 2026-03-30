camion = leer_camion('../Data/camion.csv')
from collections import Counter
tenencias = Counter()
for s in camion:
    tenencias[s['nombre']] += s['cajones']
tenencias
Counter({'Caqui': 150, 'Durazno': 95, 'Lima': 100, 'Mandarina': 250, 'Naranja': 150})
