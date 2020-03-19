import requests


def corona(UCountry=None,
           UConfirmed=None,
           URecovered=None,
           UDeaths=None,
           UActive=None,
           UMortality=None,
           URecoveredp=None,
           UDay=None,
           UWeek=None,
           llave=None):

    resp = requests.get('https://corona-stats.online/')
    tabla = resp.text

    # elimino caracteres molestos
    tabla = tabla.replace("╔", "")
    tabla = tabla.replace("═", "")
    tabla = tabla.replace("╗", "")
    tabla = tabla.replace("║", "")
    tabla = tabla.replace(" ", "")
    tabla = tabla.replace("─", "")
    tabla = tabla.replace("╢", "")
    tabla = tabla.replace("╟", "")
    tabla = tabla.replace("┼", "")
    tabla = tabla.replace("╚", "")
    tabla = tabla.replace("╧", "")
    tabla = tabla.replace("╝", "")
    tabla = tabla.replace("╤", "")
    tabla = tabla.replace(",The", "")
    tabla = tabla.replace("▲", "")
    tabla = tabla.replace("\n\n", "│\n│")

    casilleros = []
    lista = [[]]
    n = 0

    Country = {}
    Confirmed = {}
    Recovered = {}
    Deaths = {}
    Active = {}
    Mortality = {}
    Recoveredp = {}
    Day = {}
    Week = {}

    # itero cada casillero
    for num in range(tabla.count("│")):

        # creo una lista con cada casillero del cuadro
        casilleros.append(tabla[:tabla.index("│")])

        # saco las abreviaciones de los paises
        if "(" in casilleros[num]:
            casilleros[num] = casilleros[num][:casilleros[num].index("(")]

        # elimino de la tabla los casilleros ya guardados en la lista
        tabla = tabla[tabla.index("│")+1:]

        # separo la lista en filas con una lista de listas
        if casilleros[num] != "\n":
            lista[n].append(casilleros[num])
        else:
            lista.append([])
            n += 1

    # Elimino listas vacias y los links y comentarios al final del texto
    while lista.count([]):
        lista.remove([])
    lista.pop(0)
    lista.pop(-1)
    lista.pop(-1)
    lista.pop(-1)

    # Por cada atributo creo un diccionario con el numero como llave
    # y el valor del atributo como valor
    for element in lista:

        Country[element[0]] = element[1]
        Confirmed[element[0]] = element[2]
        Recovered[element[0]] = element[3]
        Deaths[element[0]] = element[4]
        Active[element[0]] = element[5]
        Mortality[element[0]] = element[6]
        Recoveredp[element[0]] = element[7]
        Day[element[0]] = element[8]
        Week[element[0]] = element[9]

    # Busco la llave en cada diccionario dependiendo del valor buscado
    for key, value in Country.items():
        if UCountry == value:
            llave = key
    for key, value in Confirmed.items():
        if UConfirmed == value:
            llave = key
    for key, value in Recovered.items():
        if URecovered == value:
            llave = key
    for key, value in Deaths.items():
        if UDeaths == value:
            llave = key
    for key, value in Active.items():
        if UActive == value:
            llave = key
    for key, value in Mortality.items():
        if UMortality == value:
            llave = key
    for key, value in Recoveredp.items():
        if URecoveredp == value:
            llave = key
    for key, value in Day.items():
        if UDay == value:
            llave = key
    for key, value in Week.items():
        if UWeek == value:
            llave = key

    # Devuelvo los valores de cada atributo para el valor buscado
    if llave:
        return (llave,
                Country[llave],
                Confirmed[llave],
                Recovered[llave],
                Deaths[llave],
                Active[llave],
                Mortality[llave],
                Recoveredp[llave],
                Day[llave],
                Week[llave])


print(corona("Argentina"))

print(corona(URecovered="3"))

print(corona(llave="18"))
