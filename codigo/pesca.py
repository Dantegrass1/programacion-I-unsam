import csv

# ---------- FUNCION PRINCIPAL ----------
def informe(nombre_archivo, especie=None, anio=None):

    datos = []

    # -------- LEER ARCHIVO --------
    try:
        archivo = open(nombre_archivo, encoding="utf-8")
        lector = csv.DictReader(archivo)

        for fila in lector:
            # convierto los datos a tipos correctos
            registro = {
                "anio": int(fila["anio"]),
                "especie": fila["especie"],
                "cantidad": int(fila["cantidad"])
            }
            datos.append(registro)

        archivo.close()

    except:
        print("Error al leer el archivo")
        return

    # -------- FILTRAR DATOS --------
    filtrados = []

    for d in datos:
        # si se pidió especie, filtro
        if especie != None and d["especie"] != especie:
            continue

        # si se pidió año, filtro
        if anio != None and d["anio"] != anio:
            continue

        filtrados.append(d)

    # -------- TOTAL --------
    total = 0
    for d in filtrados:
        total += d["cantidad"]

    # -------- ACUMULAR POR ESPECIE Y AÑO --------
    por_especie = {}
    por_anio = {}

    for d in filtrados:
        esp = d["especie"]
        a = d["anio"]

        # acumulo por especie
        if esp in por_especie:
            por_especie[esp] += d["cantidad"]
        else:
            por_especie[esp] = d["cantidad"]

        # acumulo por año
        if a in por_anio:
            por_anio[a] += d["cantidad"]
        else:
            por_anio[a] = d["cantidad"]

    # -------- BUSCAR MAX Y MIN --------
    esp_max = None
    esp_min = None

    for esp in por_especie:
        if esp_max == None or por_especie[esp] > por_especie[esp_max]:
            esp_max = esp
        if esp_min == None or por_especie[esp] < por_especie[esp_min]:
            esp_min = esp

    anio_max = None
    anio_min = None

    for a in por_anio:
        if anio_max == None or por_anio[a] > por_anio[anio_max]:
            anio_max = a
        if anio_min == None or por_anio[a] < por_anio[anio_min]:
            anio_min = a

    # -------- ESPECIES EN TODOS LOS AÑOS --------
    especies_todas = []

    # lista de años únicos
    anios = []
    for d in datos:
        if d["anio"] not in anios:
            anios.append(d["anio"])

    # lista de especies únicas
    especies = []
    for d in datos:
        if d["especie"] not in especies:
            especies.append(d["especie"])

    # chequeo si cada especie aparece en todos los años
    for esp in especies:
        aparece_en_todos = True

        for a in anios:
            aparece = False

            for d in datos:
                if d["anio"] == a and d["especie"] == esp:
                    aparece = True

            if not aparece:
                aparece_en_todos = False

        if aparece_en_todos:
            especies_todas.append(esp)

    # -------- ESPECIES ÚNICAS --------
    conteo = {}
    especies_unicas = []

    for d in datos:
        esp = d["especie"]

        if esp in conteo:
            conteo[esp] += 1
        else:
            conteo[esp] = 1

    for esp in conteo:
        if conteo[esp] == 1:
            especies_unicas.append(esp)

    # -------- IMPRESIÓN --------
    print("\n--- INFORME DE PESCA ---\n")

    print("Total pescado:", total)

    if len(filtrados) > 0:
        print("Especie más pescada:", esp_max)
        print("Especie menos pescada:", esp_min)
        print("Año con más pesca:", anio_max)
        print("Año con menos pesca:", anio_min)

    print("\nEspecies en todos los años:")
    print(especies_todas)

    print("\nEspecies que aparecen una sola vez:")
    print(especies_unicas)


# ---------- EJECUCIÓN ----------
archivo = "pesca.csv"

# podés probar distintas variantes:
informe(archivo)
# informe(archivo, especie="Merluza")
# informe(archivo, anio=2015)