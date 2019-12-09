from functools import reduce

# MAXIMO 15 LINEAS POR FUNCION
l1 = ["Altura", "Ojos", "Pelo", "Piel", "Nariz", "Pies", "Vello", "Guata",
      "Problemas"]
l2 = ["AAG", "GTC", "GGA", "TCT", "GTA", "CTC", "CGA", "TGG", "TAG"]
# esta funcion retorna el numero de espacios que se debe saltar para cortar
# el string
def salto(datos, tipo):
    if datos[retorna(datos, tipo) + 5].isdigit():
        return 6
    elif datos[retorna(datos, tipo) + 4].isdigit():
        return 5
    else:
        return 4

# esta funcion se usa para acortar strings
def acortar(datos, tipo):
    return [str(datos[i][0:retorna(datos[i], tipo)]) + str(datos[i][retorna(
        datos[i], tipo) + int(salto(datos[i], tipo)):]) for i in range(len(
            datos))]

# retorna la posicion del tipo en el string
def retorna(string, tipo):
    lista = [str(i) for i in range(len(string)-2)if str(string[i]+string[
        i+1]+string[i+2]) == tipo]
    return int(lista[0])

# retorna una lista por compresion de los datos
def rellenar(datos, tipo):
    return list(map(lambda i: datos[i][retorna(datos[i], tipo) + 3:retorna(
        datos[i], tipo) + 6] if datos[i][retorna(datos[i], tipo) + 5].isdigit()
            else datos[i][retorna(datos[i], tipo) + 3:retorna(datos[i], tipo)
            + 5] if datos[i][retorna(datos[i], tipo) + 4].isdigit() else
            datos[i][retorna(datos[i], tipo) + 3:retorna(datos[i], tipo) +
            4], range(len(datos))))

def atributos(listas, numero, diccionario):
    a = diccionario[int(numero)]
    if a == ['']:
        return []
    return [listas[int(i)] for i in a]

# las funciones de aca abajo son para ver que fenotipo tiene la persona
# debido a sus genes
def ojos(genotipos):
    if genotipos["Ojos"] == []:
        return "No tiene fenotipo"
    if "CCT" in genotipos["Ojos"]:
        return "Cafes"
    elif "AAT" in genotipos["Ojos"]:
        return "Azules"
    else:
        return "Verde"

def pelo(genotipos):
    if genotipos["Pelo"] == []:
        return "No tiene fenotipo"
    if "GTG" in genotipos["Pelo"]:
        return "Negro"
    elif "AAT" in genotipos["Pelo"]:
        return "Rubio"
    else:
        return "Pelirrojo"

def nariz(genotipos):
    if genotipos["Nariz"] == []:
        return "No tiene fenotipo"
    if "TCG" in genotipos["Nariz"]:
        return "Aguileña"
    elif "CAG" in genotipos["Nariz"]:
        return "Respingada"
    else:
        return "Recta"

def pies(genotipos):
    if genotipos["Pies"] == []:
        return "No tiene fenotipo"
    max = list(filter(lambda x: x == "GTA", genotipos["Pies"]))
    min = list(filter(lambda x: x == "CCA", genotipos["Pies"]))
    return (len(max) * 48 + len(min) * 34) / len(genotipos["Pies"])

def altura(genotipos):
    if genotipos["Altura"] == []:
        return "No tiene fenotipo"
    max = list(filter(lambda x: x == "AGT", genotipos["Altura"]))
    min = list(filter(lambda x: x == "ACT", genotipos["Altura"]))
    return (len(max) * 2.1 + len(min) * 1.4) / len(genotipos["Altura"])

def guata(genotipos):
    if genotipos["Guata"] == []:
        return "No tiene fenotipo"
    gen1 = list(filter(lambda x: x == "ACT", genotipos["Guata"]))
    porcentaje = len(gen1)/len(genotipos["Guata"]) * 100
    if porcentaje < 24.999:
        return "Guatón Parrillero"
    elif porcentaje < 49.999:
        return "Mañana empiezo la dieta"
    elif porcentaje < 74.999:
        return "Atleta"
    else:
        return "Modelo"

