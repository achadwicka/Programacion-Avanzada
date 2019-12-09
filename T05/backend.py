
# BACKEND T05
# aca va el codigo importante, todos los calculos e informaciones necesarias.
# quizas crear una clase que sea etapa, y cuando el jugador suba de nivel se
#  hace etapa = Etapa(asd). para asi llamar a sus atributos mas facil.

from PyQt5.QtGui import QPixmap, QTransform, QCursor, QIcon, QImage, QBrush,\
    QPalette, QFont
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer, pyqtSignal, QObject, QThread, QRect
from PyQt5.QtWidgets import QLabel, QWidget, QMainWindow, QApplication, \
    QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QProgressBar
from PyQt5.Qt import QTest
from random import uniform, random, expovariate, triangular
import time
import labels
import datetime
import os
from math import sqrt, atan, degrees, sin, cos, radians, floor
from matplotlib import path



class Compra:
    def __init__(self, habilidad, valor):
        self.habilidad = habilidad
        self.valor = valor


class Crear:
    def __init__(self, tamano, posicion):
        self.x = posicion[0]
        self.y = posicion[1]
        self.tamano = tamano


class Move:
    def __init__(self, label, x, y):
        self.label = label
        self.x = x
        self.y = y


class SendLabel:
    def __init__(self, label, objeto):
        self.label = label
        self.objeto = objeto


class Revisa:
    def __init__(self, objeto, radio):
        self.objeto = objeto
        self.radio = radio


class entidad(QThread):

    def __init__(self):
        super().__init__()
        self.tamano = 1
        self.velocidad = 1
        self.bonificaciones = 0
        self.capacidad_ataque = self.cap_ataque
        self.atacar = False

    @property
    def probabilidad(self):
        return random()

    @property
    def vida_maxima(self):
        return self.tamano * 20 + 100 + self.bonificaciones

    @property
    def cap_ataque(self):
        return round(self.tamano * 0.1 * self.vida_maxima, 0)


