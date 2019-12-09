"""
ESTE MODULO CORRESPONDE A LA DEFINICION DE CLASES
"""

# creamos la estructura del nodo
class Nodo:
    def __init__(self, valor=None):
        self.siguiente = None
        self.valor = valor
        self.conexiones = ListaLigada()

    def __repr__(self):
        return str(self.valor)

# se crea la estructura de una lista ligada
class ListaLigada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.len = 0

    # aqui hacemos que la lista se pueda iterar
    def __iter__(self):
        current = self.primero
        while current is not None:
            yield current
            current = current.siguiente

    def agregar_nodo(self, valor):
        if not self.primero:
            self.primero = Nodo(valor)
            self.ultimo = self.primero
        else:
            self.ultimo.siguiente = Nodo(valor)
            self.ultimo = self.ultimo.siguiente
        self.len += 1

    def obtener(self, posicion):
        nodo = self.primero

        for i in range(posicion):
            if nodo:
                nodo = nodo.siguiente
        if not nodo:
            return "posicion no encontrada"
        else:
            return nodo.valor


    def __repr__(self):
        rep = ''
        nodo_actual = self.primero

        while nodo_actual:
            rep += '{0}'.format(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente

        return rep

    def __len__(self):
        return self.len

    def __getitem__(self, item):
        nodo = self.primero
        for i in range(item):
            if nodo:
                nodo = nodo.siguiente
        if not nodo:
            raise IndexError
        else:
            return nodo.valor

class Grafo:
    # aca ver si le puedo poner un arriba abajo ......
    # ver el orden de agregar pa agregarle posiciones... si se pueda :)

    def __init__(self, i, j):
        self.valor = ""
        self.bordes = ListaLigada()
        self.i = i
        self.j = j


    def add_borde(self, i, j):
        for cosa in table:
            if cosa.i == i and cosa.j == j:
                self.bordes.agregar_nodo(cosa)
                break

    def __repr__(self):
        l = "Node{}".format(str(self.i)+str(self.j))
        return l

# para crear el tablero podemos hacer un grafo con varios nodos
table = ListaLigada()
for i in range(8):
    for j in range(8):
        a = Grafo(i, j)
        table.agregar_nodo(a)

# aqui creo las relaciones entre nodos
"""for node in table:
    print(type(node))
    # piezas sin bordes y impar
    if 0 < node.i < 7 and 0 < node.j < 7 and node.j % 2 != 0:
        node.add_borde(node.i - 1, node.j)
        node.add_borde(node.i - 1, node.j + 1)
        node.add_borde(node.i, node.j + 1)
        node.add_borde(node.i + 1, node.j)
        node.add_borde(node.i, node.j - 1)
        node.add_borde(node.i -1 , node.j - 1)

    # sin bordes y pares
    elif 0 < node.i < 7 and 0 < node.j < 7 and node.j % 2 == 0:
        node.add_borde(node.i -1 , node.j)
        node.add_borde(node.i, node.j + 1)
        node.add_borde(node.i + 1, node.j + 1)
        node.add_borde(node.i + 1, node.j)
        node.add_borde(node.i + 1, node.j - 1)
        node.add_borde(node.i, node.j - 1)

    elif node.i == 0:
        if node.j == 0:
            node.add_borde(None, None)
            node.add_borde(node.i, node.j+1)
            node.add_borde(node.i+1, node.j+1)
            node.add_borde(node.i+1, node.j)
            node.add_borde(None, None)
            node.add_borde(None, None)

        elif node.j == 7:
            node.add_borde(None, None)
            node.add_borde(None, None)
            node.add_borde(None, None)
            node.add_borde(node.i+1, node.j)
            node.add_borde(node.i, node.j-1)
            node.add_borde(None, None)

        elif node.j % 2 != 0:
            node.add_borde(None, None)
            node.add_borde(None, None)
            node.add_borde(node.i, node.j+1)
            node.add_borde(node.i+1, node.j)
            node.add_borde(node.i, node.j-1)
            node.add_borde(None, None)

        else:
            node.add_borde(None, None)
            node.add_borde(node.i, node.j+1)
            node.add_borde(node.i+1, node.j+1)
            node.add_borde(node.i+1, node.j)
            node.add_borde(node.i+1, node.j-1)
            node.add_borde(node.i, node.j-1)

    elif node.i == 7:
        if node.j == 0:
            node.add_borde(node.i-1,node.j)
            node.add_borde(node.i, node.j+1)
            node.add_borde(None, None)
            node.add_borde(None, None)
            node.add_borde(None, None)
            node.add_borde(None, None)

        elif node.j == 7:
            node.add_borde(node.i-1, node.j)
            node.add_borde(None, None)
            node.add_borde(None, None)
            node.add_borde(None, None)
            node.add_borde(node.i, node.j-1)
            node.add_borde(node.i-1, node.j-1)

        elif node.j % 2 != 0:
            node.add_borde(node.i-1, node.j)
            node.add_borde(node.i-1, node.j+1)
            node.add_borde(node.i, node.j+1)
            node.add_borde(None, None)
            node.add_borde(node.i, node.j-1)
            node.add_borde(node.i-1, node.j-1)

        else:
            node.add_borde(node.i-1, node.j)
            node.add_borde(node.i, node.j+1)
            node.add_borde(None, None)
            node.add_borde(None, None)
            node.add_borde(None, None)
            node.add_borde(node.i, node.j-1)

    elif node.j == 0:
        node.add_borde(node.i-1, node.j)
        node.add_borde(node.i, node.j+1)
        node.add_borde(node.i+1, node.j+1)
        node.add_borde(node.i+1, node.j)
        node.add_borde(None, None)
        node.add_borde(None, None)

    elif node.j == 7:
        node.add_borde(node.i-1, node.j)
        node.add_borde(None, None)
        node.add_borde(None, None)
        node.add_borde(node.i+1, node.j)
        node.add_borde(node.i, node.j-1)
        node.add_borde(node.i-1, node.j)
"""
