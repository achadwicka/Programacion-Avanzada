import threading
import socket
import json
import os
import pickle
import funciones as func
import time
import datetime




class Server:

    def __init__(self):

        print("Inicializando servidor...")

        self.host = "localhost"
        self.port = 12345

        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.socket_servidor.bind((self.host, self.port))
        print("Dirección y puerto enlazados..")

        self.socket_servidor.listen()
        print("Servidor escuchando en {}:{}...".format(self.host, self.port))
        thread = threading.Thread(target=self.accept_connections_thread, daemon=True)
        thread.start()

        # lo pongo aca porque se demora un poco :S
        print('Espera mientras se carga...')
        self.imagenes = ['Knightmare.png', 'DragonBall.png',
                         'MickeyMouse.png', 'Mushroom.png']

        self.editando = {0: False, 1: False, 2: False, 3: False}

        self.im1 = func.genera_png(func.retorna_matriz(self.imagenes[0]),
                                    self.imagenes[0])
        self.im2 = func.genera_png(func.retorna_matriz(self.imagenes[1]),
                                    self.imagenes[1])
        self.im3 = func.genera_png(func.retorna_matriz(self.imagenes[2]),
                                    self.imagenes[2])
        self.im4 = func.genera_png(func.retorna_matriz(self.imagenes[3]),
                                    self.imagenes[3])

        self.comentarios = {0: [], 1: [], 2: [], 3: []}

        print("Listo! Servidor aceptando conexiones...")

        self.editor = {}
        self.cantidad = -1
        self.sockets = {}
        self.usuarios = []

        self.leer_datos()

    def accept_connections_thread(self):


        while True:

            client_socket, _ = self.socket_servidor.accept()

            self.cantidad += 1
            self.editor[client_socket] = 'editor_' + str(self.cantidad)
            self.sockets["editor_" + str(self.cantidad)] = client_socket

            print("Servidor conectado a un nuevo cliente...")

            listening_client_thread = threading.Thread(
                target=self.listen_client_thread,
                args=(client_socket,),
                daemon=True
            )
            listening_client_thread.start()

    def listen_client_thread(self, client_socket):
        try:
            while True:
                response_bytes_length = client_socket.recv(4)
                response_length = int.from_bytes(response_bytes_length,
                                                 byteorder="big")

                response = bytearray()

                while len(response) < response_length:
                    response += client_socket.recv(256)

                decoded = pickle.loads(response)

                self.handle_command(decoded, client_socket)


        except (socket.error, BrokenPipeError, ConnectionResetError,
                EOFError):
            # aqui es cuando la persona no apretacerrar sesion sino que
             # cierra con la x
            print('Persona se desconecta')

    def handle_command(self, received, client_socket):
        print("Mensaje Recibido: {}".format(received))

        if received['status'] == 'ingreso':
            self.ingresar(received['data'])

        elif received['status'] == 'registro':
            self.registrarse(received['data'])

        elif received['status'] == 'cerrar_sesion':
            self.cerrar_sesion(received['data'])
            self.send({'status': '', 'data': ''}, client_socket)

        elif received['status'] == 'pide_imagenes':
            self.genera_imagenes()

        elif received['status'] == 'act':
            self.actualiza()

        elif received['status'] == 'bloquear':
            self.bloquea(received['data'])
            self.manda_bloqueos()

        elif received['status'] == 'desbloquear':
            self.desbloquea(received['data'])
            self.manda_bloqueos()

        elif received['status'] == 'edit':
            imagen = received['data'][0]
            tipo = received['data'][1]
            self.editar(imagen, tipo)

        elif received['status'] == 'descarga':
            imagen = received['data']
            if imagen == 0:
                da = [self.im1, 0]
            elif imagen == 1:
                da = [self.im2, 1]
            elif imagen == 2:
                da = [self.im3, 2]
            else:
                da = [self.im4, 3]
            data = {'status': 'descarga', 'data': da}
            for i in range(self.cantidad + 1):
                time.sleep(0.01)
                self.send(data, self.sockets['editor_' + str(i)])

        elif received['status'] == 'coment':
            usuario = received['data'][1][0]
            text = received['data'][1][1]
            nro = received['data'][0]
            texto = str(datetime.datetime.today()).split('.')[0] + '| ' + \
                    str(usuario) + '| ' + str(text)

            if nro == 0:
                self.comentarios[0].append(texto)
            elif nro == 1:
                self.comentarios[1].append(texto)
            elif nro == 2:
                self.comentarios[2].append(texto)
            else:
                self.comentarios[3].append(texto)

            self.escribir()
            self.comenta()

        elif received['status'] == 'pide_com':
            self.comenta()

        elif received['status'] == 'nombre':
            self.cerrar_sesion(received['data'])

    @staticmethod
    def send(value, socket):

        try:
            msg_bytes = pickle.dumps(value)

            msg_length = len(msg_bytes).to_bytes(4, byteorder="big")

            socket.send(msg_length + msg_bytes)

        # si el cliente se habia desconectado
        except BrokenPipeError:
            pass

    def revisar(self, nombre):
        if nombre.isalnum():
            if len(nombre) > 2:
                self.usuarios.append(nombre)
                data = {'status': 'cerrar_ventana1', 'data': self.usuarios}
                time.sleep(0.01)
                self.send(data, self.sockets['editor_' + str(self.cantidad)])

                return True
            else:
                self.levantar_advertencia('maximo')
        else:
            self.levantar_advertencia('tipo')

    def levantar_advertencia(self, tipo):
        if tipo == 'tipo':
            data = {'status': 'mostrar_ventana', 'data': 'pop_up_tipo'}
        elif tipo == 'maximo':
            data = {'status': 'mostrar_ventana', 'data': 'pop_up_maximo'}
        elif tipo == 'noexiste':
            data = {'status': 'mostrar_ventana', 'data': 'pop_up_noexiste'}
        elif tipo == 'conectado':
            data = {'status': 'mostrar_ventana', 'data': 'pop_up_conectado'}
        else:
            data = {'status': 'mostrar_ventana', 'data': 'pop_up_existe'}

        time.sleep(0.01)
        self.send(data, self.sockets['editor_' + str(self.cantidad)])

    def ingresar(self, nombre):
        if nombre in self.usuarios:
            self.levantar_advertencia('conectado')
            return
        path = 'usuarios.txt'
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as file:
                usuarios = list(a.strip() for a in file)
            if nombre not in usuarios:
                self.levantar_advertencia('noexiste')
            else:
                self.usuarios.append(nombre)
                data = {'status': 'cerrar_ventana1', 'data': self.usuarios}
                time.sleep(0.01)
                self.send(data, self.sockets['editor_' + str(self.cantidad)])
                self.manda_bloqueos()

        else:
            self.levantar_advertencia('noexiste')

    def registrarse(self, nombre):
        path = 'usuarios.txt'
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as file:
                usuarios = list(a.strip() for a in file)

            if nombre not in usuarios:
                if self.revisar(nombre):
                    with open(path, 'a') as file:
                        file.write(str(nombre) + '\n')
                        self.manda_bloqueos()
            else:
                self.levantar_advertencia('existe')

        else:
            if self.revisar(nombre):
                with open(path, 'w') as file:
                    file.write(str(nombre) + '\n')
            else:
                self.levantar_advertencia('tipo')

    def cerrar_sesion(self, nombre):
        self.usuarios.remove(nombre)
        self.actualiza()

    def bloquea(self, imagen):
        self.editando[int(imagen)] = True

    def manda_bloqueos(self):
            for i in range(self.cantidad + 1):
                data = {'status': 'bloqueadas', 'data': self.editando}
                time.sleep(0.01)
                self.send(data, self.sockets['editor_' + str(i)])

    def desbloquea(self, imagen):
        self.editando[int(imagen)] = False

    def genera_imagenes(self):

        data = {"status": 'imagenes', "data": [self.im1, self.im2, self.im3,
                                               self.im4]}
        time.sleep(0.01)
        self.send(data, self.sockets['editor_' + str(self.cantidad)])

    def actualiza(self):
        for i in range(self.cantidad + 1):
            data = {'status': 'actualizar', 'data': self.usuarios}
            time.sleep(0.01)
            self.send(data, self.sockets['editor_' + str(i)])

    def editar(self, imagen, tipo):
        ed = tipo[0]

        if ed == 'blurry':
            if imagen == 0:
                im = 'Knightmare.png'
                matr = func.retorna_matriz(im)
                final = func.blurry(matr)
                self.im1 = func.genera_png(final, im)
            elif imagen == 1:
                im = 'DragonBall.png'
                matr = func.retorna_matriz(im)
                final = func.blurry(matr)
                self.im2 = func.genera_png(final, im)
            elif imagen == 2:
                im = 'MickeyMouse.png'
                matr = func.retorna_matriz(im)
                final = func.blurry(matr)
                self.im3 = func.genera_png(final, im)
            else:
                im = 'Mushroom.png'
                matr = func.retorna_matriz(im)
                final = func.blurry(matr)
                self.im4 = func.genera_png(final, im)

        elif ed == 'blade':
            color = tipo[1]
            if imagen == 0:
                im = 'Knightmare.png'
                matr = func.retorna_matriz(im)
                final = func.blade(matr, color, [255, 255, 255])
                self.im1 = func.genera_png(final, im)
            elif imagen == 1:
                im = 'DragonBall.png'
                matr = func.retorna_matriz(im)
                final = func.blade(matr, color, [255, 255, 255])
                self.im2 = func.genera_png(final, im)
            elif imagen == 2:
                im = 'MickeyMouse.png'
                matr = func.retorna_matriz(im)
                final = func.blade(matr, color, [255, 255, 255])
                self.im3 = func.genera_png(final, im)
            else:
                im = 'Mushroom.png'
                matr = func.retorna_matriz(im)
                final = func.blade(matr, color, [255, 255, 255])
                self.im4 = func.genera_png(final, im)

        elif ed == 'recorta':
            if imagen == 0:
                im = 'Knightmare.png'
                matr = func.retorna_matriz(im)
                final = func.recorta(matr)
                self.im1 = func.genera_png(final, im)
            elif imagen == 1:
                im = 'DragonBall.png'
                matr = func.retorna_matriz(im)
                final = func.recorta(matr)
                self.im2 = func.genera_png(final, im)
            elif imagen == 2:
                im = 'MickeyMouse.png'
                matr = func.retorna_matriz(im)
                final = func.recorta(matr)
                self.im3 = func.genera_png(final, im)
            else:
                im = 'Mushroom.png'
                matr = func.retorna_matriz(im)
                final = func.recorta(matr)
                self.im4 = func.genera_png(final, im)

        self.escribir()
        self.act_imagenes(imagen, [self.im1, self.im2, self.im3, self.im4])

    def act_imagenes(self, nro, img):
        for i in range(self.cantidad + 1):
            data = {'status': 'act_img', 'data': [nro, img]}
            time.sleep(0.01)
            self.send(data, self.sockets['editor_' + str(i)])

    def leer_datos(self):
        path = 'act/'
        path1 = 'comentarios.txt'

        with open(path + self.imagenes[0], 'rb') as file:
            ima = file.read()
            imagen1 = bytearray(ima)

        with open(path + self.imagenes[1], 'rb') as file:
            ima = file.read()
            imagen2 = bytearray(ima)

        with open(path + self.imagenes[2], 'rb') as file:
            ima = file.read()
            imagen3 = bytearray(ima)

        with open(path + self.imagenes[3], 'rb') as file:
            ima = file.read()
            imagen4 = bytearray(ima)

        self.im1 = imagen1
        self.im2 = imagen2
        self.im3 = imagen3
        self.im4 = imagen4

        if os.path.exists(path1):
            with open(path1, 'r', encoding='utf-8') as file:
                ca = [come.strip() for come in file]
                comentarios = [come.split(',') for come in ca]

            self.comentarios[0] = comentarios[0]
            self.comentarios[1] = comentarios[1]
            self.comentarios[2] = comentarios[2]
            self.comentarios[3] = comentarios[3]

    # al final tengo que hacer que se guarden siempre bien...
    def escribir(self):
        a = 'act/'
        path = 'comentarios.txt'
        with open(a + self.imagenes[0], 'wb') as file:
            file.write(self.im1)
        with open(a + self.imagenes[1], 'wb') as file:
            file.write(self.im2)
        with open(a + self.imagenes[2], 'wb') as file:
            file.write(self.im3)
        with open(a + self.imagenes[3], 'wb') as file:
            file.write(self.im4)

        with open(path, 'w') as file:
            com1 = ','.join(self.comentarios[0])
            com2 = ','.join(self.comentarios[1])
            com3 = ','.join(self.comentarios[2])
            com4 = ','.join(self.comentarios[3])
            file.write(com1 + '\n')
            file.write(com2 + '\n')
            file.write(com3 + '\n')
            file.write(com4 + '\n')

    def comenta(self):
        data = {'status': 'add_com', 'data': self.comentarios}
        for i in range(self.cantidad + 1):
            time.sleep(0.01)
            self.send(data, self.sockets['editor_' + str(i)])


if __name__ == "__main__":


    server = Server()

    # Mantenemos al server corriendo
    while True:
        pass