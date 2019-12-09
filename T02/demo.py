import gui
import sys
from random import choice, randint
import DATOS
import CLASES
import FUNCIONES

def elegir_pieza():
    largo = len(DATOS.piezas)
    b = False

    numero = FUNCIONES.numero_azar(DATOS.piezas.len - 1)
    # aca reviso que queden piezas y si es asi resto una
    while b == False:
        pie = 0
        i = 0
        for cantidad in DATOS.cantidad:
            if numero == i:
                ca = str(cantidad)
                c = int(ca)
                if c > 0:
                    b = True
                    c -= 1
                    cantidad.valor = str(c)
                    break
                else:
                    numero = FUNCIONES.numero_azar(
                        DATOS.piezas.len - 1)
                    break

            else:
                i += 1
                pie += 1

            if pie == largo:
                return "salir"
    i = 0


    for nombre in DATOS.piezas:
        if i == numero:
            pieza = str(nombre)
            break
        else:
            i += 1

    return pieza[:6]

def get_next_number():
    num = 1
    while True:
        yield num
        num += 1

# aca agregamos la pieza al tablero (fila i col j)
def agregar_valor(i,j, valor):
    if i == 0:
        a = 0
        for node in DATOS.fila1:
            if a == j:
                # aca ver que valor asignar! tiene q ser str
                node.valor = valor
                break
            else:
                a += 1
    elif i == 1:
        a = 0
        for node in DATOS.fila2:
            if a == j:
                # aca ver que valor asignar! tiene q ser str
                node.valor = valor
                break
            else:
                a += 1
    elif i == 2:
        a = 0
        for node in DATOS.fila3:
            if a == j:
                # aca ver que valor asignar! tiene q ser str
                node.valor = valor
                break
            else:
                a += 1
    elif i == 3:
        a = 0
        for node in DATOS.fila4:
            if a == j:
                # aca ver que valor asignar! tiene q ser str
                node.valor = valor
                break
            else:
                a += 1
    elif i == 4:
        a = 0
        for node in DATOS.fila5:
            if a == j:
                # aca ver que valor asignar! tiene q ser str
                node.valor = valor
                break
            else:
                a += 1
    elif i == 5:
        a = 0
        for node in DATOS.fila6:
            if a == j:
                # aca ver que valor asignar! tiene q ser str
                node.valor = valor
                break
            else:
                a += 1
    elif i == 6:
        a = 0
        for node in DATOS.fila7:
            if a == j:
                # aca ver que valor asignar! tiene q ser str
                node.valor = valor
                break
            else:
                a += 1
    else:
        a = 0
        for node in DATOS.fila8:
            if a == j:
                # aca ver que valor asignar! tiene q ser str
                node.valor = valor
                break
            else:
                a += 1

a = get_next_number()

