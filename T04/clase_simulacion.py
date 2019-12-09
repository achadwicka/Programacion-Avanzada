import funciones as f
from math import floor, ceil
from collections import deque
from clases import *
from random import choice, shuffle, uniform
from estadisticas import *


class Simulacion:

    def __init__(self):
        self.tiempo = 0
        self.compraron = []
        self.dias = 0
        self.mes = 1
        self.alumnos = []
        self.funcionarios = []
        self.vendedores = []
        self.carabineros = []
        self.miembros = []
        self.master_event = [(420, 'nuevo_dia')]
        # es solo alumnos
        self.no_almuerza_mes = []
        self.no_almuerza = 0
        self.vendedores_eliminados = []
        self.vendidos_dia = []
        self.vendidos = []
        self.almuerza12 = 0
        self.almuerza1 = 0
        self.almuerza2 = 0
        self.a = []
        self.abandona_cola = 0
        self.total_sin_stock = 0
        self.proxima_temperatura = self.calculo_prox_temp(0)
        self.proxima_lluvia = self.calculo_prox_lluvia(0)
        self.frio_ext = False
        self.calor_ext = False
        self.concha = False
        self.lluvia = False
        self.ultima_temp = 0
        self.lamda_carabineros = 0
        self.prob_concha = 0
        self.ultima_concha = 0
        self.cantidad_llamadas = 0
        self.cantidad_temperaturas = 0
        self.cantidad_concha = 0
        # aca para ver que imprimir :)
        self.imprimir = True
        self.cant_stock_requisado = 0
        self.enganos_hyde = 0
        self.ultima_lluvia = 0
        self.enganos_jekyll = 0
        self.prod_originales = {}
        self.prod_originales2 = {}
        self.lluvia_ayer = False
        self.lluvias = 0
        self.cantidad_vendedores = 0
        self.vendedores_originales = []
        self.cantidad_requisado_hyde = 0
        self.u_tem = 0
        self.cantidad_requisado_jekyll = 0


    def calculo_prox_temp(self, dia):
        # calcula la proxima fecha de temperatura extrema
        return dia + round(uniform(2, 20))

    def hay_concha(self, prob):
        # calcula si es que hay concha esa semana
        return random() < prob

    def calculo_prox_llamado(self, lamda):
        # calcula el proximo llamado de carabineros
        return round(expovariate(lamda))

    def calculo_prox_lluvia(self, ultima_temp):
        # calcula la proxima lluvia de hamburguesas
        return round(expovariate(1 / (21 - ultima_temp)))

    @property
    def semana(self):
        # retorna la semana actual
        semana = floor(self.tiempo / 7) + 1
        return int(semana)

    def poblar(self, escenario):
        """Metodo que me pobla la simulacion.

        escenario: escenario para poblar la simulacion
        escenario: dict
        """
        self.escenario = escenario
        self.lamda_carabineros = float(escenario['llamado_policial'])
        self.prob_concha = float(escenario['concha_estéreo'])
        self.prox_llamado_policial = self.calculo_prox_llamado(
            self.lamda_carabineros)
        orden = f.orden('personas.csv')
        pos_nombre = orden.index('Nombre')
        pos_apellido = orden.index('Apellido')
        pos_edad = orden.index('Edad')
        pos_preferencias = orden.index('Vendedores de Preferencia')
        pos_entidad = orden.index('Entidad')
        pos_tipo = orden.index('Tipo Comida')
        pos_personalidad = orden.index('Personalidad')

        personas = f.read_file('personas.csv')
        datos_carabineros = list(
            filter(lambda x: x[pos_entidad] == 'Carabinero',
                   personas))
        datos_funcionarios = list(
            filter(lambda x: x[pos_entidad] == 'Funcionario',
                   personas))
        datos_alumnos = list(
            filter(lambda x: x[pos_entidad] == 'Alumno', personas))
        datos_vendedores = list(filter(lambda x: x[pos_entidad] == 'Vendedor',
                                       personas))

        posiciones = f.orden('productos.csv')
        pro = posiciones.index('Producto')
        tip = posiciones.index('Tipo')
        pre = posiciones.index('Precio')
        cal = posiciones.index('Calorias')
        tasa = posiciones.index('Tasa Putrefacción')
        vend = posiciones.index('Vendido en')

        lineas = f.read_file('productos.csv')

        for linea in lineas:
            p = linea
            self.prod_originales[p[pro]] = int(p[pre])
            self.prod_originales2[p[pro]] = 0


        carabineros = {
        str(datos_carabineros[i][pos_nombre] + datos_carabineros[i][
            pos_apellido]): Carabinero(datos_carabineros[i][pos_nombre],
                                       datos_carabineros[i][pos_apellido],
                                       datos_carabineros[i][pos_edad],
                                       datos_carabineros[i][
                                                pos_personalidad], escenario)
        for i in range(len(
            datos_carabineros))}
        funcionarios = {
        str(datos_funcionarios[i][pos_nombre] + datos_funcionarios[
            i][pos_apellido]):
            Funcionario(datos_funcionarios[i][pos_nombre],
                        datos_funcionarios[i][
                            pos_apellido], datos_funcionarios[i][pos_edad],
                        datos_funcionarios[
                            i][pos_preferencias], escenario) for i in
        range(len(
            datos_funcionarios))}
        alumnos = {
        str(datos_alumnos[i][pos_nombre] + datos_alumnos[i][pos_apellido]):
            Alumno(datos_alumnos[i][pos_nombre],
                   datos_alumnos[i][pos_apellido],
                   datos_alumnos[i][pos_edad],
                   datos_alumnos[i][pos_preferencias], escenario) for
        i in
        range(len(datos_alumnos))}
        vendedores = {
        str(datos_vendedores[i][pos_nombre] + datos_vendedores[i][
            pos_apellido]): Vendedor(datos_vendedores[i][pos_nombre],
                                     datos_vendedores[i][pos_apellido],
                                     datos_vendedores[i][pos_edad],
                                     datos_vendedores[i][pos_tipo], escenario) for
            i in
        range(len(datos_vendedores))}

        for i in funcionarios:
            self.funcionarios.append(funcionarios[i])
            self.miembros.append(funcionarios[i])
        for i in alumnos:
            alumnos[i].consulta_mesada = 1
            self.alumnos.append(alumnos[i])
            self.miembros.append(alumnos[i])
        for i in vendedores:
            self.vendedores.append(vendedores[i])
        for i in carabineros:
            self.carabineros.append(carabineros[i])

        # aca le agrego los productos a cada vendedor
        devil = Vendedor('Quick', 'Devil', 100, 'todo', escenario)
        for vende in self.vendedores:
            self.vendedores_originales.append(vende)
            for linea in lineas:
                p = linea
                if p[vend] == 'Puesto de snacks':
                    ele = 'Snack'
                elif p[vend] == 'Puesto de comida china':
                    ele = 'China'
                else:
                    ele = 'Mexicana'
                producto = Producto(p[pro], p[tip], int(p[tasa]), int(p[pre]),
                                    int(p[cal]), ele)
                if producto not in devil.productos:
                    devil.productos.append(producto)
                if vende.tipo_comida == ele:
                    vende.productos.append(producto)

        self.cantidad_vendedores = len(self.vendedores)


    def nuevo_dia(self):
        # funcion que simula un nuevo día y reinicia los parametros
        for vendedor in self.vendedores:
            vendedor.cola = deque()
            if vendedor.vendio == 0:
                vendedor.no_vendio += 1
                vendedor.dias_sin_vender += 1
            if vendedor.stock == 0:
                self.total_sin_stock += 1
            else:
                vendedor.dias_sin_vender = 0
            vendedor.stock = vendedor.cantidad_stock
            vendedor.vendio = 0

            if vendedor.dias_sin_vender >= 20:
                self.vendedores_eliminados.append(vendedor)
                if self.imprimir:
                    print('{} no ha vendido nada durante 20 dias seguidos :('
                         .format(vendedor))
                self.vendedores.remove(vendedor)
                for miembro in self.miembros:
                    if vendedor in miembro.prioridades:
                        miembro.prioridades.remove(vendedor)

        if self.dias % 20 == 0 and self.dias > 0:
            if self.imprimir:
                print('-'*40)
            self.mes += 1
            if self.imprimir:
                print('Comenzó el mes {}'.format(self.mes))
            self.no_almuerza_mes.append(self.no_almuerza)
            self.vendidos.append(self.vendidos_dia)
            self.vendidos_dia = []
            self.no_almuerza = 0

            for alumno in self.alumnos:
                alumno.consulta_mesada = 0

            for vendedor in self.vendedores:
                a = vendedor.sin_stock
                c = vendedor.no_vendio
                for producto in vendedor.productos:
                    if self.imprimir:
                        print('')
                    pra = producto.precio
                    n = True
                    if a != 0 and c != 0:
                        pre = 0.06 * a * pra + pra - 0.05 * c * pra
                    elif a != 0:
                        pre = 0.06 * a * pra + pra
                    elif c != 0:
                        pre = pra - 0.05 * c * pra
                    else:
                        pre = pra
                        n = False
                    por = abs(pra-pre)/100
                    if self.imprimir and n:
                        print('Los precios de {} del vendedor {} cambiaron '
                              'en un {} porciento'.format(producto,
                                                          vendedor, por))
                    if pre < 0.01 * self.prod_originales[str(producto)]:
                        producto.precio = ceil(0.01 * self.prod_originales[
                            str(producto)])
                        if producto.precio == 0:
                            producto.precio = 1
                    else:
                        producto.precio = round(pre)
                if self.imprimir:
                    print('-' * 40)



        self.dias += 1
        self.tiempo = 0
        self.master_event = [(420, 'nuevo_dia')]

        for alumno in self.alumnos:
            alumno.consulta_saldo = 0
            alumno.in_campus = False

        for funcionario in self.funcionarios:
            funcionario.consulta_saldo = 0
            funcionario.in_campus = False
            funcionario.rechazados = 0

        for alumno in self.alumnos:
            self.master_event.append(alumno.tiempo_llegada_campus())
            self.master_event.append(alumno.tiempo_decide_comer())

        for funcionario in self.funcionarios:
            self.master_event.append(funcionario.tiempo_llegada_campus())
            self.master_event.append(funcionario.tiempo_decide_comer())

        for vendedor in self.vendedores:
            vendedor.instalado = False
            self.master_event.append(vendedor.tiempo_instalar())

    def compra_prod(self, vend, persona, tipo):
        """
        simula cuando una persona compra producto
        :param vend: instancia clase vendedor
        :param persona: instancia clase persona
        :param tipo: snack o comida
        :return: la opcion que puede comprar
        """
        opciones = []
        for vendedor in self.vendedores:
            if vendedor == vend:
                for producto in vendedor.productos:
                    if self.concha:
                        prec = producto.precio * 1.25
                    else:
                        prec = producto.precio
                    if tipo != 'Snack':
                        if prec <= persona.saldo and producto.tipo != 'Snack':
                            opciones.append(producto)
                    else:
                        if prec <= persona.saldo and producto.tipo == 'Snack':
                            opciones.append(producto)
        return choice(opciones)

    def compra_prod_func(self, vend, persona, tipo):
        """
        Funcion que elige el producto de mejor calidad para el funcionario
        :param vend: instancia clase vendedor
        :param persona: instancia clase persona
        :param tipo: str snack o otro
        :return: la opcion para el funcionario
        """
        opciones = []
        for vendedor in self.vendedores:
            if vendedor == vend:
                for producto in vendedor.productos:
                    if self.concha:
                        prec = producto.precio * 1.25
                    else:
                        prec = producto.precio
                    if tipo != 'Snack':
                        if prec <= persona.saldo and producto.tipo != 'Snack':
                            opciones.append(producto)
                    else:
                        if prec <= persona.saldo and producto.tipo == 'Snack':
                           opciones.append(producto)
        if len(opciones) != 0:

            maxi = opciones[0]
            for op in opciones:
                if op.calidad(self.tiempo) > maxi.calidad(self.tiempo):
                    maxi = op
            return maxi
        else:
            return None

    def ejecuta_compra(self, pers, vend, tipo, producto, tiempo):
        """
        Esta es la mas importante, modifica todos los datos al efectuar una
        compra
        :param pers: instancia class persona
        :param vend: instancia class vendedor
        :param tipo: alumno o funcionario
        :param producto: instancia class producto
        :param tiempo: tiempo actual
        :return: nada
        """

        if tipo == 'alumno':
            for alumno in self.alumnos:
                if alumno == pers:
                    for vendedor in self.vendedores:
                        if vendedor == vend:
                            if self.concha:
                                prec = producto.precio * 1.25
                            else:
                                prec = producto.precio
                            if vendedor.stock == 0:
                                vendedor.sin_stock += 1
                                continue
                            alumno.saldo -= prec
                            producto.cant_vendidos += 1
                            vendedor.stock -= 1
                            vendedor.vendio = 1
                            self.vendidos_dia.append(producto)
                            self.prod_originales2[str(producto)] += 1

                            if producto.enferma(tiempo, self.frio_ext,
                                            self.calor_ext, self.lluvia_ayer):
                                if self.imprimir:
                                    print('{} lamentablemente se '
                                          'enfermó'.format(alumno))
                                vendedor.enfermos += 1
                                alumno.prioridades.remove(str(vendedor))

        else:
            for funcionario in self.funcionarios:
                if funcionario == pers:
                    for vendedor in self.vendedores:
                        if vendedor == vend:
                            if self.concha:
                                prec = producto.precio * 1.25
                            else:
                                prec = producto.precio
                            if vendedor.stock == 0:
                                vendedor.sin_stock += 1
                                continue
                            funcionario.saldo -= prec
                            vendedor.stock -= 1
                            vendedor.vendio = 1
                            self.vendidos_dia.append(producto)
                            producto.cant_vendidos += 1
                            self.prod_originales2[str(producto)] += 1

                            if producto.enferma(tiempo, self.frio_ext,
                                            self.calor_ext, self.lluvia_ayer):
                                if self.imprimir:
                                    print('{} se enfermó'.format(funcionario))
                                vendedor.enfermos += 1
                                funcionario.prioridades.remove(str(vendedor))

    def agregar_cola(self, persona, vendedor, tipo, producto):
        """
        Agrega a la persona a la cola del vendedor
        :param persona: instancia class persona
        :param vendedor: instancia class vendedor
        :param tipo: alumno o funcionario
        :param producto: instancia class producto
        :return: una tupla con las acciones
        """

        return (len(vendedor.cola) * vendedor.velocidad + self.tiempo,
                 vendedor, persona, 'termina_de_comprar', tipo, producto)

    def puede_comprar(self, persona, vendedor, tipo):
        """
        Funcion que revisa si la persona puede comprar o no
        :param persona: instancia class persona
        :param vendedor: instancia class vendedor
        :param tipo: snack o fondo
        :return: el producto si es que hay y si no, None
        """

        for i in vendedor.productos:
            if self.concha:
                prec = i.precio * 1.25
            else:
                prec = i.precio
            if tipo != 'Snack':
                if prec <= int(persona.saldo) and i.tipo != 'Snack':
                    return i
            else:
                if prec <= int(persona.saldo) and i.tipo == 'Snack':
                    return i
        return None

    def run(self):
        """
        metodo que corre la simulacion
        :return: Nada
        """
        # pueblo todo con los eventos:
        self.nuevo_dia()

        while self.dias <= 8:
            self.u_tem = self.dias - self.ultima_temp
            if self.tiempo == 0:
                # reviso si hay concha
                if self.dias % 5 == 0 and self.hay_concha(self.prob_concha):
                    self.ultima_concha = 0
                    self.concha = True
                    if self.imprimir:
                        print('Hoy hay Concha Acustica! :) en dia {}'.format(
                            self.dias))
                    self.cantidad_concha += 1
                elif self.ultima_concha == 4 and self.dias % 5 == 0:
                    self.concha = True
                    if self.imprimir:
                        print('Hoy hay Concha Acustica! :) en dia {}'
                              .format(self.dias))
                    self.cantidad_concha += 1
                else:
                    self.ultima_concha += 1
                    self.concha = False

                # reviso si hay temperatura extrema
                if self.dias == self.proxima_temperatura:
                    self.cantidad_temperaturas += 1
                    self.ultima_temp = self.dias
                    self.proxima_temperatura = self.calculo_prox_temp(
                        self.dias)
                    # frio intenso
                    if random() > 0.5:
                        if self.imprimir:
                            print('Hoy hay frío extremo :(')
                        self.frio_ext = True
                    # calor intenso
                    else:
                        if self.imprimir:
                            print('Hoy hay calor extremo :(')
                        self.calor_ext = True
                else:
                    self.calor_ext = False
                    self.frio_ext = False

                # reviso si vienen los carabineros

                if self.dias == self.prox_llamado_policial:
                    self.cantidad_llamadas += 1
                    self.prox_llamado_policial = self.dias + \
                                                 self.calculo_prox_llamado(
                                                     self.lamda_carabineros)
                    if self.imprimir:
                        print('Hoy llamaron a los carabineros :S')
                    carab = choice(self.carabineros)
                    self.master_event.append((300, 'Carabinero', str(carab),
                                              'Llegada_carabineros'))

                if self.proxima_lluvia == self.dias:
                    self.lluvias += 1
                    if self.imprimir:
                        print('Hoy hay lluvia de HAMBURGUESAS :P en dia {}'
                          .format(self.dias))
                    self.lluvia = True
                    self.ultima_lluvia = self.dias
                    self.proxima_lluvia = self.dias + self.calculo_prox_lluvia(
                        self.u_tem)

                else:
                    self.lluvia = False

            if self.ultima_lluvia == self.dias - 1:
                self.lluvia_ayer = True
            else:
                self.lluvia_ayer = False

            if self.lluvia:
                self.master_event = [(420, 'nuevo_dia')]
            self.master_event = sorted(self.master_event, key=lambda x:
                                       x[0])
            evento = self.master_event[0]
            self.master_event.pop(0)
            self.tiempo = evento[0]

            if evento[1] == 'nuevo_dia':
                if self.imprimir:
                    print("Termino el dia {0}!\n".format(self.dias))
                self.nuevo_dia()
                continue

            if evento[3] == 'llega_campus':
                if evento[1] == 'Alumno':
                    for alumno in self.alumnos:
                        if alumno == evento[2]:
                            alumno.in_campus = True
                            alumno.hora_snack = alumno.horario_snack(
                                int(evento[0]))
                            if alumno.hora_snack != False:
                                self.master_event.append((alumno.hora_snack,
                                    'Alumno', alumno, 'compra_snack'))
                            break

                else:
                    for funcionario in self.funcionarios:
                        if funcionario == evento[2]:
                            funcionario.in_campus = True
                            funcionario.hora_snack = \
                                funcionario.horario_snack(int(evento[0]))

                            if funcionario.hora_snack != False:
                                self.master_event.append((funcionario.
                                    hora_snack, 'Alumno', funcionario,
                                     'compra_snack'))
                            break

            elif evento[3] == 'decide_comer':
                if evento[1] == 'Alumno':
                    for alumno in self.alumnos:
                        if alumno == evento[2]:
                            if not alumno.in_campus:
                                self.no_almuerza += 1
                                continue
                            else:
                                self.master_event.append(
                                    alumno.tiempo_compra(evento[0],
                                                         'llega_a_comprar'))
                                break
                else:
                    for funcionario in self.funcionarios:
                        if funcionario == evento[2]:
                            if not funcionario.in_campus:
                                self.no_almuerza += 1
                                continue

                            else:
                                self.master_event.append(
                                    funcionario.tiempo_compra(evento[0],
                                                            'llega_a_comprar'))
                                break

            elif evento[3] == 'instala_puesto':
                for vendedor in self.vendedores:
                    if vendedor == evento[2]:
                        if vendedor.dias_para_volver != 0:
                            vendedor.dias_para_volver -= 1
                        else:
                            vendedor.instalado = True

            elif evento[3] == 'llega_a_comprar':
                if evento[1] == 'Alumno':
                    for alumno in self.alumnos:
                        if alumno == evento[2]:
                            lista_elecciones = alumno.prioridades
                            venta = True
                            for elec in lista_elecciones:
                                for vendedor in self.vendedores:
                                    if str(elec) == str(vendedor) and venta:
                                        if not vendedor.instalado or \
                                                vendedor.tipo_comida == \
                                                        'Snack':
                                            continue

                                        elif vendedor.stock == 0:
                                            self.abandona_cola += 1

                                        elif len(vendedor.cola) * \
                                                vendedor.velocidad > \
                                                alumno.paciencia:
                                            self.abandona_cola += 1
                                            alumno.paciencia -= 5
                                            continue
                                        producto = self.puede_comprar(
                                            alumno, vendedor, 'a')
                                        if producto == None:
                                            self.abandona_cola += 1

                                        else:
                                            prod = self.compra_prod(
                                                vendedor, alumno, 'a')
                                            if self.imprimir:
                                                print('{0} ingresa a la cola de: '
                                                      '{1}'.format(alumno,
                                                                   vendedor))
                                            venta = False
                                            vendedor.cola.append(alumno)
                                            self.master_event.append(
                                                self.agregar_cola(alumno,
                                                    vendedor, 'alumno', prod))



                            if venta:
                                almuerza = False
                                if self.imprimir:
                                    print('{0} no puede ingresar a ninguna '
                                          'cola'.format(alumno))
                                for vendedor in self.vendedores:
                                    if vendedor == 'Quick Devil':
                                        p = self.puede_comprar(alumno,
                                                               vendedor, 'a')

                                        if p != None:
                                            almuerza = True
                                            prod = self.compra_prod(
                                                vendedor, alumno, 'a')
                                            self.agregar_cola(alumno,
                                                vendedor, 'alumno', prod)
                                            if self.imprimir:
                                                print('{0} compra {1} en '
                                                      'Quick Devil :('.
                                                      format(alumno, prod))
                                                self.ejecuta_compra(alumno,
                                                    vendedor, 'alumno',
                                                    prod, self.tiempo)

                                if not almuerza:
                                    self.no_almuerza += 1

                else:
                    for funcionario in self.funcionarios:
                        if funcionario == evento[2]:
                            lista_elecciones = funcionario.prioridades
                            venta = True
                            shuffle(lista_elecciones)
                            for elec in lista_elecciones:
                                if funcionario.rechazados == 3:
                                    break
                                for vendedor in self.vendedores:
                                    if str(elec) == str(vendedor) and venta \
                                            and funcionario.ultima_compra != \
                                                    vendedor and \
                                            vendedor.tipo_comida != 'Snack':

                                        if funcionario.rechazados == 3:
                                            break

                                        if not vendedor.instalado:
                                            continue

                                        elif vendedor.stock == 0:
                                            funcionario.rechazados += 1
                                            self.abandona_cola += 1

                                        producto = self.puede_comprar(
                                            funcionario, vendedor, 'a')
                                        if producto == None:
                                            pass
                                        else:
                                            prod = self.compra_prod_func(
                                                vendedor, funcionario, 'a')
                                            venta = False
                                            vendedor.cola.appendleft(
                                                funcionario)
                                            if self.imprimir:
                                                print('{0} ingresa a la cola de: '
                                                      '{1}'.format(funcionario,
                                                                  vendedor))
                                            self.master_event.append(
                                                self.agregar_cola(
                                                    funcionario, vendedor,
                                                    'funcionario', prod))

                            if venta:
                                if self.imprimir:
                                    print('{0} no puede ingresar a ninguna '
                                          'cola'.format(funcionario))
                                for vendedor in self.vendedores:
                                    if vendedor == 'Quick Devil':
                                        for producto in vendedor.productos:
                                            if self.concha:
                                                prec = producto.precio * 1.25
                                            else:
                                                prec = producto.precio
                                            if prec <= funcionario.saldo:
                                                prod = self.compra_prod(
                                                    vendedor, funcionario, 'a')
                                                self.agregar_cola(funcionario,
                                                    vendedor, 'funcionario',
                                                                  prod)
                                                if self.imprimir:

                                                    print('{0} compra {1} en '
                                                          'Quick Devil :('.
                                                          format(funcionario,
                                                                 prod))
                                                    self.ejecuta_compra(
                                                        funcionario, vendedor,
                                                        'funcionairo',
                                                        prod, self.tiempo)

            elif evento[3] == 'termina_de_comprar':

                for vendedor in self.vendedores:
                    if vendedor == evento[1]:
                        vendedor.cola.remove(evento[2])
                        vendedor.vendio = 1
                        break

                self.ejecuta_compra(evento[2], evento[1], evento[4], evento[5],
                                    self.tiempo)
                if self.imprimir:
                    print('{0} {1} su {2} en tiempo = {3}'.format(evento[2],
                                evento[3], evento[5], self.tiempo))

                if 240 <= self.tiempo < 300:
                    self.almuerza12 += 1

                elif 300 <= self.tiempo < 360:
                    self.almuerza1 += 1

                else:
                    self.almuerza2 += 1
                continue

            elif evento[3] == 'compra_snack':
                if evento[1] == 'Alumno':
                    for alumno in self.alumnos:
                        if alumno == evento[2]:
                            lista_elecciones = alumno.prioridades
                            venta = True
                            for elec in lista_elecciones:
                                for vendedor in self.vendedores:
                                    if str(elec) == str(vendedor) and venta:
                                        if vendedor.tipo_comida != 'Snack':
                                            continue

                                        elif not vendedor.instalado:
                                            continue

                                        elif vendedor.stock == 0:
                                            self.abandona_cola += 1

                                        elif len(vendedor.cola) * \
                                                vendedor.velocidad > \
                                                alumno.paciencia:
                                            self.abandona_cola += 1
                                            alumno.paciencia -= 5
                                            continue
                                        producto = self.puede_comprar(
                                            alumno, vendedor, 'Snack')
                                        if producto == None:
                                            self.abandona_cola += 1

                                        else:
                                            self.compraron.append(str(
                                                vendedor))
                                            prod = self.compra_prod(
                                                vendedor, alumno, 'Snack')
                                            if self.imprimir:
                                                print(
                                                    '{0} ingresa a la cola de: '
                                                    '{1}'.format(alumno,
                                                                 vendedor))
                                            venta = False
                                            vendedor.cola.append(alumno)
                                            self.ejecuta_compra(alumno,
                                                vendedor, 'alumno', prod,
                                                                self.tiempo)
                                            vendedor.vendio = 1


                            if venta:
                                almuerza = False
                                if self.imprimir:
                                    print('{0} no puede ingresar a ninguna '
                                          'cola'.format(alumno))
                                for vendedor in self.vendedores:
                                    if vendedor == 'Quick Devil':
                                        print('asd')
                                        p = self.puede_comprar(alumno,
                                                        vendedor, 'Snack')
                                        print(p)
                                        if p != None:
                                            print('dddd')
                                            almuerza = True
                                            prod = self.compra_prod(
                                                vendedor, alumno, 'Snack')
                                            self.agregar_cola(alumno,
                                                              vendedor,
                                                              'alumno', prod)
                                            if self.imprimir:
                                                print('{0} compra {1} en '
                                                      'Quick Devil :('.
                                                      format(alumno, prod))
                                            vendedor.vendio = 1
                                            continue

                                if not almuerza:
                                    self.no_almuerza += 1

                else:
                    for funcionario in self.funcionarios:
                        if funcionario == evento[2]:
                            lista_elecciones = funcionario.prioridades
                            venta = True
                            shuffle(lista_elecciones)
                            for elec in lista_elecciones:
                                if funcionario.rechazados == 3:
                                    break
                                for vendedor in self.vendedores:
                                    if str(elec) == str(vendedor) and venta \
                                            and funcionario.ultima_compra != \
                                            vendedor and vendedor.tipo_comida\
                                            == 'Snack':

                                        if funcionario.rechazados == 3:
                                            break

                                        if not vendedor.instalado:
                                            continue

                                        elif vendedor.stock == 0:
                                            funcionario.rechazados += 1
                                            self.abandona_cola += 1

                                        producto = self.puede_comprar(
                                            funcionario, vendedor, 'Snack')
                                        if producto == None:
                                            pass
                                        else:
                                            prod = self.compra_prod_func(
                                                vendedor, funcionario, 'Snack')
                                            venta = False
                                            vendedor.cola.appendleft(funcionario)
                                            self.ejecuta_compra(funcionario,
                                                    vendedor, 'funcionario',
                                                               prod, self.tiempo)
                                            vendedor.vendio = 1

                            if venta:
                                if self.imprimir:
                                    print('{0} no puede ingresar a ninguna '
                                          'cola'.format(funcionario))
                                almuerza = False
                                for vendedor in self.vendedores:
                                    if vendedor == 'Quick Devil':
                                        for producto in vendedor.productos:
                                            if self.concha:
                                                prec = producto.precio * 1.25
                                            else:
                                                prec = producto.precio
                                            if prec <= funcionario.saldo:
                                                prod = self.compra_prod(
                                                    vendedor, funcionario,
                                                    'Snack')
                                                self.agregar_cola(funcionario,
                                                                  vendedor,
                                                                  'funcionario',
                                                                  prod)
                                                if self.imprimir:
                                                    print('{0} compra {1} en '
                                                          'Quick Devil :('.
                                                          format(funcionario,
                                                                 prod))
                                                almuerza = True
                                                vendedor.vendio = 1
                                                # ver que se descuente
                                                break

            elif evento[3] == 'Llegada_carabineros':
                revis = 0
                try:
                    demora = 40 / len(self.vendedores)
                except:
                    demora = 0
                opciones = [i for i in self.vendedores]
                for carabinero in self.carabineros:
                    if str(carabinero) == evento[2]:
                        shuffle(opciones)
                        for opcion in opciones:
                            vendedor_a_revisar = opciones.pop(0)
                            self.master_event.append((self.tiempo + revis *
                            demora, carabinero, vendedor_a_revisar,
                                                 'revisa_puesto'))
                            revis += 1

            elif evento[3] == 'revisa_puesto':
                for vendedor in self.vendedores:
                    if str(vendedor) == str(evento[2]):
                        for carabinero in self.carabineros:
                            if str(carabinero) == str(evento[1]):
                                if not vendedor.permiso:
                                    a = random()
                                    if not a < carabinero.engano:
                                        if self.imprimir:
                                            print('{0} fue descubierto sin '
                                                  'permiso'.format(vendedor))
                                        vendedor.instalado = False
                                        vendedor.dias_para_volver = \
                                            vendedor.dias_susto
                                        maxi = 0
                                        self.cant_stock_requisado += \
                                            vendedor.stock
                                        for prod in vendedor.productos:
                                            if prod.precio > maxi:
                                                maxi = prod.precio

                                        vendedor.dinero_requisado += \
                                            vendedor.stock * maxi
                                        if carabinero.personalidad == 'Dr. ' \
                                                                      'Jekyll':
                                            self.cantidad_requisado_jekyll \
                                                += vendedor.stock

                                        else:
                                            self.cantidad_requisado_hyde += \
                                                vendedor.stock

                                        for i in vendedor.cola:
                                            # son solo los alumnos los que
                                            # piden en estadisticas
                                            if i in self.alumnos:
                                                self.no_almuerza += 1


                                    else:
                                        if self.imprimir:
                                            print('{0} ha engañado a {1}'.
                                                  format(vendedor, carabinero))
                                        if carabinero.personalidad == 'Dr. ' \
                                                                      'Jekyll':
                                            self.enganos_jekyll += 1
                                        else:
                                            self.enganos_hyde += 1
                                else:
                                    cantidad = round(len(vendedor.productos) *\
                                               carabinero.tasa_revisar)
                                    for i in range(cantidad):
                                        if float(vendedor.productos[i].calidad(
                                                self.tiempo)) < 0.2:
                                            if self.imprimir:
                                                print('A {0} se le encontró '
                                                    'un producto en mal '
                                                    'estado'.format(vendedor))
                                            vendedor.instalado = False
                                            # aca pierden el stock
                                            maxi = 0
                                            self.cant_stock_requisado +=\
                                                vendedor.stock
                                            for prod in vendedor.productos:
                                                if prod.precio > maxi:
                                                    maxi = prod.precio

                                            vendedor.dinero_requisado +=\
                                                vendedor.stock * maxi
                                            for i in vendedor.cola:
                                                if str(i) in self.alumnos:
                                                    self.no_almuerza += 1
                                            if carabinero.personalidad == 'Dr.' \
                                                   ' Jekyll':
                                                self.cantidad_requisado_jekyll \
                                                    += vendedor.stock

                                            else:
                                                self.cantidad_requisado_hyde += \
                                                    vendedor.stock
                                            break

            if self.imprimir:
                print('{0} {1} en tiempo = {2}'.format(evento[2],
                    evento[3], self.tiempo))




