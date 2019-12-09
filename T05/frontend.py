
# FRONTEND T05
# aca vemos la forma de implementarlo en la interfaz.


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from PyQt5.QtGui import QIcon
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, QTimer, QRect
import os
from random import randint
from math import sqrt
import time
import threading

import backend


class Atack:
    def __init__(self, persona):
        self.persona = persona


class Pausa(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("uis/Pausa.ui", self)


class Puntajes(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("uis/puntajes.ui", self)


class Pide(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("uis/pide.ui", self)


class Tienda(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("uis/Tienda.ui", self)
        #self.elem1.setStyleSheet("QWidget {background-image: url("
         #                           "./Assets/puntaje_extra.png) }")


class MainMenu(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("uis/mainmenu.ui", self)
        self.setStyleSheet("QWidget {background-image: url("
                           "./images/oferta.png)}")
        self.label.setStyleSheet('background:transparent')
        self.ranking.setStyleSheet('background:transparent')
        self.comenzar.setStyleSheet('background:transparent')


class MainWindow(QMainWindow):
    move_left = pyqtSignal()
    move_right = pyqtSignal()
    move_front = pyqtSignal()
    move_back = pyqtSignal()
    attack = pyqtSignal(Atack)
    attacke = pyqtSignal(Atack)

    def __init__(self):
        super().__init__()
        self.jugador = backend.principal(self, 50, 50)
        self.enemigo = backend.enemigo(self, 100, 100, 2)
        self.pausado = False
        self.terminado = False
        uic.loadUi("uis/MainWindow.ui", self)
        self.puntajes = []
        self.enemigos = []


        self.setStyleSheet("QMainWindow {background-image: url("
                                    "./images/grass.png)}")


        self.actualiza_datos()
        self.tiendaButton.clicked.connect(self.tienda)
        self.tiendaButton.setShortcut("Ctrl+T")
        self.salirButton.clicked.connect(self.salir)
        self.pauseButton.clicked.connect(self.pause)
        self.pauseButton.setShortcut("Ctrl+S")

        self.ventana_pausa = Pausa()
        self.ventana_puntajes = Puntajes()
        self.ventana_menu = MainMenu()
        self.ventana_tienda = Tienda()
        self.pedir = Pide()



        self.move_back.connect(self.jugador.move_back)
        self.move_front.connect(self.jugador.move_front)
        self.move_right.connect(self.jugador.move_right)
        self.move_left.connect(self.jugador.move_left)

        self.ventana_menu.show()
        self.ventana_menu.comenzar.clicked.connect(self.comenzar)
        self.ventana_menu.ranking.clicked.connect(self.ranking)

        self.attack.connect(self.jugador.pelea)


    def ranking(self):
        self.ventana_menu.close()
        self.actualiza_puntajes()
        self.ventana_puntajes.show()
        self.ventana_puntajes.comenzar.clicked.connect(self.volverme)

    def comenzar(self):
        self.ventana_menu.close()
        self.show()
        self.jugador.run()

    def tienda(self):
        self.hide()
        self.ventana_tienda.show()
        self.ventana_tienda.volver.clicked.connect(self.volver)
        self.ventana_tienda.compra_v.clicked.connect(self.jugador.compravida)
        self.ventana_tienda.compra_m.clicked.connect(
            self.jugador.compravelocidad)
        self.ventana_tienda.compra_a.clicked.connect(
            self.jugador.compraataque)

    def salir(self):
        self.terminado = True
        self.pide_nombre()
        # ver como terminar los threads
        self.hide()

    def pide_nombre(self):
        self.pedir.show()
        self.pedir.guardar.clicked.connect(self.guarda_nombre)

    # edit
    def guarda_nombre(self):
        nombre = self.pedir.rellena.text()
        puntaje = randint(2,11245)
        #puntaje = self.jugador.puntaje
        self.escribir(nombre, puntaje)
        self.actualiza_puntajes()
        self.ventana_puntajes.show()
        self.pedir.close()

    def actualiza_puntajes(self):
        self.puntajes = []
        path = 'resultados.txt'
        if os.path.exists(path):
            with open(path, 'r') as file:
                for linea in file:
                    linea = linea.strip()
                    lin = linea.split(';')
                    self.puntajes.append(lin)
        else:
            pass

        self.ventana_puntajes.label1.setText('0')
        self.ventana_puntajes.label2.setText('0')
        self.ventana_puntajes.label3.setText('0')
        self.ventana_puntajes.label4.setText('0')
        self.ventana_puntajes.label5.setText('0')
        self.ventana_puntajes.label6.setText('0')
        self.ventana_puntajes.label7.setText('0')
        self.ventana_puntajes.label8.setText('0')
        self.ventana_puntajes.label9.setText('0')
        self.ventana_puntajes.label10.setText('0')

        for puntaje in self.puntajes:
            puntaje[0] = int(puntaje[0])

        self.puntajes.sort()
        self.puntajes = self.puntajes[::-1]
        for i in range(len(self.puntajes)):
            if i == 0:
                self.ventana_puntajes.label1.setText('{0} {1}'.format(
                    self.puntajes[i][1], self.puntajes[i][0]))
            elif i == 1:
                self.ventana_puntajes.label2.setText('{0} {1}'.format(
                    self.puntajes[i][1], self.puntajes[i][0]))
            elif i == 2:
                self.ventana_puntajes.label3.setText('{0} {1}'.format(
                    self.puntajes[i][1], self.puntajes[i][0]))
            elif i == 3:
                self.ventana_puntajes.label4.setText('{0} {1}'.format(
                    self.puntajes[i][1], self.puntajes[i][0]))
            elif i == 4:
                self.ventana_puntajes.label5.setText('{0} {1}'.format(
                    self.puntajes[i][1], self.puntajes[i][0]))
            elif i == 5:
                self.ventana_puntajes.label6.setText('{0} {1}'.format(
                    self.puntajes[i][1], self.puntajes[i][0]))
            elif i == 6:
                self.ventana_puntajes.label7.setText('{0} {1}'.format(
                    self.puntajes[i][1], self.puntajes[i][0]))
            elif i == 7:
                self.ventana_puntajes.label8.setText('{0} {1}'.format(
                    self.puntajes[i][1], self.puntajes[i][0]))
            elif i == 8:
                self.ventana_puntajes.label9.setText('{0} {1}'.format(
                    self.puntajes[i][1], self.puntajes[i][0]))
            elif i == 9:
                self.ventana_puntajes.label10.setText('{0} {1}'.format(
                    self.puntajes[i][1], self.puntajes[i][0]))
            else:
                break

    def actualiza_datos(self):

        self.experienceBar.setValue(self.jugador.experiencia // 10)

        self.labelnivel.setText(' Nivel: {}'.format(self.jugador.nivel))
        self.labelprogreso.setText('{}%'.format(self.jugador.experiencia //
                                                10))
        self.labelpuntaje.setText('Puntaje total: {}'.format(
            self.jugador.puntaje))

    def escribir(self, nom, pun):
        path = 'resultados.txt'
        if os.path.exists(path):
            with open(path, 'a') as file:
                file.write(str(pun) + ';' + str(nom) + '\n')
        else:
            with open(path, 'w') as file:
                file.write(str(pun) + ';' + str(nom) + '\n')

    def volverm(self):
        self.ventana_menu.hide()
        self.show()

    def volverme(self):
        self.ventana_puntajes.hide()
        self.ventana_menu.show()

    def volver(self):
        self.ventana_tienda.close()
        self.show()

    def pause(self):
        if self.pause:
            pass
        self.pause = not self.pause
        self.ventana_pausa.show()
        self.ventana_pausa.volver.clicked.connect(self.volverp)

    def volverp(self):
        self.ventana_pausa.close()
        self.show()

    def keyPressEvent(self, event):
        tecla = event.text()
        if tecla == 'w' or tecla == 'W':
            self.move_front.emit()
        if tecla == 'a' or tecla == 'A':
            self.move_left.emit()
        if tecla == 's' or tecla == 'S':
            self.move_back.emit()
        if tecla == 'd' or tecla == 'D':
            self.move_right.emit()

    def crea_enemigos(self, enemigo):
        tamano = enemigo.tamano
        x = enemigo.x
        y = enemigo.y
        a = backend.enemigo(self, x, y, tamano)
        # es necesario?
        #a.start()
        self.enemigos.append(a)



    def start(self):
        pass

    def revisa(self, senal):
        enemigo = senal.objeto
        radio = senal.radio
        x1 = enemigo.label.x()
        y1 = enemigo.label.y()
        x2 = self.jugador.label.x()
        y2 = self.jugador.label.y()
        distancia = self.distance(x1, y1, x2, y2)
        if radio >= distancia:
            enemigo.en_guardia = True
            if enemigo.rec.intersects(self.jugador.rec):
                enemigo.atacar = True
                self.jugador.atacar = True
                self.attacke.connect(enemigo.pelea)
                # aca despues ver lo que tiene que esperar
                self.attacke.emit(Atack(self.jugador))
                self.attack.emit(Atack(enemigo))

            else:
                enemigo.atacar = False
                self.jugador.atacar = False

            if self.jugador.tamano > enemigo.tamano:
                enemigo.mayor = 'mayor'
            elif self.jugador.tamano == enemigo.tamano:
                enemigo.mayor = 'igual'
            else:
                enemigo.mayor = 'menor'
        else:
            enemigo.en_guardia = False


    @staticmethod
    def actualizar_imagen(move):
        lab = move.label
        x = move.x
        y = move.y
        lab.move(move.x, move.y)
        ancho = lab.frameGeometry().width()

        if move.label.x() < 0:
            lab.move(0, move.label.y())

        if move.label.x() > 770 - ancho:
            lab.move(770 - ancho, move.label.y())

        if move.label.y() < 33:
            lab.move(move.label.x(), 33)

        if move.label.y() > 463 - ancho:
            lab.move(move.label.x(), 463 - ancho)




    @staticmethod
    def distance(x1, y1, x2, y2):
        dist = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
        return dist



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.enemigo.start()
    sys.exit(app.exec_())