class MyInterface(gui.GameInterface):
    def __init__(self):

        self.npieza = elegir_pieza()
        self.color = ""
        self.rojo = ""
        self.azul = ""
        self.numeros = 0
        self.hint = ""

        e = randint(0, 1)
        if e == 1:
            self.color = "red"
        else:
            self.color = "blue"

        # falta ver color y si hay y guardarla
        gui.nueva_pieza(color=self.color, piece_type=self.npieza)
        i = randint(0, 7)
        j = randint(0, 7)
        agregar_valor(i, j, self.npieza)
        gui.add_piece(i, j)
        poner = str(i) + str(j) + str(self.npieza)
        DATOS.colores.agregar_nodo(self.color)
        DATOS.puestas.agregar_nodo(poner)
        DATOS.posiciones.agregar_nodo(str(i)+str(j))

        self.npieza = elegir_pieza()
        if self.npieza == "salir":
            print("Se terminaron las piezas :(")
            self.terminar_juego()
        if FUNCIONES.revisar_opcion(DATOS.fila1,DATOS.fila2,DATOS.fila3,
                             DATOS.fila4,DATOS.fila5,DATOS.fila6,
                             DATOS.fila7,DATOS.fila8,self.npieza,
                                 DATOS.posiciones) == False:
            self.terminar_juego()
        if self.color == "red":
            self.color = "blue"
        else:
            self.color = "red"
        gui.nueva_pieza(color=self.color, piece_type=self.npieza)

        pass

    # aca bien
    def colocar_pieza(self, i, j):
        if FUNCIONES.revisar_bordes(i, j, self.npieza, DATOS.fila1,
                                    DATOS.fila2, DATOS.fila3, DATOS.fila4,
                                    DATOS.fila5, DATOS.fila6, DATOS.fila7,
                                    DATOS.fila8, DATOS.posiciones) == True:
            if self.hint == "":
                pass
            else:
                gui.pop_piece(int(self.hint[0]),int(self.hint[1]))
                self.hint = ""
            print("Presionaste", (i, j))
            # comenta la siguiente linea y descomenta la que sigue para ver como se destaca un espacio
            gui.add_piece(i, j)
            DATOS.posiciones.agregar_nodo(str(i)+str(j))
            agregar_valor(i, j, self.npieza)
            poner = str(i)+str(j)+str(self.npieza)
            DATOS.puestas.agregar_nodo(poner)
            DATOS.colores.agregar_nodo(self.color)
            # aca guardar la jugada para poder borrarla despues
            if self.color == "red":
                self.rojo = str(i)+str(j)
                self.color = "blue"
            else:
                self.azul = poner
                self.color = "red"
            self.npieza = elegir_pieza()
            if self.npieza == "salir":
                print("Se terminaron las piezas :(")
                self.terminar_juego()
            if FUNCIONES.revisar_opcion(DATOS.fila1, DATOS.fila2, DATOS.fila3,
                                        DATOS.fila4, DATOS.fila5, DATOS.fila6,
                                        DATOS.fila7, DATOS.fila8, self.npieza,
                                        DATOS.posiciones) == False:
                self.terminar_juego()

            gui.nueva_pieza(color=self.color,piece_type= self.npieza)


        else:
            print("No se puede ingresar esa pieza en esa posicion.")

    #listo
    def rotar_pieza(self, orientation):
        if self.hint == "":
            pass
        else:
            gui.pop_piece(int(self.hint[0]), int(self.hint[1]))
            self.hint = ""
        primera = self.npieza[5]
        pieza = self.npieza[:5]
        self.npieza = primera + pieza
        return

    # bien
    def retroceder(self):
        if self.hint == "":
            pass
        else:
            gui.pop_piece(int(self.hint[0]),int(self.hint[1]))
            self.hint = ""

        if self.color == "red":
            if self.rojo == "":
                print("En tu ultima jugada no pusiste ninguna pieza :(")
                return
            quitar = self.rojo
            i = quitar[0]
            j = quitar[1]
            gui.pop_piece(int(i),int(j))
            self.rojo = ""
            self.color = "blue"
        else:
            if self.azul == "":
                print("En tu ultima jugada no pusiste ninguna pieza :(")
                return
            quitar = self.azul
            i = quitar[0]
            j = quitar[1]
            gui.pop_piece(int(i),int(j))
            self.color = "red"
            self.azul = ""
        self.npieza = elegir_pieza()
        if self.npieza == "salir":
            print("Se terminaron las piezas :(")
            self.terminar_juego()
        if FUNCIONES.revisar_opcion(DATOS.fila1,DATOS.fila2,DATOS.fila3,
                             DATOS.fila4,DATOS.fila5,DATOS.fila6,
                             DATOS.fila7,DATOS.fila8,self.npieza,
                                 DATOS.posiciones) == False:
            self.terminar_juego()
        gui.nueva_pieza(self.color,self.npieza)
        nueva = CLASES.ListaLigada()
        tabl = CLASES.ListaLigada()
        col = CLASES.ListaLigada()
        j = 0
        for node in DATOS.posiciones:
            if node != str(i)+str(j):
                nueva.agregar_nodo(node)
            else:
                j += 1
        a = 0
        for node in DATOS.colores:
            if a != j:
                col.agregar_nodo(node)
                a += 1
            else:
                a += 1
        for node in DATOS.puestas:
            if str(node)[0] != i and str(node)[1] != j:
                tabl.agregar_nodo(node)
        DATOS.puestas = CLASES.ListaLigada()
        for node in tabl:
            DATOS.puestas.agregar_nodo(node)
        DATOS.posiciones = CLASES.ListaLigada()
        for node in nueva:
            DATOS.posiciones.agregar_nodo(node)
        DATOS.colores = CLASES.ListaLigada()
        for node in col:
            DATOS.colores.agregar_nodo(node)
        print("Presionaste retroceder")

    def terminar_juego(self):
        lista = FUNCIONES.contar_puntos(DATOS.puestas, DATOS.colores)
        azul = int(lista[0])
        rojo = int(lista[1])
        print("Presionaste terminar juego")
        # contar puntos
        gui.set_points(1,azul)
        gui.set_points(2,rojo)

    # listo :)
    def hint_asked(self):
        a = FUNCIONES.crear_hint(DATOS.fila1,DATOS.fila2,DATOS.fila3,
                             DATOS.fila4,DATOS.fila5,DATOS.fila6,
                             DATOS.fila7,DATOS.fila8,self.npieza,
                                 DATOS.posiciones)
        if a == False:
            print("Lo lamento, no puedes poner esta pieza, puedes rotarla y "
                  "pedir otro hint :)")
            return
        else:
            a = str(a)
            i = int(a[0])
            j = int(a[1])
            gui.add_hint(i,j)
            self.hint = str(i)+str(j)



    def click_number(self, number):
        if self.hint == "":
            pass
        else:
            gui.pop_piece(int(self.hint[0]),int(self.hint[1]))
            self.hint = ""
        # borra el numero bien.
        for i in range(int(number),self.numeros):
            gui.pop_number()
            self.numeros -= 1

        tablero = CLASES.ListaLigada()
        colrs = CLASES.ListaLigada()
        # aca se ve el total de piezas que hay puestas en el numero guardado
        # borra las piezas, bien
        for i in range(DATOS.posiciones.len):
            x = int(str(DATOS.posiciones.obtener(i))[0])
            y = int(str(DATOS.posiciones.obtener(i))[1])
            gui.pop_piece(x,y)
        pos = DATOS.guardados.obtener(int(number)-1)
        posic = CLASES.ListaLigada()
        # aca se crean otras listas para poder cambiar las otras
        for i in range(int(pos)):
            x = DATOS.posiciones.obtener(i)
            te = DATOS.puestas.obtener(i)
            co = DATOS.colores.obtener(i)
            tablero.agregar_nodo(str(te))
            colrs.agregar_nodo(str(co))
            posic.agregar_nodo(str(x))
        DATOS.puestas = CLASES.ListaLigada()
        DATOS.colores = CLASES.ListaLigada()
        DATOS.posiciones = CLASES.ListaLigada()
        for node in posic:
            node = str(node)
            DATOS.posiciones.agregar_nodo(node)
        for node in colrs:
            node = str(node)
            DATOS.colores.agregar_nodo(node)
        for node in tablero:
            node = str(node)
            DATOS.puestas.agregar_nodo(node)

        z = 0
        for elem in DATOS.puestas:
            e = str(elem)
            gui.nueva_pieza(colrs.obtener(z),e[2:])
            gui.add_piece(int(e[0]),int(e[1]))
            z += 1

        guar = CLASES.ListaLigada()
        for i in range(self.numeros):
            guar.agregar_nodo(str(DATOS.guardados.obtener(i)))

        DATOS.guardados = CLASES.ListaLigada()
        for i in range(guar.len):
            DATOS.guardados.agregar_nodo(str(guar.obtener(i)))
        self.npieza = elegir_pieza()

        if self.npieza == "salir":
            print("Se terminaron las piezas :(")
            self.terminar_juego()
        if FUNCIONES.revisar_opcion(DATOS.fila1,DATOS.fila2,DATOS.fila3,
                             DATOS.fila4,DATOS.fila5,DATOS.fila6,
                             DATOS.fila7,DATOS.fila8,self.npieza,
                                 DATOS.posiciones) == False:
            self.terminar_juego()

        gui.nueva_pieza(self.color,self.npieza)

        DATOS.fila1 = CLASES.ListaLigada()
        DATOS.fila2 = CLASES.ListaLigada()
        DATOS.fila3 = CLASES.ListaLigada()
        DATOS.fila4 = CLASES.ListaLigada()
        DATOS.fila5 = CLASES.ListaLigada()
        DATOS.fila6 = CLASES.ListaLigada()
        DATOS.fila7 = CLASES.ListaLigada()
        DATOS.fila8 = CLASES.ListaLigada()
        FUNCIONES.llenar_lista(DATOS.fila1)
        FUNCIONES.llenar_lista(DATOS.fila2)
        FUNCIONES.llenar_lista(DATOS.fila3)
        FUNCIONES.llenar_lista(DATOS.fila4)
        FUNCIONES.llenar_lista(DATOS.fila5)
        FUNCIONES.llenar_lista(DATOS.fila6)
        FUNCIONES.llenar_lista(DATOS.fila7)
        FUNCIONES.llenar_lista(DATOS.fila8)

        for pieza in DATOS.puestas:
            e = str(pieza)
            agregar_valor(int(e[0]),int(e[1]),e[2:])

    # listo
    def guardar_juego(self):
        if self.hint == "":
            pass
        else:
            gui.pop_piece(int(self.hint[0]),int(self.hint[1]))
            self.hint = ""
        self.numeros += 1
        DATOS.guardados.agregar_nodo(DATOS.puestas.len)
        gui.add_number(self.numeros, self.color)

        print("Presionaron guardar")


if __name__ == 'demo':
    def hook(type, value, traceback):
        print(type)
        print(value)
        print(traceback)


    sys.__excepthook__ = hook

    gui.set_scale(False)  # Any float different from 0
    gui.init()
    gui.set_quality("ultra")  # low, medium, high ultra
    gui.set_animations(False)
    gui.init_grid()
    gui.set_game_interface(MyInterface())  # GUI Listener
    gui.run()
