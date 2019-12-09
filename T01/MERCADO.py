import random
from decimal import *
import os.path
from datetime import date, datetime
""" ESTE MODULO CORRESPONDE A LA CLASE MERCADO """


class Mercado:

    def __init__(self, nombre):

        self.moneda1 = nombre[:3]
        self.moneda2 = nombre[3:]
        self.nombre = nombre
        self.ask = []   # DE LA FORMA [NOMBRE USUARIO, CANTIDAD, PRECIO]
        self.bid = []
        self.lista_ordersm = []
        self.ganancia = Decimal()



        # PARA VER MATCH, EN OPEN CREAR LISAS DE BID O ASK CON BID[TYPE] == BID
        # CADA VEZ Q SE ADD ASK O BID SE REVISA.

        with open("orders.csv", "r", encoding="UTF-8") as orders:
            lista_orders = []
            for i in orders:

                b = i.split(",")
                for elem in b:
                    b = b[0].split(";")
                lista_orders.append(b)

            for a in lista_orders:
                a[len(a) - 1] = a[len(a) - 1].rstrip()
            nombres = lista_orders[0]
            order_id = nombres.index('order_id: int')
            date_created = nombres.index('date_created: string')
            price = nombres.index('price: float')
            amount = nombres.index('amount: float')
            date_match = nombres.index('date_match: string')
            ticker = nombres.index('ticker: string')
            tipo = nombres.index('type: string')

            #ACA PODRIAMOS ABRIR ORDERS PARA AGREGAR TODAS LAS ADD Y BID


        for order in lista_orders:

            if order[ticker] == self.nombre:

                self.lista_ordersm.append(order)

                if order[tipo] == "ask":

                    self.ask.append(order)

                elif order[tipo] == "bid":

                    self.bid.append(order)
       #ACA SE GUARDAN LOS ASK Y BID EN CADA MERCADO...

        with open("Currencies.csv", "r", encoding="UTF-8") as monedas:
            lista_monedas = []
            for i in monedas:

                b = i.split(",")
                b = b[0].split(";")
                lista_monedas.append(b)

            for a in lista_monedas:
                a[len(a) - 1] = a[len(a) - 1].rstrip()

            nombres = lista_monedas[0]
            name = nombres.index('name: string')
            symbol = nombres.index('symbol: string')
            lista_monedas.pop(0)
            dcc = [0,0]
            dcc[name] = "DCC CryptoCoin"
            dcc[symbol] = "DCC"
            lista_monedas.append(dcc)
            mercados_totales = []
            for moneda1 in lista_monedas:
                for moneda2 in lista_monedas:
                    if moneda2[symbol] != moneda1[symbol]:
                        nombre_mer = str(moneda1[symbol])+str(moneda2[symbol])
                        self.comision = Decimal(random.random())
                        com = str(self.comision)
                        mercados_totales.append([nombre_mer+","+com])

        if os.path.exists("comisiones.csv") == False:
            with open("comisiones.csv", mode="w", encoding="UTF-8") as file:
                for element in mercados_totales:
                    print(";".join(element), file=file)

        with open("comisiones.csv", "r", encoding="UTF-8") as mercados:
            mercadoscom = []
            ## aca hay un error
            for i in mercados:
                b = i.rstrip()
                b = b.split(",")
                mercadoscom.append(b)

            for mercado in mercadoscom:
                if mercado[0] == self.nombre:
                    self.ganancia = Decimal(mercado[1])

    def match(self):
        with open("orders.csv", "r", encoding="UTF-8") as orders:
            lista_orders = []
            for i in orders:

                b = i.split(",")
                for elem in b:
                    b = b[0].split(";")
                lista_orders.append(b)

            for a in lista_orders:
                a[len(a) - 1] = a[len(a) - 1].rstrip()
            nombres = lista_orders[0]
            order_id = nombres.index('order_id: int')
            date_created = nombres.index('date_created: string')
            price = nombres.index('price: float')
            amount = nombres.index('amount: float')
            date_match = nombres.index('date_match: string')
            ticker = nombres.index('ticker: string')
            tipo = nombres.index('type: string')

        a = []
        for ask in self.ask:

            for bid in self.bid:
                # esto es cuando hay match
                ask[price] = Decimal(ask[price])
                bid[price] = Decimal(bid[price])
                #caso 1
                if ask[price] <= bid[price] and ask[amount] >= bid[amount]:

                    # aca se cambia la fecha
                    bid[date_match] = str(date.today())
                    ask[date_match] = str(date.today())
                    for algo in lista_orders:
                        if algo[order_id] == bid[order_id] or algo[order_id]\
                                == ask[order_id]:
                            if len(algo[date_match]) == 0:
                                algo[date_match] = str(date.today())

                            totala = Decimal(bid[price])*Decimal(bid[amount])\
                                     *self.ganancia

                            cantidad = Decimal(bid[amount])*self.ganancia
                            a = [totala,cantidad]

                            if Decimal(ask[amount]) - Decimal(bid[amount]) \
                                    != 0:
                                ask[amount] = str(Decimal(ask[amount])
                                                  - Decimal(bid[amount]))

                    print("match"+str(order_id))
                    with open("orders.csv", "w", encoding="UTF-8") as file:
                        for cosa in lista_orders:
                                print(";".join(cosa), file=file)
        if len(a) != 0:
            return a

        return []