def piel(genotipos):
    if genotipos["Piel"] == []:
        return "No tiene fenotipo"
    gen1 = list(filter(lambda x: x == "AAT", genotipos["Piel"]))
    porcentaje = len(gen1) / len(genotipos["Piel"]) * 100
    if porcentaje < 24.999:
        return "Negro"
    elif porcentaje < 49.999:
        return "Moreno"
    elif porcentaje < 74.999:
        return "Blanco"
    else:
        return "Albino"

def vello(genotipos):
    if genotipos["Vello"] == []:
        return "No tiene fenotipo"
    op1 = list(filter(lambda x: x == "TGC", genotipos["Vello"]))
    op2 = list(filter(lambda x: x == "GTG", genotipos["Vello"]))
    op3 = list(filter(lambda x: x == "CCT", genotipos["Vello"]))
    retu = []
    if len(op1)/len(genotipos["Vello"]) * 100 >= 20:
        retu.append("Pecho")
    if len(op2)/len(genotipos["Vello"]) * 100 >= 20:
        retu.append("Axila")
    if len(op3)/len(genotipos["Vello"]) * 100 >= 20:
        retu.append("Espalda")
    return retu

def problemas(genotipos):
    if genotipos["Problemas"] == []:
        return "No tiene fenotipo"
    op1 = list(filter(lambda x: x == "TTC", genotipos["Problemas"]))
    op2 = list(filter(lambda x: x == "ATT", genotipos["Problemas"]))
    retu = []
    if len(op1) / len(genotipos["Problemas"]) * 100 > 20:
        retu.append("Daltonismo")
    if len(op2) / len(genotipos["Problemas"]) * 100 > 20:
        retu.append("Miopia")
    return retu

def diferencia_guata(l):
    if "Modelo" in l and "Atleta" in l or "Atleta" in l and "Mañana empiezo " \
        "la dieta" in l or "Mañana empiezo la dieta" in l and "Guatón " \
         "Parrillero" in l or l[0] == l[1]:
        return True
    else:
        return False

def parienteigual(persona, fenotipos):
    return list(filter(lambda x: fenotipos[x] == fenotipos[persona] and x !=
            persona, fenotipos))

def parientedistinto(persona, fenotipos):
    return list(filter(lambda x: fenotipos[x] != fenotipos[persona] and x !=
            persona, fenotipos))

a = "Altura"
b = "Ojos"
c = "Pelo"
d = "Piel"
e = "Nariz"
f = "Pies"
g = "Vello"
h = "Guata"
i = "Problemas"

def parienteg1(persona, fenotipos):
    return list(filter(lambda x: abs(fenotipos[x][a] - fenotipos[persona][
        a]) <= 20 and fenotipos[x][b] == fenotipos[persona][b] and fenotipos[
        x][c] == fenotipos[persona][c] and fenotipos[x][d] == fenotipos[
        persona][d] and fenotipos[x][e] == fenotipos[persona][e] and fenotipos[
        x][i] == fenotipos[persona][i] and abs(fenotipos[x][f] - fenotipos[
         persona][f]) <= 2 and x != persona, fenotipos))

def parienteg2(persona, fenotipos):
    return list(filter(lambda x: abs(fenotipos[x][a] - fenotipos[persona][
        a]) <= 50 and fenotipos[x][c] == fenotipos[persona][c] and fenotipos[
            x][d] == fenotipos[persona][d] and fenotipos[x][i] == fenotipos[
        persona][i] and abs(fenotipos[x][f] - fenotipos[persona][f]) <= 4
        and x != persona, fenotipos))

def parienten(persona, fenotipos):
    return list(filter(lambda x: abs(fenotipos[x][a] - fenotipos[persona][
        a]) < 70 and fenotipos[x][d] == fenotipos[persona][d] and abs(
        fenotipos[x][f] - fenotipos[persona][f]) <= 6 and x != persona and
        diferencia_guata([fenotipos[persona][h], fenotipos[x][h]]), fenotipos))

def maximo(tag, fenotipos):
    return max(map(lambda x: fenotipos[x][tag], fenotipos))

def gemelo_altura(persona, genotipos):
    return [gemi_altura(persona, x, genotipos) if x != \
            persona else 0 for x in genotipos]

