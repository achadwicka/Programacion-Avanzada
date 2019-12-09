import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, \
    QTextEdit, QPushButton
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPixmap
import os
from cliente import Client
from eventos import *
import random

# clases de ventanas para ir abriendo
class Ingreso(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("uis/ingreso.ui", self)


class Espectador(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("uis/espectador.ui", self)


class Colores(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("uis/colores.ui", self)


class Ventana_edicion(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("uis/ventana_edicion.ui", self)


class Pop_up_existe(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("uis/pop_up_existe.ui", self)
        self.volver.clicked.connect(self.cerrar)

    def cerrar(self):
        self.close()


class Pop_up_noexiste(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("uis/pop_up_noexiste.ui", self)
        self.volver.clicked.connect(self.cerrar)

    def cerrar(self):
        self.close()


class Pop_up_tipo(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("uis/pop_up_tipo.ui", self)
        self.volver.clicked.connect(self.cerrar)

    def cerrar(self):
        self.close()


class Pop_up_maximo(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("uis/pop_up_maximo.ui", self)
        self.volver.clicked.connect(self.cerrar)

    def cerrar(self):
        self.close()


class Pop_up_conectado(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("uis/pup_up_conectado.ui", self)
        self.volver.clicked.connect(self.cerrar)

    def cerrar(self):
        self.close()


# clase principal
class MainWindow(QMainWindow):

    senal_ingreso = pyqtSignal(Ingresa)
    senal_cerrar_sesion = pyqtSignal(Ingresa)
    trigger_pide = pyqtSignal()
    trigger_edit = pyqtSignal(Edit)
    trigger_bloqueo = pyqtSignal(Imagenes)
    trigger_desbloqueo = pyqtSignal(Imagenes)
    trigger_pide_descarga = pyqtSignal(Imagenes)
    trigger_comentarios = pyqtSignal(Actualiza_edit)
    trigger_pide_come = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.nombre = ''
        uic.loadUi("uis/mainwindow.ui", self)
        self.client = Client(self)
        self.orden = []
        self.imagenes = ['Knightmare.png', 'DragonBall.png',
                         'MickeyMouse.png', 'Mushroom.png']
        while len(self.orden) < 4:
            a = random.randint(0, 3)
            if a not in self.orden:
                self.orden.append(a)

        # aca vemos el orden original
        self.final = [self.imagenes[self.orden[0]], self.imagenes[
            self.orden[1]], self.imagenes[self.orden[2]], self.imagenes[
            self.orden[3]]]

        self.pos1 = self.orden[0]
        self.pos2 = self.orden[1]
        self.pos3 = self.orden[2]
        self.pos4 = self.orden[3]

        self.trigger_pide.connect(self.client.pide)
        self.trigger_edit.connect(self.client.edit)
        self.trigger_bloqueo.connect(self.client.bloqueo)
        self.trigger_desbloqueo.connect(self.client.desbloqueo)
        self.trigger_pide_descarga.connect(self.client.descarga)
        self.trigger_comentarios.connect(self.client.comenta)
        self.trigger_pide_come.connect(self.client.pidecom)
        self.trigger_pide.emit()
        self.imagen1 = QPixmap()
        self.imagen2 = QPixmap()
        self.imagen3 = QPixmap()
        self.imagen4 = QPixmap()
        self.veri1 = QPixmap()
        self.veri2 = QPixmap()
        self.veri3 = QPixmap()
        self.veri4 = QPixmap()

        self.ventana_ingreso = Ingreso()
        self.pop_up_existe = Pop_up_existe()
        self.pop_up_tipo = Pop_up_tipo()
        self.pop_up_maximo = Pop_up_maximo()
        self.pop_up_noexiste = Pop_up_noexiste()
        self.pop_up_conectado = Pop_up_conectado()
        self.espectador = Espectador()
        self.espectador.volver.clicked.connect(self.volveresp)
        self.ventana_edicion = Ventana_edicion()
        self.ventana_edicion.descarga.clicked.connect(self.descar)
        self.espectador.descarga.clicked.connect(self.descar)
        self.ventana_colores = Colores()
        self.ventana_edicion.volver.clicked.connect(self.volver_ingreso)
        self.senal_ingreso.connect(self.client.envio_cliente)
        self.senal_cerrar_sesion.connect(self.client.envio_cliente)
        self.ventana_edicion.comenta.clicked.connect(self.comenta)
        self.espectador.comenta.clicked.connect(self.comenta)
        self.cerrar.clicked.connect(self.cerrar_sesion)
        self.editar1.clicked.connect(self.edita1)
        self.editar2.clicked.connect(self.edita2)
        self.editar3.clicked.connect(self.edita3)
        self.editar4.clicked.connect(self.edita4)
        self.editando = 0
        self.viendo = 0
        self.entrar()

    def entrar(self):
        self.ventana_ingreso.ingresar.clicked.connect(self.ingresar)
        self.ventana_ingreso.registrarse.clicked.connect(self.registrarse)
        self.ventana_ingreso.show()

    def ingresar(self):
        nombre = self.ventana_ingreso.nombre.text()
        self.ventana_ingreso.nombre.clear()
        self.nombre = nombre
        senal = Ingresa(nombre, 'ingreso')
        self.senal_ingreso.emit(senal)

    def registrarse(self):
        nombre = self.ventana_ingreso.nombre.text()
        self.ventana_ingreso.nombre.clear()
        senal = Ingresa(nombre, 'registro')
        self.senal_ingreso.emit(senal)
        self.nombre = nombre

    def volveresp(self):
        self.ventana_edicion.comentarios.clear()
        self.espectador.comentarios.clear()
        self.viendo = 0
        self.espectador.close()
        self.show()

    def cerrar_ventana(self, event):
        v = event.ventana

        if v == 'ventana_ingreso':
            self.ventana_ingreso.close()
            self.show()

    def abrir_ventana(self, event):
        v = event.ventana

        if v == 'pop_up_tipo':
            self.pop_up_tipo.show()

        elif v == 'pop_up_noexiste':
            self.pop_up_noexiste.show()

        elif v == 'pop_up_maximo':
            self.pop_up_maximo.show()

        elif v == 'pop_up_existe':
            self.pop_up_existe.show()

        elif v == 'pop_up_conectado':
            self.pop_up_conectado.show()

    def cerrar_sesion(self):
        senal = Ingresa(self.nombre, 'cerrar_sesion')
        self.close()
        self.ventana_ingreso.show()
        self.senal_cerrar_sesion.emit(senal)

    def genera_imagenes(self, event):
        lista = event.images
        self.imagen1 = QPixmap()
        self.imagen2 = QPixmap()
        self.imagen3 = QPixmap()
        self.imagen4 = QPixmap()
        self.imagen1.loadFromData(lista[self.orden[0]])
        self.imagen2.loadFromData(lista[self.orden[1]])
        self.imagen3.loadFromData(lista[self.orden[2]])
        self.imagen4.loadFromData(lista[self.orden[3]])
        scaled = self.imagen1.scaled(self.foto1.size(), Qt.KeepAspectRatio)
        scaled2 = self.imagen2.scaled(self.foto2.size(), Qt.KeepAspectRatio)
        scaled3 = self.imagen3.scaled(self.foto3.size(), Qt.KeepAspectRatio)
        scaled4 = self.imagen4.scaled(self.foto4.size(), Qt.KeepAspectRatio)
        self.foto1.setPixmap(scaled)
        self.foto2.setPixmap(scaled2)
        self.foto3.setPixmap(scaled3)
        self.foto4.setPixmap(scaled4)

    def comenta(self):
        if self.editando != 0:
            text = self.ventana_edicion.escrito.text()
        else:
            text = self.espectador.escrito.text()
        self.ventana_edicion.escrito.clear()
        self.espectador.escrito.clear()
        e = [self.nombre, text]
        if self.editando == 1 or self.viendo == 1:
            self.trigger_comentarios.emit(Actualiza_edit(e, self.pos1))
        elif self.editando == 2 or self.viendo == 2:
            self.trigger_comentarios.emit(Actualiza_edit(e, self.pos2))
        elif self.editando == 3 or self.viendo == 3:
            self.trigger_comentarios.emit(Actualiza_edit(e, self.pos3))
        else:
            self.trigger_comentarios.emit(Actualiza_edit(e, self.pos4))

    def edita1(self):

        self.editando = 1
        self.pide_come()
        self.desconecta()
        self.trigger_bloqueo.emit(Imagenes(self.pos1))
        self.close()
        scaled = self.imagen1.scaled(self.ventana_edicion.imagen.size(),
                                     Qt.KeepAspectRatio)
        self.ventana_edicion.imagen.setPixmap(scaled)
        self.ventana_edicion.blurry.clicked.connect(self.blurry1)
        self.ventana_edicion.blade.clicked.connect(self.blade1)
        self.ventana_edicion.recortar.clicked.connect(self.recorta1)
        self.ventana_edicion.show()

    def blurry1(self):
        self.trigger_edit.emit(Edit(self.pos1, ['blurry']))

    def blade1(self):
        self.ventana_colores.blanco.clicked.connect(self.blanco1)
        self.ventana_colores.azul.clicked.connect(self.azul1)
        self.ventana_colores.amarillo.clicked.connect(self.amarillo1)
        self.ventana_colores.negro.clicked.connect(self.negro1)
        self.ventana_colores.rojo.clicked.connect(self.rojo1)
        self.ventana_colores.show()

    def recorta1(self):
        self.trigger_edit.emit(Edit(self.pos1, ['recorta']))

    def blanco1(self):
        self.ventana_colores.close()
        self.trigger_edit.emit(Edit(self.pos1, ['blade', 'blanco']))

    def azul1(self):
        self.ventana_colores.close()
        self.trigger_edit.emit(Edit(self.pos1, ['blade', 'azul']))

    def amarillo1(self):
        self.ventana_colores.close()
        self.trigger_edit.emit(Edit(self.pos1, ['blade', 'amarillo']))

    def negro1(self):
        self.ventana_colores.close()
        self.trigger_edit.emit(Edit(self.pos1, ['blade', 'negro']))

    def rojo1(self):
        self.ventana_colores.close()
        self.trigger_edit.emit(Edit(self.pos1, ['blade', 'rojo']))

    def edita2(self):
        self.editando = 2
        self.pide_come()
        self.desconecta()
        self.trigger_bloqueo.emit(Imagenes(self.pos2))
        self.close()
        scaled = self.imagen2.scaled(self.ventana_edicion.imagen.size(),
                                     Qt.KeepAspectRatio)
        self.ventana_edicion.imagen.setPixmap(scaled)
        self.ventana_edicion.blurry.clicked.connect(self.blurry2)
        self.ventana_edicion.recortar.clicked.connect(self.recorta2)
        self.ventana_edicion.blade.clicked.connect(self.blade2)
        self.ventana_edicion.show()

    def blurry2(self):
        self.trigger_edit.emit(Edit(self.pos2, ['blurry']))

    def blade2(self):
        self.ventana_colores.blanco.clicked.connect(self.blanco2)
        self.ventana_colores.azul.clicked.connect(self.azul2)
        self.ventana_colores.amarillo.clicked.connect(self.amarillo2)
        self.ventana_colores.negro.clicked.connect(self.negro2)
        self.ventana_colores.rojo.clicked.connect(self.rojo2)
        self.ventana_colores.show()

    def recorta2(self):
        self.trigger_edit.emit(Edit(self.pos2, ['recorta']))

    def blanco2(self):
        self.ventana_colores.close()
        self.trigger_edit.emit(Edit(self.pos2, ['blade', 'blanco']))

    def azul2(self):
        self.ventana_colores.close()
        self.trigger_edit.emit(Edit(self.pos2, ['blade', 'azul']))

    def amarillo2(self):
        self.ventana_colores.close()
        self.trigger_edit.emit(Edit(self.pos2, ['blade', 'amarillo']))

    def negro2(self):
        self.ventana_colores.close()
        self.trigger_edit.emit(Edit(self.pos2, ['blade', 'negro']))

    def rojo2(self):
        self.ventana_colores.close()
        self.trigger_edit.emit(Edit(self.pos2, ['blade', 'rojo']))

    def edita3(self):
        self.editando = 3
        self.pide_come()
        self.desconecta()
        self.trigger_bloqueo.emit(Imagenes(self.pos3))
        self.close()
        scaled = self.imagen3.scaled(self.ventana_edicion.imagen.size(),
                                     Qt.KeepAspectRatio)
        self.ventana_edicion.imagen.setPixmap(scaled)
        self.ventana_edicion.blurry.clicked.connect(self.blurry3)
        self.ventana_edicion.recortar.clicked.connect(self.recorta3)
        self.ventana_edicion.blade.clicked.connect(self.blade3)
        self.ventana_edicion.show()

    def blurry3(self):
        self.trigger_edit.emit(Edit(self.pos3, ['blurry']))

    def blade3(self):
        self.ventana_colores.blanco.clicked.connect(self.blanco3)
        self.ventana_colores.azul.clicked.connect(self.azul3)
        self.ventana_colores.amarillo.clicked.connect(self.amarillo3)
        self.ventana_colores.negro.clicked.connect(self.negro3)
        self.ventana_colores.rojo.clicked.connect(self.rojo3)
        self.ventana_colores.show()

    def recorta3(self):
        self.trigger_edit.emit(Edit(self.pos3, ['recorta']))

    def blanco3(self):
        self.ventana_colores.close()
        self.trigger_edit.emit(Edit(self.pos3, ['blade', 'blanco']))

    def azul3(self):
        self.ventana_colores.close()
        self.trigger_edit.emit(Edit(self.pos3, ['blade', 'azul']))

    def amarillo3(self):
        self.ventana_colores.close()
        self.trigger_edit.emit(Edit(self.pos3, ['blade', 'amarillo']))

    def negro3(self):
        self.ventana_colores.close()
        self.trigger_edit.emit(Edit(self.pos3, ['blade', 'negro']))

    def rojo3(self):
        self.ventana_colores.close()
        self.trigger_edit.emit(Edit(self.pos3, ['blade', 'rojo']))

    def edita4(self):
        self.editando = 4
        self.pide_come()
        self.desconecta()
        self.trigger_bloqueo.emit(Imagenes(self.pos4))
        self.close()
        scaled = self.imagen4.scaled(self.ventana_edicion.imagen.size(),
                                     Qt.KeepAspectRatio)
        self.ventana_edicion.imagen.setPixmap(scaled)
        self.ventana_edicion.blurry.clicked.connect(self.blurry4)
        self.ventana_edicion.recortar.clicked.connect(self.recorta4)
        self.ventana_edicion.blade.clicked.connect(self.blade4)
        self.ventana_edicion.show()

    def blurry4(self):
        self.trigger_edit.emit(Edit(self.pos4, ['blurry']))

    def blade4(self):
        self.ventana_colores.blanco.clicked.connect(self.blanco4)
        self.ventana_colores.azul.clicked.connect(self.azul4)
        self.ventana_colores.amarillo.clicked.connect(self.amarillo4)
        self.ventana_colores.negro.clicked.connect(self.negro4)
        self.ventana_colores.rojo.clicked.connect(self.rojo4)
        self.ventana_colores.show()

    def recorta4(self):
        self.trigger_edit.emit(Edit(self.pos4, ['recorta']))

    def blanco4(self):
        self.ventana_colores.close()
        self.trigger_edit.emit(Edit(self.pos4, ['blade', 'blanco']))

    def azul4(self):
        self.ventana_colores.close()
        self.trigger_edit.emit(Edit(self.pos4, ['blade', 'azul']))

    def amarillo4(self):
        self.ventana_colores.close()
        self.trigger_edit.emit(Edit(self.pos4, ['blade', 'amarillo']))

    def negro4(self):
        self.ventana_colores.close()
        self.trigger_edit.emit(Edit(self.pos4, ['blade', 'negro']))

    def rojo4(self):
        self.ventana_colores.close()
        self.trigger_edit.emit(Edit(self.pos4, ['blade', 'rojo']))

    def actualiza(self, evento):
        text = QTextEdit()
        self.activos.setWidget(text)
        usuarios = evento.lista
        for nombre in usuarios:
            text.append(nombre)

    def volver_ingreso(self):
        self.ventana_edicion.comentarios.clear()
        self.espectador.comentarios.clear()
        self.ventana_edicion.editada.setPixmap(QPixmap())
        if self.editando == 1:
            self.trigger_desbloqueo.emit(Imagenes(self.orden[0]))
        elif self.editando == 2:
            self.trigger_desbloqueo.emit(Imagenes(self.orden[1]))
        elif self.editando == 3:
            self.trigger_desbloqueo.emit(Imagenes(self.orden[2]))
        elif self.editando == 4:
            self.trigger_desbloqueo.emit(Imagenes(self.orden[3]))
        self.editando = 0
        self.viendo = 0
        self.ventana_edicion.close()
        self.show()

    def ver1(self):
        self.viendo = 1
        self.pide_come()
        self.close()
        scaled = self.imagen1.scaled(self.espectador.imagen.size(),
                                     Qt.KeepAspectRatio)
        self.espectador.imagen.setPixmap(scaled)
        self.espectador.show()

    def ver2(self):
        self.viendo = 2
        self.pide_come()
        self.close()
        scaled = self.imagen2.scaled(self.espectador.imagen.size(),
                                     Qt.KeepAspectRatio)
        self.espectador.imagen.setPixmap(scaled)
        self.espectador.show()

    def ver3(self):
        self.viendo = 3
        self.pide_come()
        self.close()
        scaled = self.imagen3.scaled(self.espectador.imagen.size(),
                                     Qt.KeepAspectRatio)
        self.espectador.imagen.setPixmap(scaled)
        self.espectador.show()

    def ver4(self):
        self.viendo = 4
        self.pide_come()
        self.close()
        scaled = self.imagen4.scaled(self.espectador.imagen.size(),
                                     Qt.KeepAspectRatio)
        self.espectador.imagen.setPixmap(scaled)
        self.espectador.show()

    def act_imagenes(self, imagen):
        ima = imagen.ima
        foto = imagen.nro
        nro = self.orden.index(foto)
        if nro == 0:
            self.imagen1 = QPixmap()
            self.imagen1.loadFromData(ima)
            scaled = self.imagen1.scaled(self.ventana_edicion.editada.size(),
                                         Qt.KeepAspectRatio)
            self.ventana_edicion.editada.setPixmap(scaled)
        elif nro == 1:
            self.imagen2 = QPixmap()
            self.imagen2.loadFromData(ima)
            scaled = self.imagen2.scaled(self.ventana_edicion.editada.size(),
                                         Qt.KeepAspectRatio)
            self.ventana_edicion.editada.setPixmap(scaled)
        elif nro == 2:
            self.imagen3 = QPixmap()
            self.imagen3.loadFromData(ima)
            scaled = self.imagen3.scaled(self.ventana_edicion.editada.size(),
                                         Qt.KeepAspectRatio)
            self.ventana_edicion.editada.setPixmap(scaled)
        else:
            self.imagen4 = QPixmap()
            self.imagen4.loadFromData(ima)
            scaled = self.imagen4.scaled(self.ventana_edicion.editada.size(),
                                         Qt.KeepAspectRatio)
            self.ventana_edicion.editada.setPixmap(scaled)

    def desconecta(self):
        try:
            self.ventana_edicion.blurry.clicked.disconnect()
        except Exception:
            pass
        try:
            self.ventana_edicion.blade.clicked.disconnect()
        except Exception:
            pass
        try:
            self.ventana_colores.blanco.clicked.disconnect()
        except Exception:
            pass
        try:
            self.ventana_colores.rojo.clicked.disconnect()
        except Exception:
            pass
        try:
            self.ventana_colores.azul.clicked.disconnect()
        except Exception:
            pass
        try:
            self.ventana_colores.amarillo.clicked.disconnect()
        except Exception:
            pass
        try:
            self.ventana_colores.negro.clicked.disconnect()
        except Exception:
            pass
        try:
            self.ventana_edicion.recortar.clicked.disconnect()
        except Exception:
            pass

    def bloquea(self, evento):
        dict = evento.images
        self.editar1.close()
        self.editar2.close()
        self.editar3.close()
        self.editar4.close()

        if dict[self.orden[0]] == False:
            self.editar1 = QPushButton('Editar', self)
            self.editar1.resize(self.editar1.sizeHint())
            self.editar1.move(50, 230)
            self.editar1.clicked.connect(self.edita1)
        else:
            self.editar1 = QPushButton('Ver', self)
            self.editar1.resize(self.editar1.sizeHint())
            self.editar1.move(50, 230)
            self.editar1.clicked.connect(self.ver1)

        if dict[self.orden[1]] == False:
            self.editar2 = QPushButton('Editar', self)
            self.editar2.resize(self.editar2.sizeHint())
            self.editar2.move(330, 230)
            self.editar2.clicked.connect(self.edita2)
        else:
            self.editar2 = QPushButton('Ver', self)
            self.editar2.resize(self.editar2.sizeHint())
            self.editar2.move(330, 230)
            self.editar2.clicked.connect(self.ver2)

        if dict[self.orden[2]] == False:
            self.editar3 = QPushButton('Editar', self)
            self.editar3.resize(self.editar3.sizeHint())
            self.editar3.move(50, 520)
            self.editar3.clicked.connect(self.edita3)
        else:
            self.editar3 = QPushButton('Ver', self)
            self.editar3.resize(self.editar3.sizeHint())
            self.editar3.move(50, 520)
            self.editar3.clicked.connect(self.ver3)

        if dict[self.orden[3]] == False:
            self.editar4 = QPushButton('Editar', self)
            self.editar4.resize(self.editar4.sizeHint())
            self.editar4.move(320, 520)
            self.editar4.clicked.connect(self.edita4)
        else:
            self.editar4 = QPushButton('Ver', self)
            self.editar4.resize(self.editar4.sizeHint())
            self.editar4.move(320, 520)
            self.editar4.clicked.connect(self.ver4)

        self.editar1.show()
        self.editar2.show()
        self.editar3.show()
        self.editar4.show()




    # revisar los boqueos....

    def descar(self):
        if self.editando == 1 or self.viendo == 1:
            self.trigger_pide_descarga.emit(Imagenes(self.orden[0]))
        elif self.editando == 2 or self.viendo == 2:
            self.trigger_pide_descarga.emit(Imagenes(self.orden[1]))
        elif self.editando == 3 or self.viendo == 3:
            self.trigger_pide_descarga.emit(Imagenes(self.orden[2]))
        elif self.editando == 4 or self.viendo == 4:
            self.trigger_pide_descarga.emit(Imagenes(self.orden[3]))

    def descarga(self, event):
        ima = event.images[0]
        n = event.images[1]
        path = 'downloads/'
        if self.final[self.editando - 1] == self.imagenes[n]:
            print(self.imagenes[n])
            with open(path + self.imagenes[n], 'wb') as file:
                file.write(ima)

    def comenta1(self, event):
        self.ventana_edicion.comentarios.clear()
        self.espectador.comentarios.clear()
        dic = event.lista
        if self.viendo == 1 or self.editando == 1:
            for come in dic[self.orden[0]]:
                self.ventana_edicion.comentarios.addItem(come)
                self.espectador.comentarios.addItem(come)
        elif self.viendo == 2 or self.editando == 2:
            for come in dic[self.orden[1]]:
                self.ventana_edicion.comentarios.addItem(come)
                self.espectador.comentarios.addItem(come)
        elif self.viendo == 3 or self.editando == 3:
            for come in dic[self.orden[2]]:
                self.ventana_edicion.comentarios.addItem(come)
                self.espectador.comentarios.addItem(come)
        elif self.viendo == 4 or self.editando == 4:
            for come in dic[self.orden[3]]:
                self.ventana_edicion.comentarios.addItem(come)
                self.espectador.comentarios.addItem(come)

    def pide_come(self):
        self.trigger_pide_come.emit()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())