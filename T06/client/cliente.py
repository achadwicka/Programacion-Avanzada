
import threading
import socket
import json
from PyQt5.QtCore import pyqtSignal, QObject
from eventos import *
import pickle
import time


class Client(QObject):

    # Señal para avisar cuando llegan resultados del servidor
    trigger_cerrar = pyqtSignal(Ventanas)
    trigger_abrir = pyqtSignal(Ventanas)
    trigger_images = pyqtSignal(Imagenes)
    trigger_actualiza = pyqtSignal(Lista)
    trigger_act_edit = pyqtSignal(Actualiza_edit)
    trigger_bloqueos = pyqtSignal(Imagenes)
    trigger_descarga = pyqtSignal(Imagenes)
    trigger_coment = pyqtSignal(Lista)

    def __init__(self, window=None):

        super().__init__()
        self.trigger_cerrar.connect(window.cerrar_ventana)
        self.trigger_abrir.connect(window.abrir_ventana)
        self.trigger_images.connect(window.genera_imagenes)
        self.trigger_act_edit.connect(window.act_imagenes)
        self.trigger_actualiza.connect(window.actualiza)
        self.trigger_bloqueos.connect(window.bloquea)
        self.trigger_descarga.connect(window.descarga)
        self.trigger_coment.connect(window.comenta1)
        print("Inicializando cliente...")

        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket = self.socket_cliente

        self.host = "localhost"
        self.port = 12345


        try:


            self.socket_cliente.connect((self.host, self.port))
            print("Cliente conectado exitosamente al servidor...")

            self.connected = True


            thread = threading.Thread(target=self.listen_thread, daemon=True)
            thread.start()
            print("Escuchando al servidor...")

        except ConnectionRefusedError:
            # Si la conexión es rechazada, entonces se 'cierra' el socket
            print("Conexión terminada")
            self.socket_cliente.close()
            exit()

    def pide(self):
        data = {"status": 'pide_imagenes', "data": ''}
        self.send(data)

    def listen_thread(self):

        while self.connected:
            response_bytes_length = self.socket_cliente.recv(4)
            response_length = int.from_bytes(response_bytes_length,
                                             byteorder="big")

            response = bytearray()

            while len(response) < response_length:
                response += self.socket_cliente.recv(256)

            decoded = pickle.loads(response)


            self.handlecommand(decoded)

    def handlecommand(self, decoded):


        print("Mensaje Recibido: {}".format(decoded))



        if decoded['status'] == 'cerrar_ventana':
            self.trigger_cerrar.emit(Ventanas(decoded['data']))

        elif decoded['status'] == 'mostrar_ventana':
            self.trigger_abrir.emit(Ventanas(decoded['data']))

        elif decoded['status'] == 'imagenes':
            self.trigger_images.emit(Imagenes(decoded['data']))

        elif decoded['status'] == 'actualizar':
            self.trigger_actualiza.emit(Lista(decoded['data']))
            time.sleep(0.01)
            self.send({'status': 'respuesta', 'data': ''})

        elif decoded['status'] == 'cerrar_ventana1':
            self.trigger_actualiza.emit(Lista(decoded['data']))
            self.trigger_cerrar.emit(Ventanas('ventana_ingreso'))
            time.sleep(0.01)
            self.send({'status': 'act', 'data': ''})


        elif decoded['status'] == 'act_img':
            pos = decoded['data'][0]
            self.trigger_images.emit(Imagenes(decoded['data'][1]))
            self.trigger_act_edit.emit(Actualiza_edit(pos, decoded[
                'data'][1][pos]))

        elif decoded['status'] == 'bloqueadas':
            self.act_bloqueo(decoded['data'])

        elif decoded['status'] == 'descarga':
            self.download(decoded['data'])

        elif decoded['status'] == 'add_com':
            self.comentarios(decoded['data'])

    def bloqueo(self, event):
        imagen = event.images
        data = {'status': 'bloquear', 'data': imagen}
        time.sleep(0.01)
        self.send(data)

    def act_bloqueo(self, diccionario):
        self.trigger_bloqueos.emit(Imagenes(diccionario))

    def send(self, msg):

        msg_bytes = pickle.dumps(msg)
        msg_length = len(msg_bytes).to_bytes(4, byteorder="big")
        self.socket_cliente.send(msg_length + msg_bytes)

    def desbloqueo(self, event):
        ima = event.images
        data = {'status': 'desbloquear', 'data': ima}
        time.sleep(0.01)
        self.send(data)

    def edit(self, evento):
        imagen = evento.imagen
        tipo = evento.tipo
        time.sleep(0.01)
        self.send({'status': 'edit', 'data': [imagen, tipo]})

    def descarga(self, event):
        imagen = event.images
        time.sleep(0.01)
        self.send({'status': 'descarga', 'data': imagen})

    def download(self, imagen):
        self.trigger_descarga.emit(Imagenes(imagen))

    def comenta(self, event):
        nro = event.ima
        texto = event.nro
        data = {'status': 'coment', 'data': [nro, texto]}
        time.sleep(0.01)
        self.send(data)

    def comentarios(self, comentarios):
        self.trigger_coment.emit(Lista(comentarios))

    def pidecom(self):
        data = {'status': 'pide_com', 'data': ''}
        time.sleep(0.01)
        self.send(data)

    def nombre1(self, event):
        nombre = event.lista
        data = {'status': 'nombre', 'data': nombre}
        time.sleep(0.01)
        self.send(data)

    def envio_cliente(self, event):
        data = {"status": event.tipo, "data": event.nombre}
        time.sleep(0.01)
        self.send(data)
        # esta señal se recibe de la interfaz, y se tiene que enviar un
        # socket al server para que revise el contenido...