def gemi_altura(persona, persona2, genotipos):
    agt_p1 = len(list(filter(lambda x: x == "AGT", genotipos[persona][
        "Altura"])))
    agt_p2 = len(list(filter(lambda x: x == "AGT", genotipos[persona2][
        "Altura"])))
    agt = min(agt_p1, agt_p2)
    act_p1 = len(list(filter(lambda x: x == "ACT", genotipos[persona][
        "Altura"])))
    act_p2 = len(list(filter(lambda x: x == "ACT", genotipos[persona2][
        "Altura"])))
    act = min(act_p1, act_p2)
    return agt + act

def gemelo_ojos(persona, genotipos):
    return [gemi_ojos(persona, x, genotipos) if x != persona else 0 for x in
            genotipos]

def gemi_ojos(persona, persona2, genotipos):
    cct_p1 = len(list(filter(lambda x: x == "CCT", genotipos[persona][
        "Ojos"])))
    cct_p2 = len(list(filter(lambda x: x == "CCT", genotipos[persona2][
        "Ojos"])))
    cct = min(cct_p1, cct_p2)
    aat_p1 = len(list(filter(lambda x: x == "AAT", genotipos[persona][
        "Ojos"])))
    aat_p2 = len(list(filter(lambda x: x == "AAT", genotipos[persona2][
        "Ojos"])))
    aat = min(aat_p1, aat_p2)
    cag_p1 = len(list(filter(lambda x: x == "CAG", genotipos[persona][
        "Ojos"])))
    cag_p2 = len(list(filter(lambda x: x == "CAG", genotipos[persona2][
        "Ojos"])))
    cag = min(cag_p1, cag_p2)
    return cag + aat + cct

def gemelo_pelo(persona, genotipos):
    return [gemi_pelo(persona, x, genotipos) if x != persona else 0 for x in
            genotipos]

def gemi_pelo(persona, persona2, genotipos):
    cct_p1 = len(list(filter(lambda x: x == "CCT", genotipos[persona][
        "Pelo"])))
    cct_p2 = len(list(filter(lambda x: x == "CCT", genotipos[persona2][
        "Pelo"])))
    cct = min(cct_p1, cct_p2)
    aat_p1 = len(list(filter(lambda x: x == "AAT", genotipos[persona][
        "Pelo"])))
    aat_p2 = len(list(filter(lambda x: x == "AAT", genotipos[persona2][
        "Pelo"])))
    aat = min(aat_p1, aat_p2)
    ctg_p1 = len(list(filter(lambda x: x == "CTG", genotipos[persona][
        "Pelo"])))
    ctg_p2 = len(list(filter(lambda x: x == "CTG", genotipos[persona2][
        "Pelo"])))
    ctg = min(ctg_p1, ctg_p2)
    return ctg + aat + cct

def gemelo_piel(persona, genotipos):
    return [gemi_piel(persona, x, genotipos) if x != persona else 0 for x in
            genotipos]

def gemi_piel(persona, persona2, genotipos):
    aat_p1 = len(list(filter(lambda x: x == "AAT", genotipos[persona][
        "Piel"])))
    aat_p2 = len(list(filter(lambda x: x == "AAT", genotipos[persona2][
        "Piel"])))
    aat = min(aat_p1, aat_p2)
    gcg_p1 = len(list(filter(lambda x: x == "GCG", genotipos[persona][
        "Piel"])))
    gcg_p2 = len(list(filter(lambda x: x == "GCG", genotipos[persona2][
        "Piel"])))
    gcg = min(gcg_p1, gcg_p2)
    return aat + gcg

def gemelo_nariz(persona, genotipos):
    return [gemi_nariz(persona, x, genotipos) if x != persona else 0 for x in
            genotipos]

def gemi_nariz(persona, persona2, genotipos):
    tcg_p1 = len(list(filter(lambda x: x == "TCG", genotipos[persona][
        "Nariz"])))
    tcg_p2 = len(list(filter(lambda x: x == "TCG", genotipos[persona2][
        "Nariz"])))
    tcg = min(tcg_p1, tcg_p2)
    tac_p1 = len(list(filter(lambda x: x == "TAC", genotipos[persona][
        "Nariz"])))
    tac_p2 = len(list(filter(lambda x: x == "TAC", genotipos[persona2][
        "Nariz"])))
    tac = min(tac_p1, tac_p2)
    cag_p1 = len(list(filter(lambda x: x == "CAG", genotipos[persona][
        "Nariz"])))
    cag_p2 = len(list(filter(lambda x: x == "CAG", genotipos[persona2][
        "Nariz"])))
    cag = min(cag_p1, cag_p2)
    return cag + tcg + tac

