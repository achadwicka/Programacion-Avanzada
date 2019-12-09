"""
ACA SE CREAN TODOS LOS DATOS NECESARIOS
"""
import CLASES
import FUNCIONES

piezas = FUNCIONES.leer_archivo("pieces_name.csv")
cantidad = FUNCIONES.crear_lista_numeros("pieces.csv")
fila1 = CLASES.ListaLigada()
fila2 = CLASES.ListaLigada()
fila3 = CLASES.ListaLigada()
fila4 = CLASES.ListaLigada()
fila5 = CLASES.ListaLigada()
fila6 = CLASES.ListaLigada()
fila7 = CLASES.ListaLigada()
fila8 = CLASES.ListaLigada()
FUNCIONES.llenar_lista(fila1)
FUNCIONES.llenar_lista(fila2)
FUNCIONES.llenar_lista(fila3)
FUNCIONES.llenar_lista(fila4)
FUNCIONES.llenar_lista(fila5)
FUNCIONES.llenar_lista(fila6)
FUNCIONES.llenar_lista(fila7)
FUNCIONES.llenar_lista(fila8)

puestas = CLASES.ListaLigada()
posiciones = CLASES.ListaLigada()
guardados = CLASES.ListaLigada()
colores = CLASES.ListaLigada()
