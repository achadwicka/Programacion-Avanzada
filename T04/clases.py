from random import triangular, normalvariate, expovariate, random, randint, \
    uniform
from collections import deque
from math import floor, exp
import variables as var


class Persona:
    def __init__(self, nombre, apellido, edad, escenario):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.escenario = escenario

    @property
    def probabilidad(self):
        # retorna un numero entre 0 y 1
        return random()

    def __repr__(self):
        return str(self.nombre + " " + self.apellido)


class Producto:
    def __init__(self, nombre, tipo, tasa_putrefaccion, precio,
                 calorias, vendido_en):
        self.nombre = nombre
        self.vendido_en = vendido_en
        self.tipo = tipo
        self.tasa_putrefaccion = tasa_putrefaccion
        self.precio = precio
        self.calorias = calorias
        self.cant_vendidos = 0

    def __repr__(self):
        return self.nombre

    def putrefaccion(self, tiempo):
        # retorna la putrefaccion del producto
        return 1 - exp(-(tiempo / self.tasa_putrefaccion))

    def calidad(self, tiempo, calor=False):
        # retorna la calidad del producto
        if calor:
            putr = self.putrefaccion(tiempo) * 2
        else:
            putr = self.putrefaccion(tiempo)
        if self.precio == 0:
            self.precio = 1
        return self.calorias * ((1 - putr)**4) / self.precio**(4/5)

    def enferma(self, tiempo, frio, calor, lluvia_ayer):
        # retorna si es que el producto enferma a la persona
        if frio:
            calidad = self.calidad(tiempo)
        elif calor:
            calidad = self.calidad(tiempo, True)
        else:
            calidad = self.calidad(tiempo)

        if calidad < 0.2 and not lluvia_ayer:
            if self.probabilidad < 0.35:
                return True
        elif calidad < 0.2 and lluvia_ayer:
            if self.probabilidad < 0.7:
                return True
        return False

    @property
    def probabilidad(self):
        # retorna una probabilidad
        return var.probabilidad



class Quick_Devil:
    def __init__(self):
        pass


class MiembroUC(Persona):
    def __init__(self, nombre, apellido, edad, prioridades, escenario):
        super().__init__(nombre, apellido, edad, escenario)
        self.prioridades = prioridades
        self.prioridades = self.prioridades.split(' - ')
        self.in_campus = False
        self.rango_horarios = self.escenario[
            'distribución_almuerzo'].split(';')
        self.rango_horarios = list(int(self.rango_horarios[i]) for i
                                   in range(2))
        self.horario_almuerzo = self.elegir_horario(self.probabilidad * 100)
        self.hora_snack = 0




    @property
    def llegada_campus(self):
        # retorna a que hora se llega al campus
        return 180 + round(triangular(0, 240, int(self.escenario[
                                                      'moda_llegada_campus'])))

    @property
    def come_snack(self):
        # retorna si va a comer snack ese dia o no
        if self.probabilidad > 0.5:
            return True
        else:
            return False

    def horario_snack(self, hora_llegada):
        # si come snack, retorna la hora en la que lo hace
        if self.come_snack:
            return round(uniform(hora_llegada, 420))
        else:
            return False

    @property
    def decide_comer(self):
        # retorna un entero distribuido normal a la hora que decide ir a comer
        return round(normalvariate(int(self.horario_almuerzo)+10, 10))

    @property
    def ir_a_comprar(self):
        # retorna un int distribuido exp. de cuanto demora en trasladarse
        lamda = float(self.escenario['traslado_campus'])
        tasa = 1 / lamda
        if round(expovariate(float(lamda))) < float(3 * tasa):
            return round(expovariate(float(lamda)))
        else:
            return round(3 * lamda)


    def elegir_horario(self, value):
        # retorna el horario en que la persona va a comer
        if value < self.rango_horarios[0]:
            return 300
        elif value < self.rango_horarios[1] + self.rango_horarios[0]:
            return 360
        else:
            return 240


