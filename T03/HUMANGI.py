import Funciones as func
import datetime
from Fenotipo import fenotipos, genotipos
from functools import reduce
import collections
from Lectura import todos, datos
from Excepciones import *

# aca genero la excepcion GenomeError en caso de existir
e = list(filter(lambda x: func.trygenoma(x) == False, datos))
if len(e) != 0:
    raise GenomeError


def ascendencia(persona):
    ascendencia = []
    if func.tratar(fenotipos, persona):
        print(fenotipos[persona]['Nariz'])
        if fenotipos[persona]["Pelo"] == "Negro" and "Pecho" in fenotipos[
                persona]["Vello"] and fenotipos[persona]["Nariz"] == "Recta":
            ascendencia.append("Mediterranea")
        elif fenotipos[persona]["Piel"] == "Negra" and fenotipos[persona][
            "Pelo"] == "Negro" and fenotipos[persona]["Pies"] > 44:
            ascendencia.append("Africana")
        elif fenotipos[persona]["Guata"] == "Guatón Parrillero" and \
                "Espalda" in fenotipos[persona]["Vello"]:
            ascendencia.append("Estadounidense")
        elif "AAT" in genotipos[persona]["Ojos"] and "AAT" in genotipos[
                persona]["Pelo"] and "AAT" in genotipos[persona]["Piel"]:
                ascendencia.append("Albino")
    else:
        raise NotFound
    return ascendencia


def indice_de_tamano(persona):
    if func.tratar(genotipos, persona):
        guata = list(filter(lambda x: x == "AGT", genotipos[persona]["Guata"]))
        altura = list(filter(lambda x: x == "AGT", genotipos[persona]["Altura"]))
        porcentaje_guata = len(guata) / len(genotipos[persona]["Guata"])
        porcentaje_altura = len(altura) / len(genotipos[persona]["Altura"])
        return [(porcentaje_altura * porcentaje_guata) ** 0.5]
    else:
        raise NotFound


# parentezcos
def pariente_de(grado, persona):
    if func.tratar(fenotipos, persona):
        if grado == 1:
            return func.parienteg1(persona, fenotipos)
        elif grado == 0:
            return func.parienteigual(persona, fenotipos)
        elif grado == 2:
            return func.parienteg2(persona, fenotipos)
        elif grado == "n":
            return func.parienten(persona, fenotipos)
        elif grado == -1:
            return func.parientedistinto(persona, fenotipos)
    else:
        raise NotFound

# revisar lo de los repetidos :S
def gemelo_identico(persona):
    if func.tratar(genotipos, persona):
        listas = list(zip(func.gemelo_ojos(persona, genotipos),
                     func.gemelo_pelo(persona, genotipos),
                     func.gemelo_nariz(persona, genotipos),
                     func.gemelo_altura(persona, genotipos),
                     func.gemelo_pies(persona, genotipos),
                     func.gemelo_piel(persona, genotipos),
                     func.gemelo_guata(persona, genotipos),
                     func.gemelo_vello(persona, genotipos),
                     func.gemelo_vision(persona, genotipos)))
        totales = [[reduce(lambda x, y: x + y, listas[x])] for x in range(
            len(listas))]
        return todos[totales.index(max(totales))]
    else:
        raise NotFound


l1 = ["Altura", "Ojos", "Pelo", "Piel", "Nariz", "Pies", "Vello", "Guata",
      "Problemas"]
l2 = ["AAG", "GTC", "GGA", "TCT", "GTA", "CTC", "CGA", "TGG", "TAG"]


def valor_caracteristica(tag, persona):
    if func.tratar(fenotipos, persona) and func.tratar2(fenotipos, tag,
                                                        persona):
        return fenotipos[persona][l1[l2.index(tag)]]
    else:
        raise NotFound


# consultas estadisticas
def minimo(tag):
    if func.tratar2(fenotipos, tag, todos[0]):
        if tag == l2[0] or tag == l2[5]:
            return min(map(lambda x: fenotipos[x][l1[l2.index(tag)]], fenotipos))
        else:
            a = list(map(lambda x: fenotipos[x][l1[l2.index(tag)]], fenotipos))
            b = collections.Counter(a)
            i = list(zip(b.keys(), b.values()))
            r = [x[1] for x in i]
            f = r.index(min(r))
            return i[f][0]
    else:
        raise NotFound


def maximo(tag):
    if func.tratar2(fenotipos, tag, todos[0]):
        if tag == l2[0] or tag == l2[5]:
            return max(map(lambda x: fenotipos[x][l1[l2.index(tag)]], fenotipos))
        else:
            a = list(map(lambda x: fenotipos[x][l1[l2.index(tag)]], fenotipos))
            b = collections.Counter(a)
            return b.most_common(1)[0][0]
    else:
        raise NotFound

def prom(tag):
    if func.tratar2(fenotipos, tag, todos[0]):
        if tag == "AAG" or tag == "CTC":
            lista = (fenotipos[i][l1[l2.index(tag)]] for i in fenotipos)
            valores = map(lambda x: x, lista)
            acum = reduce(lambda x, y: x + y, valores)
            return int(acum) / len(fenotipos)
        else:
            raise NotFound
    else:
        raise NotFound


# definimos unas funciones para levantar las excepciones

lisac = ["ascendencia","índice_de_tamaño","pariente_de","gemelo_genético",
         "valor_característica", "min", "max", "prom"]
def bad(accion):
    if accion not in lisac:
        raise BadRequest

def notf(accion, nombre, cosa):
    if accion == lisac[0] or accion == lisac[1] or accion == lisac[2] or \
            accion == lisac[3]:
        try:
            a = fenotipos[nombre][cosa]
        except KeyError:
            raise NotFound

def nota(nombre):
    if len(ascendencia(nombre)) == 0:

        raise NotAcceptable

def geno(genoma):
    l = "TACG"
    e = [x if x not in l else "" for x in genoma]
    if len(e) != 0:
        raise GenomeError