# revisar movimientos
class principal(entidad):
    mover = pyqtSignal(Move)
    muerte = pyqtSignal()
    crea = pyqtSignal(Crear)
    revisa = pyqtSignal()
    actualiza = pyqtSignal()
    pedir = pyqtSignal()

    def __init__(self, parent, posx, posy):
        super().__init__()
        self.nivel = 1
        self.tamano = 3
        self.velocidad = 1.1 - self.tamano / 10
        self.label = labels.FLabel(parent, self)
        self.label.setGeometry(30, 30, (self.tamano + 1) * 10, (self.tamano +
                                                               1) * 10)
        self.rec = QRect(posx, posy, (self.tamano + 1) * 10, (self.tamano +
                                                               1) * 10)
        self.experiencia = 200
        self.parent = parent
        self.puntaje = 0
        self.position = [posx, posy]
        self.pixmap = QPixmap(os.getcwd() + '/images/p1.png')
        self.pixmap = self.pixmap.scaled(self.tamano * 10, self.tamano * 10)
        self.angulo = radians(90)

        self.degrees = 90
        self.pixmap = self.pixmap.transformed(QtGui.QTransform().rotate(
            self.degrees))
        self.label.setPixmap(self.pixmap)
        self.label.move(posx, posy)


        self.pbar = QProgressBar(parent)
        self.pbar.setGeometry(posx, posy - 8, self.tamano * 10, 9)
        self.vida = self.vida_maxima
        self.pbar.setValue(self.vida / self.vida_maxima * 100)

        self.subio_nivel = False
        self.terminado = False
        self.imagen = 1
        # usar esto para ver si se puede!! hacer un self.path que sea un
        # path.Path que vaya cambiando cada vez que se cambia posicion o
        # geometria del label para asi comparar mas facil :)
        """p = path.Path([(30, 30), (50, 30), (50, 50), (30, 50)])
        print(p.contains_point((49, 32)))
        print(p.contains_point((49, 29)))"""
        # aqui cambiar esto

    def run(self):
        self.label.show()
        self.pbar.show()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.generador_enemigos)
        self.timer.start(self.cantidad() * 1000)
        #self.timer.start(7000)
        self.lifetimer = QTimer(self)
        self.lifetimer.timeout.connect(self.actualizar_vida)
        self.lifetimer.start(50)
        self.ataquetimer = QTimer(self)
        self.ataquetimer.timeout.connect(self.ataque)
        self.ataquetimer.start(10)
        self.atacandotimer = QTimer(self)
        self.atacandotimer.timeout.connect(self.pelea)
        self.ataquetimer.start(50)

        self.mover.connect(self.parent.actualizar_imagen)
        self.crea.connect(self.parent.crea_enemigos)
        self.muerte.connect(self.parent.salir)
        self.timer = QTimer(self)
        self.mover.emit(
            Move(self.label, self.position[0], self.position[1]))
        self.rec = QRect(self.position[0], self.position[1], (self.tamano + 1)
                         * 10, (self.tamano + 1) * 10)
        self.actualiza.connect(self.parent.actualiza_datos)
        # self.pedir.connect(parent.retorna_enemigos)

    def revisar_tiempo(self):
        self.timer.start(self.cantidad() * 1000)
        pass

    def cantidad(self):
        if self.nivel == 1:
            lamda = 1 / 10
        elif self.nivel == 2:
            lamda = 1 / 8
        elif self.nivel == 3:
            lamda = 1 / 6
        elif self.nivel == 4:
            lamda = 1 / 4
        elif self.nivel == 5:
            lamda = 1 / 2

        a = expovariate(lamda)
        return a

    def generador_enemigos(self):
        tamano = self.generador_tamanos()
        posicion = (150,150)
        self.crea.emit(Crear(tamano, posicion))

    def compravida(self):
        if self.puntaje < 700:
            pass
        else:
            self.puntaje -= 700
            self.vida = self.vida * 1.2

    def generador_tamanos(self):
        if self.nivel == 1:
            a = 1
            b = 5
            c = 1
        elif self.nivel == 2:
            a = 1
            b = 6
            c = 3
        elif self.nivel == 3:
            a = 3
            b = 7
            c = 5
        elif self.nivel == 4:
            a = 5
            b = 9
            c = 7
        elif self.nivel == 5:
            a = 7
            b = 10
            c = 9
        tamano = floor(triangular(a, b, c))
        if tamano > 10:
            tamano = 10
        return tamano

    def compravelocidad(self):
        if self.puntaje < 250:
            pass
        else:
            self.puntaje -= 250
            self.velocidad = self.velocidad * 1.1

    def compraataque(self):
        if self.puntaje < 500:
            pass
        else:
            self.puntaje -= 500
            # sube vel ataque

    def pelea(self, objeto):
        enemigo = objeto.persona
        enemigo.vida -= self.cap_ataque
        if enemigo.vida <= 0:
            self.sumar_puntos(enemigo)

    def ataque(self):
        self.revisar()

    def move_right(self):
        self.degrees += 15
        self.angulo = radians(self.degrees)
        string = '/images/p' + str(self.imagen) + '.png'
        self.act_label(string)

    def move_left(self):
        self.degrees -= 15
        self.angulo = radians(self.degrees)
        string = '/images/p' + str(self.imagen) + '.png'
        self.act_label(string)

    def move_front(self):
        if self.imagen == 8:
            self.imagen = 1
        else:
            self.imagen += 1
        string = '/images/p' + str(self.imagen) + '.png'

        self.act_label(string)
        self.mover.emit(Move(self.label, self.label.x() + sin(self.angulo) *
                             10 * self.velocidad, self.label.y() - cos(
            self.angulo) * 10 * self.velocidad))
        self.rec = QRect(self.label.x(), self.label.y(), (self.tamano + 1) *
                         10, (self.tamano + 1) * 10)
        self.pbar.move(self.label.x(), self.label.y() - 8)

    def move_back(self):
        if self.imagen == 1:
            self.imagen = 8
        else:
            self.imagen -= 1
        string = '/images/p' + str(self.imagen) + '.png'
        self.act_label(string)
        self.mover.emit(Move(self.label, self.label.x() - sin(self.angulo) *
                             10 * self.velocidad, self.label.y() + cos(
            self.angulo) * 10 * self.velocidad))
        self.rec = QRect(self.label.x(), self.label.y(), (self.tamano + 1) *
                         10, (self.tamano +1) *10)
        self.pbar.move(self.label.x(), self.label.y() - 8)

    def act_label(self, string):
        self.label.setGeometry(self.label.x(), self.label.y(), (self.tamano +
                                                                1) * 10,
                               (self.tamano + 1) * 10)
        self.pixmap = QPixmap(os.getcwd() + string)
        self.pixmap = self.pixmap.scaled(self.tamano * 10, self.tamano *
                                         10)
        self.pixmap = self.pixmap.transformed(QtGui.QTransform().rotate(
            self.degrees))
        self.label.setPixmap(self.pixmap)
        self.pbar.setGeometry(self.label.x(), self.label.y() - 8,
                              self.tamano * 10, 9)

    def actualizar_vida(self):
        # cambiar TODOS los labels del front
        self.actualiza.emit()
        self.pbar.setValue(self.vida / self.vida_maxima * 100)
        if self.vida <= 0:
            self.label.close()
            self.terminado = True
            self.pbar.close()
            self.muerte.emit()


    def sumar_puntos(self, mato):
        peg = 100 * max(self.tamano - mato.tamano + 3, 1)
        self.experiencia += peg

    # esta es clave!!
    def revisar(self):
        if self.experiencia >= 1000:
            if self.nivel == 5:
                self.muerte.emit()
                return
            self.nivel += 1
            self.subio_nivel = False

            if self.tamano < 10:
                self.tamano += 1
            self.puntaje += self.experiencia
            self.experiencia = 0
            string = '/images/p' + str(self.imagen) + '.png'
            self.act_label(string)

            # cambiar tamaño
        if self.experiencia >= 500 and not self.subio_nivel:
            self.subio_nivel = True
            if self.tamano < 10:
                self.tamano += 1

                string = '/images/p' + str(self.imagen) + '.png'
                self.act_label(string)
        self.velocidad = 1.1 - self.tamano / 10


    @staticmethod
    def distance(x1, y1, x2, y2):
        dist = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
        return dist