class Alumno(MiembroUC):
    def __init__(self, nombre, apellido, edad, prioridades, escenario):
        super().__init__(nombre, apellido, edad, prioridades, escenario)
        self.mesada = round(int(self.escenario['base_mesada']) * (1 + (random(
        ) ** random())) * 20)
        self.saldo = floor(self.mesada / 20)
        self.rango_paciencia = self.escenario[
            'limite_paciencia'].split(';')
        self.rango_paciencia = list(int(self.rango_paciencia[i]) for i
                                   in range(2))
        self.paciencia = randint(self.rango_paciencia[0],
                                 self.rango_paciencia[1])

    @property
    def consulta_mesada(self):
        # retorna la mesada
        return self.mesada

    @consulta_mesada.setter
    def consulta_mesada(self, value):
        # settea la mesada segun los parametros entregados
        self.mesada = round(int(self.escenario['base_mesada']) * (1 + (random(
        )**random())) * 20)
        self.saldo = floor(self.mesada / 20)

    @property
    def consulta_saldo(self):
        # retorna el saldo
        return self.saldo

    @consulta_saldo.setter
    def consulta_saldo(self, value):
        # se settea el saldo segun la mesada disponible
        self.saldo = floor(self.mesada / 20)

    @property
    def consulta_paciencia(self):
        # retorna la paciencia
        return self.paciencia

    @consulta_paciencia.setter
    def consulta_paciencia(self, value):
        # setea paciencia
        self.paciencia = value

    def tiempo_llegada_campus(self):
        # retorna tupla con evento llega a campus
        return (self.llegada_campus, 'Alumno', self, 'llega_campus')

    def tiempo_decide_comer(self):
        # retorna tupla cuando decide comer
        return (self.decide_comer, 'Alumno', self, 'decide_comer')

    def tiempo_compra(self, time, tipo):
        # retorna tupla con evento cuando demora a comer
        return (self.ir_a_comprar + time, 'Alumno', self, tipo)


class Funcionario(MiembroUC):
    def __init__(self, nombre, apellido, edad, prioridades, escenario):
        super().__init__(nombre, apellido, edad, prioridades, escenario)
        self.saldo = int(escenario['dinero_funcionarios'])
        self.ultima_compra = 0
        self.rechazados = 0


    @property
    def consulta_saldo(self):
        # retorna saldo
        return self.saldo

    @consulta_saldo.setter
    def consulta_saldo(self, value):
        # settea saldo segun parametros
        self.saldo = self.saldo = int(self.escenario['dinero_funcionarios'])

    def tiempo_llegada_campus(self):
        # retorna tupla con evento llega campus
        return (self.llegada_campus, 'Funcionario', self, 'llega_campus')

    def tiempo_decide_comer(self):
        # retorna tupla cuando decide comer
        return (self.decide_comer, 'Funcionario', self, 'decide_comer')

    def tiempo_compra(self, time, tipo):
        # retorna tupla cuanto demora en ir a comer
        return (self.ir_a_comprar + time, 'Funcionario', self,
                tipo)


class Vendedor(Persona):
    def __init__(self, nombre, apellido, edad, comida, escenario):
        super().__init__(nombre, apellido, edad, escenario)
        self.tipo_comida = comida
        self.escenario = escenario
        self.instalado = False
        self.cola = deque()
        self.rango_velocidad = self.escenario['rapidez_vendedores'].split(';')
        self.rango_velocidad = [int(self.rango_velocidad[i]) for i in range(2)]
        self.velocidad = randint(self.rango_velocidad[0],
                                 self.rango_velocidad[1])
        self.rango_stock = self.escenario['stock_vendedores'].split(';')
        self.rango_stock = [int(self.rango_stock[i]) for i in range(2)]
        self.precios = {}
        self.dias_susto = int(self.escenario['días_susto'])
        self.prob_permiso = float(self.escenario['probabilidad_permiso'])
        self.permiso = False
        self.sin_stock = 0
        self.stock = self.cantidad_stock
        self.productos = []
        self.vendio = 0
        self.dias_sin_vender = 0
        self.enfermos = 0
        self.dias_para_volver = 0
        self.dinero_requisado = 0
        self.no_vendio = 0

        if self.probabilidad < self.prob_permiso:
            self.permiso = True


    @property
    def instala_puesto(self):
        # retorna cuando instala puesto
        return var.instalar_puestos

    def tiempo_instalar(self):
        # retorna tupla con evento instalar puesto
        return (self.instala_puesto, 'Vendedor', self, 'instala_puesto')

    @property
    def cantidad_stock(self):
        # retorna la cantidad de stock que le queda
        return round(uniform(self.rango_stock[0], self.rango_stock[1]))


class Carabinero(Persona):
    def __init__(self, nombre, apellido, edad, personalidad, escenario):
        super().__init__(nombre, apellido, edad, escenario)
        self.personalidad = personalidad
        self.escenario = escenario
        self.rango_tasas = None
        self.tasa_revisar = None
        self.engano = None

        if self.personalidad == 'Dr. Jekyll':
            self.rango_tasas = escenario['personalidad_jekyll'].split(';')
        else:
            self.rango_tasas = escenario['personalidad_hide'].split(';')
        self.tasa_revisar = float(self.rango_tasas[0])
        self.engano = float(self.rango_tasas[1])


