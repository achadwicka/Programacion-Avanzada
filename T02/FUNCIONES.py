"""
EN ESTE MODULO SE DEFINIRAN LAS FUNCIONES
"""
import CLASES
import random

def leer_archivo(nombre):
    with open(nombre, "r") as algo:
        listal = CLASES.ListaLigada()
        for linea in algo:
            listal.agregar_nodo(linea)

    return listal

def crear_lista_numeros(nombre):
    with open(nombre, "r") as algo:
        listal = CLASES.ListaLigada()
        for linea in algo:
            cosa = str(linea)
            linea = cosa[7:]
            linea = str(int(linea))
            listal.agregar_nodo(linea)
    return listal

# esta funcion revisa que se puedan poner las piezas (R con R..)
def revisar_bordes(i, j, pieza, f1, f2, f3, f4, f5, f6, f7, f8, posiciones):
    for coordenadas in posiciones:
        if coordenadas.valor == str(i)+str(j):
            print("Lo lamento, esa posicion ya esta usada")
            return False
    p1 = pieza[0]
    p2 = pieza[1]
    p3 = pieza[2]
    p4 = pieza[3]
    p5 = pieza[4]
    p6 = pieza[5]
    fila1 = f1
    fila2 = f2
    fila3 = f3
    fila4 = f4
    fila5 = f5
    fila6 = f6
    fila7 = f7
    fila8 = f8
    x = 1
    y = 1
    w = 1
    z = 1
    if i == 0:
        fila = fila1
        siguiente = fila2
        anterior = ""
        y = 0
    elif i == 1:
        fila = fila2
        siguiente = fila3
        anterior = fila1
    elif i == 2:
        fila = fila3
        siguiente = fila4
        anterior = fila2
    elif i == 3:
        fila = fila4
        siguiente = fila5
        anterior = fila3
    elif i == 4:
        fila = fila5
        siguiente = fila6
        anterior = fila4
    elif i == 5:
        fila = fila6
        siguiente = fila7
        anterior = fila5
    elif i == 6:
        fila = fila7
        siguiente = fila8
        anterior = fila6
    else:
        fila = fila8
        siguiente = ""
        anterior = fila7
        z = 0
    if j == 0:
        cola = ""
        w = 0
        cols = 1
    elif j == 7:
        x = 0
        cola = 6
        cols = ""
    if j != 0 and j != 7:
        cola = j-1
        cols = j+1
    #tengo fila ant sig act cola y cols
    if j%2 != 0:

        # es impar
        # aca primero en el caso q no tenga bordes
        if x == 1 and w == 1 and y == 1 and z == 1:
            a = 0
            if anterior.obtener(cola) == "":
                a += 1
                ar_i = p6
            else:
                ar_i = anterior.obtener(cola)[2]
            if anterior.obtener(j) == "":
                a += 1
                ar = p1
            else:
                ar = anterior.obtener(j)[3]
            if anterior.obtener(cols) == "":
                a += 1
                ar_d = p2
            else:
                ar_d = anterior.obtener(cols)[4]
            if fila.obtener(cola) == "":
                a += 1
                ab_i = p5
            else:
                ab_i = fila.obtener(cola)[1]
            if fila.obtener(cols) == "":
                a += 1
                ab_d = p3
            else:
                ab_d = fila.obtener(cols)[5]
            if siguiente.obtener(j) == "":
                a += 1
                ab = p4
            else:
                ab = siguiente.obtener(j)[0]
            if ar_i != p6 or ar != p1 or ar_d != p2 or ab_i != p5 or ab != \
                    p4 or ab_d != p3 or a == 6:
                return False
            else:
                return True

        # caso que tenga borde a la derecha
        elif w == 1 and y == 1 and z == 1 and x == 0:
            a = 0
            if anterior.obtener(cola) == "":
                a += 1
                ar_i = p6
            else:
                ar_i = anterior.obtener(cola)[2]
            if anterior.obtener(j) == "":
                a += 1
                ar = p1
            else:
                ar = anterior.obtener(j)[3]
            if fila.obtener(cola) == "":
                a += 1
                ab_i = p5
            else:
                ab_i = fila.obtener(cola)[1]
            if siguiente.obtener(j) == "":
                a += 1
                ab = p4
            else:
                ab = siguiente.obtener(j)[0]
            if ar_i != p6 or ar != p1 or ab_i != p5 or ab != p4 or a == 4:
                return False
            else:
                return True

        # con borde arriba bien
        elif x == 1 and w == 1 and y == 0 and z == 1:
            a = 0
            if fila.obtener(cola) == "":
                a += 1
                ab_i = p5
            else:
                ab_i = fila.obtener(cola)[1]
            if fila.obtener(cols) == "":
                a += 1
                ab_d = p3
            else:
                ab_d = fila.obtener(cols)[5]
            if siguiente.obtener(j) == "":
                a += 1
                ab = p4
            else:
                ab = siguiente.obtener(j)[0]
            if ab_i != p5 or ab != p4 or ab_d != p3 or a == 3:
                return False
            else:
                return True

        # borde abajo
        elif z == 0 and x == 1 and w == 1 and y == 1:
            a = 0
            if anterior.obtener(cola) == "":
                a += 1
                ar_i = p6
            else:
                ar_i = anterior.obtener(cola)[2]
            if anterior.obtener(j) == "":
                a += 1
                ar = p1
            else:
                ar = anterior.obtener(j)[3]
            if anterior.obtener(cols) == "":
                a += 1
                ar_d = p2
            else:
                ar_d = anterior.obtener(cols)[4]
            if fila.obtener(cola) == "":
                a += 1
                ab_i = p5
            else:
                ab_i = fila.obtener(cola)[1]
            if fila.obtener(cols) == "":
                a += 1
                ab_d = p3
            else:
                ab_d = fila.obtener(cols)[5]
            if ar_i != p6 or ar != p1 or ar_d != p2 or a == 5 or ab_d != p3 \
                    or ab_i != p5:
                return False
            else:
                return True

        # esquina arriba derecha
        elif x == 0 and y == 0 and w == 1 and z == 1:
            a = 0
            if fila.obtener(cola) == "":
                a += 1
                ab_i = p5
            else:
                ab_i = fila.obtener(cola)[1]
            if siguiente.obtener(j) == "":
                a += 1
                ab = p4
            else:
                ab = siguiente.obtener(j)[0]
            if ab_i != p5 or ab != p4 or a == 2:
                return False
            else:
                return True

        # esquina abajo derecha
        elif z == 0 and x == 0 and w == 1 and y == 1:
            a = 0
            if anterior.obtener(cola) == "":
                a += 1
                ar_i = p6
            else:
                ar_i = anterior.obtener(cola)[2]
            if anterior.obtener(j) == "":
                a += 1
                ar = p1
            else:
                ar = anterior.obtener(j)[3]
            if fila.obtener(cola) == "":
                a += 1
                ab_i = p5
            else:
                ab_i = fila.obtener(cola)[1]
            if ar_i != p6 or ar != p1 or ab_i != p5 or a == 3:
                return False
            else:
                return True

        else:
            print("algo malo ")


    if j % 2 == 0:

        # es par
        # aca primero en el caso q no tenga bordes:
        if x == 1 and y == 1 and w == 1 and z == 1:
            a = 0
            if fila.obtener(cola) == "":
                a += 1
                ar_i = p6
            else:
                ar_i = fila.obtener(cola)[2]
            if anterior.obtener(j) == "":
                a += 1
                ar = p1
            else:
                ar = anterior.obtener(j)[3]
            if fila.obtener(cols) == "":
                a += 1
                ar_d = p2
            else:
                ar_d = fila.obtener(cols)[4]
            if siguiente.obtener(cola) == "":
                a += 1
                ab_i = p5
            else:
                ab_i = siguiente.obtener(cola)[1]
            if siguiente.obtener(cols) == "":
                a += 1
                ab_d = p3
            else:
                ab_d = siguiente.obtener(cols)[5]
            if siguiente.obtener(j) == "":
                a += 1
                ab = p4
            else:
                ab = siguiente.obtener(j)[0]
            if ar_i != p6 or ar != p1 or ar_d != p2 or ab_i != p5 or ab != \
                    p4 or ab_d != p3 or a == 6:
                return False
            else:
                return True

        # borde a la izquierda
        elif w == 0 and x == 1 and y == 1 and z == 1:
            a = 0
            if anterior.obtener(j) == "":
                a += 1
                ar = p1
            else:
                ar = anterior.obtener(j)[3]
            if fila.obtener(cols) == "":
                a += 1
                ar_d = p2
            else:
                ar_d = fila.obtener(cols)[4]
            if siguiente.obtener(cols) == "":
                a += 1
                ab_d = p3
            else:
                ab_d = siguiente.obtener(cols)[5]
            if siguiente.obtener(j) == "":
                a += 1
                ab = p4
            else:
                ab = siguiente.obtener(j)[0]
            if ar != p1 or ar_d != p2 or ab != \
                    p4 or ab_d != p3 or a == 4:
                return False
            else:
                return True

        # con borde arriba
        elif y == 0 and x == 1 and z == 1 and w == 1:
            a = 0
            if siguiente.obtener(cola) == "":
                a += 1
                ab_i = p5
            else:
                ab_i = siguiente.obtener(cola)[1]
            if siguiente.obtener(cols) == "":
                a += 1
                ab_d = p3
            else:
                ab_d = siguiente.obtener(cols)[5]
            if siguiente.obtener(j) == "":
                a += 1
                ab = p4
            else:
                ab = siguiente.obtener(j)[0]
            if fila.obtener(cola) == "":
                a += 1
                ar_i = p6
            else:
                ar_i = fila.obtener(cola)[2]
            if fila.obtener(cols) == "":
                a += 1
                ar_d = p2
            else:
                ar_d = fila.obtener(cols)[4]
            if ab_i != p5 or ab != p4 or ab_d != p3 or a == 5 or ar_i != p6 \
                    or ar_d != p2:
                return False
            else:
                return True

        # borde abajo
        elif z == 0 and x == 1 and y == 1 and w == 1:
            a = 0
            if fila.obtener(cola) == "":
                a += 1
                ar_i = p6
            else:
                ar_i = fila.obtener(cola)[2]
            if anterior.obtener(j) == "":
                a += 1
                ar = p1
            else:
                ar = anterior.obtener(j)[3]
            if fila.obtener(cols) == "":
                a += 1
                ar_d = p2
            else:
                ar_d = fila.obtener(cols)[4]
            if ar_i != p6 or ar != p1 or ar_d != p2 or a == 3:
                return False
            else:
                return True

        # esquina abajo izquierda
        elif z == 0 and y == 1 and w == 0 and x == 1:
            a = 0
            if anterior.obtener(j) == "":
                a += 1
                ar = p1
            else:
                ar = anterior.obtener(j)[3]
            if fila.obtener(cols) == "":
                a += 1
                ar_d = p2
            else:
                ar_d = fila.obtener(cols)[4]
            if ar != p1 or ar_d != p2 or a == 2:
                return False
            else:
                return True

        # esquina arriba izquierda
        elif z == 1 and y == 0 and w == 0 and x == 1:
            a = 0
            if siguiente.obtener(cols) == "":
                a += 1
                ab_d = p3
            else:
                ab_d = siguiente.obtener(cols)[5]
            if siguiente.obtener(j) == "":
                a += 1
                ab = p4
            else:
                ab = siguiente.obtener(j)[0]
            if fila.obtener(cols) == "":
                a += 1
                ar_d = p2
            else:
                ar_d = fila.obtener(cols)[4]
            if ab != p4 or ab_d != p3 or a == 3 or ar_d != p2:
                return False
            else:
                return True

        else:
            print("algo malo ")

