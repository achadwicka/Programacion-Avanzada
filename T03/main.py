from gui.Gui import MyWindow
from PyQt5 import QtWidgets
import sys
import HUMANGI as hu
from Excepciones import *


class T03Window(MyWindow):
    def __init__(self):
        super().__init__()
        self.j = 1
        self.p = 1

    def process_query(self, query_array):
        # Agrega en pantalla la solucion. Muestra los graficos!!
        for elem in query_array:

            try:
                if elem[0] == "pariente_de":
                    if elem[1] == "n":
                        text = hu.pariente_de(elem[1], elem[2])
                    else:
                        text = hu.pariente_de(int(elem[1]), elem[2])

                elif elem[0] == "índice_de_tamaño":
                    text = hu.indice_de_tamano(elem[1])

                elif elem[0] == "ascendencia":
                    text = hu.ascendencia(elem[1])

                elif elem[0] == "gemelo_genético":
                    text = [hu.gemelo_identico(elem[1])]

                elif elem[0] == "min":
                    text = [hu.minimo(elem[1])]

                elif elem[0] == "max":
                    text = [hu.maximo(elem[1])]

                elif elem[0] == "prom":
                    text = [hu.prom(elem[1])]

                elif elem[0] == "valor_característica":
                    if type(hu.valor_caracteristica(elem[1], elem[2])) == str:
                        text = [hu.valor_caracteristica(elem[1], elem[2])]
                    else:
                        text = hu.valor_caracteristica(elem[1], elem[2])
                else:
                    raise BadRequest
                if type(text) == list:
                    if len(text) == 0:
                        raise NotAcceptable


            except NotFound:
                text = [NotFound()]
            except BadRequest:
                text = [BadRequest()]
            except NotAcceptable:
                text = [NotAcceptable()]
            except GenomeError:
                text = [GenomeError()]
            self.add_answer("-------- CONSULTA " + str(self.j) + " --------\n")
            if type(text) != list:
                self.add_answer(str(text) + "\n")
            else:
                for i in text:
                    self.add_answer(str(i)+"\n")

            self.j += 1

            # aca podemos generar todas las excepciones y probar las cosas
            # dentro del for en el query array

    def save_file(self, query_array):
        consul = []
        # Agrega en pantalla la solucion. Muestra los graficos!!
        for elem in query_array:

            try:
                if elem[0] == "pariente_de":
                    if elem[1] == "n":
                        text = hu.pariente_de(elem[1], elem[2])
                    else:
                        text = hu.pariente_de(int(elem[1]), elem[2])

                elif elem[0] == "índice_de_tamaño":
                    text = hu.indice_de_tamano(elem[1])

                elif elem[0] == "ascendencia":
                    text = hu.ascendencia(elem[1])

                elif elem[0] == "gemelo_genético":
                    text = [hu.gemelo_identico(elem[1])]

                elif elem[0] == "min":
                    text = [hu.minimo(elem[1])]

                elif elem[0] == "max":
                    text = [hu.maximo(elem[1])]

                elif elem[0] == "prom":
                    text = [hu.prom(elem[1])]

                elif elem[0] == "valor_característica":
                    if type(hu.valor_caracteristica(elem[1], elem[2])) == str:
                        text = [hu.valor_caracteristica(elem[1], elem[2])]
                    else:
                        text = hu.valor_caracteristica(elem[1], elem[2])
                else:
                    raise BadRequest
                if len(text) == 0:
                    raise NotAcceptable

            except NotFound:
                text = [NotFound()]
            except BadRequest:
                text = [BadRequest()]
            except NotAcceptable:
                text = [NotAcceptable()]
            except GenomeError:
                text = [GenomeError()]

            consul.append("-------- CONSULTA " + str(self.p) + " --------")
            consul.append(text)

            self.p += 1
        with open("resultados.txt", "w", encoding='UTF-8') as file:
            for i in consul:
                if type(i) == list:
                    for elem in i:
                        file.write(str(elem) + "\n")
                else:
                    file.write(str(i) + "\n")

if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(value)
        print(traceback)


    sys.__excepthook__ = hook

    app = QtWidgets.QApplication(sys.argv)
    window = T03Window()
    sys.exit(app.exec_())
