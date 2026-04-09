import csv


def leer_ventas(nombre_archivo):
    """
    Lee un archivo CSV y devuelve una lista de diccionarios
    con las ventas.
    """

    ventas = []

    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                try:
                    venta = {
                        'titulo': fila['titulo'],
                        'genero': fila['genero'],
                        'precio': float(fila['precio']),
                        'cantidad': int(fila['cantidad'])
                    }
                    ventas.append(venta)

                except ValueError:
                    print("Error en datos numéricos:", fila)

                except KeyError:
                    print("Faltan columnas:", fila)

    except FileNotFoundError:
        print("Error: no se encontró el archivo.")
        return []

    return ventas


def ingresos_por_genero(ventas):
    """
    Calcula los ingresos totales por género.
    """

    ingresos = {}

    for venta in ventas:
        genero = venta['genero']
        ingreso = venta['precio'] * venta['cantidad']

        if genero in ingresos:
            ingresos[genero] += ingreso
        else:
            ingresos[genero] = ingreso

    return ingresos


def generar_informe(nombre_archivo):
    """
    Genera e imprime el informe de ventas.
    """

    ventas = leer_ventas(nombre_archivo)

    if len(ventas) == 0:
        print("No hay datos para procesar.")
        return

    ingresos = ingresos_por_genero(ventas)

    print("\nIngresos por género:\n")

    total = 0

    for genero in ingresos:
        monto = ingresos[genero]
        print(f"{genero}: ${monto:.2f}")
        total += monto

    print(f"\nIngreso total: ${total:.2f}")


# 🔹 EJECUCIÓN DIRECTA (sin terminal)
# Cambiás el nombre del archivo acá directamente

nombre_archivo = "ventas.csv"
generar_informe(nombre_archivo)