class enemigo(entidad):
    mover = pyqtSignal(Move)
    muerto = pyqtSignal(str)
    revisar = pyqtSignal(Revisa)
    def __init__(self, parent, posx, posy, tamano):
        super().__init__()
        self.label = labels.FLabel(parent, self)
        self.tamano = tamano
        self.vida = self.vida_maxima
        self.label.setGeometry(30, 30, (self.tamano + 1) * 10, (self.tamano
                                                                + 1) * 10)
        self.rec = QRect(posx, posy, (self.tamano + 1) * 10, (self.tamano +
                                                          1) * 10)
        self.position = [posx, posy]
        self.pixmap = QPixmap(os.getcwd() + '/images/e1.png')
        self.pixmap = self.pixmap.scaled(self.tamano * 10, self.tamano * 10)
        self.label.setPixmap(self.pixmap)
        self.label.move(posx, posy)
        self.label.show()
        self.pbar = QProgressBar(parent)
        self.pbar.setGeometry(posx, posy - 8, self.tamano * 10, 9)
        self.pbar.setValue(self.vida / self.vida_maxima * 100)
        self.pbar.show()
        self.angulo = radians(0)
        self.degrees = 0
        self.vivo = True
        self.velocidad = 1.1 - self.tamano / 10
        self.imagen = 1
        self.en_guardia = False
        # esto es que el principal es mayor
        self.mayor = 'mayor'
        # esto cambiarlo

        self.lifetimer = QTimer(self)
        self.lifetimer.timeout.connect(self.actualizar_vida)
        self.lifetimer.start(10)
        self.revisatimer = QTimer(self)
        self.revisatimer.timeout.connect(self.revisa_alrededores)
        self.revisatimer.start(1000)
        # aca tambien atacar

        self.mover.connect(parent.actualizar_imagen)
        self.revisar.connect(parent.revisa)
        self.mover.emit(
            Move(self.label, self.position[0], self.position[1]))
        self.rec = QRect(self.position[0], self.position[1], (self.tamano + 1)
                         * 10, (self.tamano + 1) * 10)

    def actualizar_vida(self):
        self.pbar.setValue(self.vida)
        if self.vida <= 0:
            self.label.close()
            self.pbar.close()
            self.vivo = False

    def revisa_alrededores(self):
        self.revisar.emit(Revisa(self, self.rango_vision))
        if self.en_guardia:
            self.caminatimer = QTimer(self)
            if self.mayor == 'mayor':
                pass
            elif self.mayor == 'igual':
                pass
            else:
                pass
        else:
            self.caminar()

    def caminar(self):
        # aca se laggea con el time.sleep, por lo que hare otro thread que
        # se ejecute cuando tenga que caminar, pero en teoria este deberia
        # ser el que funciona
        #time.sleep(1)
        probabilidad = self.probabilidad

        if probabilidad < 0.25:
            self.mover_arriba()
        elif probabilidad < 0.5:
            self.mover_abajo()
        elif probabilidad < 0.75:
            self.mover_derecha()
        else:
            self.mover_izquierda()

    @property
    def rango_vision(self):
        return self.tamano * 30

    @property
    def rango_escape(self):
        return self.rango_vision * 1.5

    @property
    def tiempo_reaccion(self):
        return uniform(0, 1)

    def personaje_vision(self, principal):
        distancia = principal.distance(self.position[0], self.position[1],
                        principal.position[0], principal.position[1])
        if distancia <= self.rango_vision:
            return True
        return False

    def act_label(self, string):
        self.label.setGeometry(self.label.x(), self.label.y(), (self.tamano +
                                                                1) * 10,
                               (self.tamano + 1) * 10)
        self.rec = QRect(self.label.x(), self.label.y(), (self.tamano + 1) *
                         10, (self.tamano +1) * 10)
        self.pixmap = QPixmap(os.getcwd() + string)
        self.pixmap = self.pixmap.scaled(self.tamano * 10, self.tamano *
                                         10)
        self.pixmap = self.pixmap.transformed(QtGui.QTransform().rotate(
            self.degrees))
        self.label.setPixmap(self.pixmap)
        self.pbar.setGeometry(self.label.x(), self.label.y() - 8,
                              self.tamano * 10, 9)

    def run(self):
        pass

    def pelea(self, objeto):
        jugador = objeto.persona
        jugador.vida -= self.cap_ataque

    def mover_arriba(self):
        if self.imagen == 8:
            self.imagen = 1
        else:
            self.imagen += 1
        string = '/images/e' + str(self.imagen) + '.png'

        self.act_label(string)
        self.mover.emit(Move(self.label, self.position[0],
                             self.position[1] - 20 * self.velocidad))
        self.position = (self.label.x(), self.label.y())
        self.rec = QRect(self.position[0], self.position[1], (self.tamano + 1)
                         * 10, (self.tamano + 1) * 10)
        self.pbar.move(self.position[0], self.position[1] - 8)

    def mover_abajo(self):
        if self.imagen == 8:
            self.imagen = 1
        else:
            self.imagen += 1
        string = '/images/e' + str(self.imagen) + '.png'

        self.act_label(string)

        self.mover.emit(Move(self.label, self.position[0],
                             self.position[1] + 20 * self.velocidad))
        self.position = (self.label.x(), self.label.y())
        self.rec = QRect(self.position[0], self.position[1], (self.tamano + 1)
                         * 10, (self.tamano + 1) * 10)
        self.pbar.move(self.position[0], self.position[1] - 8)

    def mover_izquierda(self):
        if self.imagen == 8:
            self.imagen = 1
        else:
            self.imagen += 1
        string = '/images/e' + str(self.imagen) + '.png'

        self.act_label(string)

        self.mover.emit(Move(self.label, self.position[1] - 20 *
                             self.velocidad, self.position[1]))
        self.position = (self.label.x(), self.label.y())
        self.rec = QRect(self.position[0], self.position[1], (self.tamano + 1)
                         * 10, (self.tamano + 1) * 10)
        self.pbar.move(self.position[0], self.position[1] - 8)

    def mover_derecha(self):
        if self.imagen == 8:
            self.imagen = 1
        else:
            self.imagen += 1
        string = '/images/e' + str(self.imagen) + '.png'

        self.act_label(string)
        self.mover.emit(Move(self.label, self.position[1] + 20 *
                             self.velocidad, self.position[1]))
        self.position = (self.label.x(), self.label.y())
        self.rec = QRect(self.position[0], self.position[1], (self.tamano + 1)
                         * 10, (self.tamano + 1) * 10)
        self.pbar.move(self.position[0], self.position[1] - 8)

    def ataque(self, objeto):
        if isinstance(objeto, principal):
            # aca no hace nada
            pass
        # aca hacer como un while objeto.rangovision < diferencia
        pass