def gemelo_pies(persona, genotipos):
    return [gemi_pies(persona, x, genotipos) if x != persona else 0 for x in
            genotipos]

def gemi_pies(persona, persona2, genotipos):
    gta_p1 = len(list(filter(lambda x: x == "GTA", genotipos[persona][
        "Pies"])))
    gta_p2 = len(list(filter(lambda x: x == "GTA", genotipos[persona2][
        "Pies"])))
    gta = min(gta_p1, gta_p2)
    cca_p1 = len(list(filter(lambda x: x == "CCA", genotipos[persona][
        "Pies"])))
    cca_p2 = len(list(filter(lambda x: x == "CCA", genotipos[persona2][
         "Pies"])))
    cca = min(cca_p1, cca_p2)
    return gta + cca

def gemelo_vision(persona, genotipos):
    return [gemi_vision(persona, x, genotipos) if x != persona else 0 for x in
            genotipos]

def gemi_vision(persona, persona2, genotipos):
    ttc_p1 = len(list(filter(lambda x: x == "TTC", genotipos[persona][
        "Problemas"])))
    ttc_p2 = len(list(filter(lambda x: x == "TTC", genotipos[persona2][
        "Problemas"])))
    ttc = min(ttc_p1, ttc_p2)
    att_p1 = len(list(filter(lambda x: x == "ATT", genotipos[persona][
        "Problemas"])))
    att_p2 = len(list(filter(lambda x: x == "ATT", genotipos[persona2][
        "Problemas"])))
    att = min(att_p1, att_p2)
    return att + ttc

def gemelo_vello(persona, genotipos):
    return [gemi_vello(persona, x, genotipos) if x != persona else 0 for x in
            genotipos]

def gemi_vello(persona, persona2, genotipos):
    tgc_p1 = len(list(filter(lambda x: x == "TGC", genotipos[persona][
        "Vello"])))
    tgc_p2 = len(list(filter(lambda x: x == "TGC", genotipos[persona2][
        "Vello"])))
    tgc = min(tgc_p1, tgc_p2)
    gtg_p1 = len(list(filter(lambda x: x == "GTG", genotipos[persona][
        "Vello"])))
    gtg_p2 = len(list(filter(lambda x: x == "GTG", genotipos[persona2][
        "Vello"])))
    gtg = min(gtg_p1, gtg_p2)
    cct_p1 = len(list(filter(lambda x: x == "CCT", genotipos[persona][
        "Vello"])))
    cct_p2 = len(list(filter(lambda x: x == "CCT", genotipos[persona2][
        "Vello"])))
    cct = min(cct_p1, cct_p2)
    return tgc + gtg + cct

def gemelo_guata(persona, genotipos):
    return [gemi_guata(persona, x, genotipos) if x != persona else 0 for x in
            genotipos]

def gemi_guata(persona, persona2, genotipos):
    agt_p1 = len(list(filter(lambda x: x == "AGT", genotipos[persona][
        "Guata"])))
    agt_p2 = len(list(filter(lambda x: x == "AGT", genotipos[persona2][
        "Guata"])))
    agt = min(agt_p1, agt_p2)
    act_p1 = len(list(filter(lambda x: x == "ACT", genotipos[persona][
        "Guata"])))
    act_p2 = len(list(filter(lambda x: x == "ACT", genotipos[persona2][
        "Guata"])))
    act = min(act_p1, act_p2)
    return agt + act

def tratar(diccionario, nombre):
    try:
        a = diccionario[nombre]
    except KeyError:
        return False
    return True

def tratar2(diccionario, tag, persona):
    try:
        a = diccionario[persona][l1[l2.index(tag)]]
    except KeyError:
        return False
    if tag not in l2:
        return False
    return True

def trygenoma(lista):
    e = [filter(lambda x: x != "A" and x != "C" and x != "G" and x != "T",
                lista)]
    if len(e) == 0:
        return False
    return True