def numero_azar(valor):
    numero = random.randint(0,valor)
    return numero

def llenar_lista(listal):
    for i in range(0,8):
        listal.agregar_nodo("")

    return listal

def crear_hint(l1,l2,l3,l4,l5,l6,l7,l8,pieza,posiciones):

    for i in range(8):
        for j in range(8):
            if revisar_bordes(i,j,pieza,l1,l2,l3,l4,l5,l6,l7,l8,posiciones) == True:
                return str(str(i)+str(j))
    return False

def contar_puntos(jugadas,colores):
    # hacer for en colores y ver jugadas
    e = 0
    rojo = 0
    azul = 0
    for i in colores:
        i = str(i)
        if i == "red":
            puesta = str(jugadas[e])
            pieza = puesta[2:]
            for letra in pieza:
                if letra == "C":
                    rojo += 10
                elif letra == "P":
                    rojo += 20
                elif letra == "R":
                    rojo += 25
        if i == "blue":
            puesta = str(jugadas[e])
            pieza = puesta[2:]
            for letra in pieza:
                if letra == "C":
                    azul += 10
                elif letra == "P":
                    azul += 20
                elif letra == "R":
                    azul += 25
        e += 1
    final = CLASES.ListaLigada()
    final.agregar_nodo(azul)
    final.agregar_nodo(rojo)
    return final

def revisar_opcion(l1,l2,l3,l4,l5,l6,l7,l8,pieza,posiciones):
    for i in range(6):
        if crear_hint(l1,l2,l3,l4,l5,l6,l7,l8,pieza,posiciones) == False:
            primera = str(pieza[5])
            piezaa = str(pieza[:5])
            pieza = primera + piezaa
        else:
            return True
    print("Lo lamento, no puedes poner esta pieza en ninguna posicion, "
          "por lo tanto el juego ha terminado :(")
    return False


