import os
from csv import reader
"""
ACORDARSE DE DEFINIR TODAS LAS FUNCIONES :)
"""


def orden(file):
    """Esta funcion la use para identificar en que orden estan las columnas

    :param file: archivo .csv a leer
    :type file: str

    :return: lista con la primera fila
    :rtype: List
    """
    if not os.path.exists(file):
        raise FileNotFoundError('No existe el archivo ' + str(file))

    with open(file, 'r', encoding='utf-8') as data:
        order = data.readline()
        order = order.strip().split(';')
        fila = []
        for i in order:
            if i[0] == " ":
                i = i[1:]
            fila.append(i)
    return fila


def read_file(archivo):
    """Funcion que lee un archivo.csv
    :param archivo: archivo .csv a leer
    :type archivo: str

    :return: lista con todas las lineas
    :rtype: List
    """
    if not os.path.exists(archivo):
        raise FileNotFoundError('No existe el archivo ' + str(archivo))
    lista = []
    with open(archivo, 'r', encoding='utf-8') as file:
        file.readline()
        for line in file:
            line = line.strip().replace('\ufeff', '').split(';')
            for elem in range(len(line)):
                line[elem] = line[elem].strip()
            lista.append(line)
    return lista


def leer_parametros(archivo):
    """Funcion que lee parametros

    archivo es str del nombre del csv a leer
    retorna un diccionario con los parametros

    """
    with open(archivo, 'r', encoding='utf-8') as para:
        i = 0
        for algo in para:
            if i == 0:
                keys = algo.strip().split(',')
                for elem in range(len(keys)):
                    keys[elem] = keys[elem].strip()
                i += 1
            else:
                values = algo.split(',')
        parametros = {keys[i]: values[i] for i in range(len(keys))}
    return parametros

def leer_escenario(archivo):
    """
    funcion que lee el archivo escenarios y crea diccionarios con datos
    :param archivo: str nombre archivo
    :return: dict con datos escenarios
    """
    orden_e = orden(archivo)
    lineas = []
    with open(archivo, 'r', encoding='utf-8') as file:
        file.readline()
        for line in file:
            line = line.strip().replace('\ufeff', '').split(',')
            for elem in range(len(line)):
                line[elem] = line[elem].strip()
            lineas.append(line)

    ordenf = orden_e[0].split(',')
    ordenf.remove('escenario')

    fila = []
    for i in ordenf:
        if i[0] == " ":
            i = i[1:]
        fila.append(i)

    ordenf = fila

    escenarios = {}
    for line in lineas:
        a = line[0]
        line = line[1:]
        esce = {ordenf[i]: line[i] for i in range(len(ordenf))}
        escenarios[int(a)] = esce
    return escenarios






