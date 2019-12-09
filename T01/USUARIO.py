from datetime import date, datetime
from MERCADO import *
from decimal import *
import random
""" CLASE USUARIO """


class Usuario:

    def __init__(self, Nombre_usuario, Nombre, Apellido, Fecha_nacimiento,
                 orders):

        self.Nombre_usuario = Nombre_usuario
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Fecha_nacimiento = Fecha_nacimiento
        self.orders = orders
        self.mercados = []
        self.tipo = ""
        self.mercados_totales = []
        self.ask = []
        self.bid = []
        self.matches = []
        #este es el que tengo para invertir
        self.dinero = []
        self.matches_ask = []
        self.matches_bid = []
        # este es el real, el que tiene en el banco, el de match
        self.dinero_disponible = []

        #aca vemos todas las orders del usuario, aunque esten con match
        with open("orders.csv", "r", encoding="UTF-8") as orders:
            lista_orders = []
            for i in orders:

                b = i.split(",")
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

        self.monedas()


        for numero in lista_orders:
            if numero[order_id] in self.orders:
                if numero[ticker] not in self.mercados:
                    self.mercados.append(numero[ticker])

        # ACA AGREGO TODOS LOS MERCADOS A MATCH, ASK O BID ACTIVOS...
        # ver que sea de mis orders... no de mis mercados! porq tengo varios
        for order in lista_orders:

            if order[order_id] in self.orders:

                if len(order[date_match]) != 0:

                    self.matches.append(order)

                    if order[tipo] == "ask":

                        self.matches_ask.append(order)

                    elif order[tipo] == "bid":

                        self.matches_bid.append(order)

                elif order[tipo] == "ask":

                    self.ask.append(order)

                elif order[tipo] == "bid":

                    self.bid.append(order)


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
            dcc = [0, 0]
            dcc[name] = "DCC CryptoCoin"
            dcc[symbol] = "DCC"
            lista_monedas.append(dcc)


            for moneda1 in lista_monedas:
                for moneda2 in lista_monedas:
                    if moneda2[symbol] != moneda1[symbol]:
                        nombre_mer = str(moneda1[symbol])+str(moneda2[symbol])
                        self.mercados_totales.append(nombre_mer)

    def actualizar(self):

        self.monedas()


        with open("banco.csv", "r", encoding="UTF-8") as dinero:
            nombres = []
            banco = []
            for i in dinero:
                banco.append(i)
                if i[0] != "[":
                    i = i[:-1]
                    nombres.append(i)



        if self.Nombre_usuario not in nombres:

            a = 1


        else:
            with open("banco.csv", "r", encoding="UTF-8") as dinero:
                listaa = []
                string = ""
                for j in dinero:
                    if j != "\n":
                        string += j
                        listaa.append(j)


            todo = string.split()
            for i in range(len(todo)):
                if todo[i] == self.Nombre_usuario:
                    a = i
                    i+=1
                else:
                    i+=1
            cosas = []
            posicion = a

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

                dcc = [0, 0]
                dcc[name] = "DCC CryptoCoin"
                dcc[symbol] = "DCC"
                if dcc not in lista_monedas:
                    lista_monedas.append(dcc)


            self.monedas()

            for o in range(posicion, posicion + len(lista_monedas)*4 + 1):
                cosas.append(todo[o])
                pass

            for a in range(len(cosas)):
                cosas[a] = cosas[a].replace("[","")
                cosas[a] = cosas[a].replace("]", "")
                cosas[a] = cosas[a].replace(",", "")
                cosas[a] = cosas[a].replace("'", "")

            self.dinero = []
            self.dinero_disponible = []
            cosas.pop(0)
            d = 0
            i = 0
            for algo in range(len(cosas)//4):
                i += 1
                self.dinero_disponible.append([cosas[d],cosas[d+1]])
                d += 2
            d = 0
            for algo in range(i,len(cosas)//2):
                self.dinero.append([cosas[d],cosas[d+1]])
                d +=2

            a = 0



        if a == 1:

            # lo que gana y lo que pierde por match hecho
            # si vende algo se asume que tenia y queda con 0
            # suponiendo que tenia justo la cantidad que vendio

            # esta misma me va a servir despues para la funcion match

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

                dcc = [0, 0]
                dcc[name] = "DCC CryptoCoin"
                dcc[symbol] = "DCC"
                if dcc not in lista_monedas:
                    lista_monedas.append(dcc)

            if len(self.dinero_disponible) == 0:
                for i in range(len(lista_monedas)):
                    self.dinero.append([lista_monedas[i][symbol]])
                    self.dinero_disponible.append([lista_monedas[i][symbol]])

                for monedas in self.dinero:
                    monedas.append(str(Decimal(0)))

                for monedas in self.dinero_disponible:
                    monedas.append(str(Decimal(0)))

            with open("orders.csv", "r", encoding="UTF-8") as orders:
                lista_orders = []
                for i in orders:
                    b = i.split(",")
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

            for match in self.matches_bid:


                # en los bid se suma cantidad en moneda
                mercado = Mercado(match[ticker])
                if self.tipo == "Investor":
                    ganancia = Decimal(mercado.ganancia/2)

                else:
                    ganancia = Decimal(mercado.ganancia)

                mercado = Mercado(match[ticker])
                cantidad = Decimal(match[amount]) * ganancia
                precio = Decimal(match[price]) * ganancia
                total = (cantidad * precio) * ganancia
                moneda1 = mercado.moneda1
                moneda2 = mercado.moneda2



                for monedas in self.dinero:

                    if monedas[0] == moneda1:

                        monedas[1] = Decimal(monedas[1])
                        cantidad = Decimal(cantidad)
                        monedas[1] += cantidad
                        monedas[1] = str(monedas[1])

                for monedas in self.dinero_disponible:


                    if monedas[0] == moneda1:

                        monedas[1] = Decimal(monedas[1])
                        cantidad = Decimal(cantidad)
                        monedas[1] += cantidad
                        monedas[1] = str(monedas[1])


                # esto pierde
                for monedas in self.dinero:

                    if monedas[0] == moneda2:

                        monedas[1] = Decimal(monedas[1])
                        total = Decimal(total)
                        monedas[1] -= total

                        if monedas[1] < 0:
                            monedas[1] = Decimal(0)

                        monedas[1] = str(monedas[1])

                for monedas in self.dinero_disponible:

                    if monedas[0] == moneda2:

                        monedas[1] = Decimal(monedas[1])
                        total = Decimal(total)
                        monedas[1] -= total

                        if monedas[1] < 0:
                            monedas[1] = Decimal(0)

                        monedas[1] = str(monedas[1])

            for match in self.matches_ask:

                # en los ask se suma mult en mon 2 y resta en mon1

                mercado = Mercado(match[ticker])
                if self.tipo == "Investor":
                    ganancia = Decimal(mercado.ganancia / 2)

                else:
                    ganancia = Decimal(mercado.ganancia)
                cantidad = Decimal(match[amount]) * ganancia
                precio = Decimal(match[price]) * ganancia
                total = (cantidad * precio) * ganancia
                moneda1 = mercado.moneda1
                moneda2 = mercado.moneda2

                # esto gana

                for monedas in self.dinero:


                    if monedas[0] == moneda2:

                        monedas[1] = Decimal(monedas[1])
                        total = Decimal(total)
                        nuevo = monedas[1] + total
                        monedas[1] = str(nuevo)

                for monedas in self.dinero_disponible:

                    if monedas[0] == moneda2:

                        monedas[1] = Decimal(monedas[1])
                        total = Decimal(total)
                        nuevo = monedas[1] + total
                        monedas[1] = str(nuevo)

                # esto pierde
                for monedas in self.dinero:


                    if monedas[0] == moneda1:

                        monedas[1] = Decimal(monedas[1])
                        cantidad = Decimal(cantidad)
                        monedas[1] -= cantidad
                        if monedas[1] < 0:

                            monedas[1] = Decimal(0)

                        monedas[1] = str(monedas[1])

                for monedas in self.dinero_disponible:


                    if monedas[0] == moneda1:

                        monedas[1] = Decimal(monedas[1])
                        cantidad = Decimal(cantidad)
                        monedas[1] -= cantidad
                        if monedas[1] < 0:

                            monedas[1] = Decimal(0)

                        monedas[1] = str(monedas[1])

            for ask in self.ask:
                mercado = Mercado(ask[ticker])
                if self.tipo == "Investor":

                    ganancia = Decimal(mercado.ganancia / 2)

                else:
                    ganancia = Decimal(mercado.ganancia)

                cantidad = Decimal(ask[amount]) * ganancia
                precio = Decimal(ask[price]) * ganancia
                total = (cantidad * precio) * ganancia
                moneda1 = mercado.moneda1

                # parece q me lo esta tirando al revez
                for monedas in self.dinero:

                    if monedas[0] == moneda1:


                        monedas[1] = Decimal(monedas[1])
                        cantidad = Decimal(cantidad)
                        monedas[1] -= cantidad
                        if monedas[1] < 0:

                            monedas[1] = Decimal(0)



                for bid in self.bid:


                    mercado = Mercado(bid[ticker])
                    if self.tipo == "Investor":
                        ganancia = Decimal(mercado.ganancia / 2)

                    else:
                        ganancia = Decimal(mercado.ganancia)
                    cantidad = Decimal(bid[amount]) * ganancia
                    precio = Decimal(bid[price]) * ganancia
                    total = (cantidad * precio) * ganancia
                    moneda1 = mercado.moneda1
                    moneda2 = mercado.moneda2

                    for monedas in self.dinero:

                        if monedas[0] == moneda2:

                            monedas[1] = Decimal(monedas[1])
                            total = Decimal(total)
                            monedas[1] -= total

                            if monedas[1] < 0:
                                monedas[1] = Decimal(0)


                for a in self.dinero:

                    a[1] = str(a[1])

                for a in self.dinero_disponible:
                    a[1] = str(a[1])


                with open("banco.csv", mode="w", encoding="UTF-8") as file:

                    banco.append(self.Nombre_usuario)
                    banco.append(self.dinero_disponible)
                    banco.append(self.dinero)
                    for cosa in banco:
                        if cosa != "\n":

                            print("".join(str(cosa)),file=file)




        # EN VERDAD SOLO NECESITO GUARDAR LO QUE TIENE FUERA DE ASK Y BID
        # MAS LO QUE SE GUARDA... ENTOCNES SOLO SUBO EL Q NO TIENE ASK Y
        # BID.. Y SE L SUMO DESPUES AL Q ME DESCARGO CN ASK Y BID




                #for a in mercadoscom:
                    #a[len(a) - 1] = a[len(a) - 1].rstrip()

                #for mercado in mercadoscom:
                    #if mercado[0] == self.nombre:
                        #self.ganancia = mercado[1]

    # aca ver todos los mercados y cambiar a int los precios... en ask son solo moneda 1 en bid son la multiplicacion

        # aca vamos a definir el tipo antes que todo, ya define underaged

        with open("users.csv", "r", encoding="UTF-8") as users:
            lista_usuarios = []
            for i in users:
                b = i.split(",")
                b = b[0].split(";")
                lista_usuarios.append(b)

        nombres = lista_usuarios[0]
        for a in lista_usuarios:
            a[len(a) - 1] = a[len(a) - 1].rstrip()

        if len(nombres) == 5:
            lista_usuarios[0].append("tipo_user:string")
            with open("users.csv", mode="w", encoding="UTF-8") as file:
                for element in lista_usuarios:
                    print(";".join(element), file=file)

    def cargar_usuario(nombreu):

        with open("users.csv", "r", encoding="UTF-8") as users:
            lista_usuarios = []
            for i in users:

                b = i.split(",")
                b = b[0].split(";")
                lista_usuarios.append(b)

        nombres = lista_usuarios[0]
        for a in lista_usuarios:
            a[len(a) - 1] = a[len(a) - 1].rstrip()

        orders = nombres.index("orders: list")
        birthday = nombres.index('birthday: string')
        username = nombres.index('username: string')
        name = nombres.index('name: string')
        lastname = nombres.index("lastname: string")

        i = 0
        for users in lista_usuarios:
            if users[username] == nombreu:
                break
            else:
                i += 1
                if i > len(lista_usuarios) - 1:
                    print("Lo lamento, ese nombre de usuario no existe.")

                    return False

        posi = i


        username = lista_usuarios[posi][username]
        name = lista_usuarios[posi][name]
        lastname = lista_usuarios[posi][lastname]
        birthday = lista_usuarios[posi][birthday]
        orders = lista_usuarios[posi][orders]
        nu = Usuario(username, name, lastname, birthday, orders)

        # vemos el tipo si tiene.

        if len(lista_usuarios[posi]) == 6:
            nu.tipo = lista_usuarios[posi][5]

        else:
            hoy = date.today()
            fecha_nac = datetime.strptime(birthday, "%Y-%m-%d").date()
            edad = hoy - fecha_nac
            edad = edad.days / 365.25

            if edad < 18:
                nu.tipo = "Underaged"

            # por mientras despues veo si es premium o no
            else:
                nu.tipo = "Trader"

            lista_usuarios[posi].append(nu.tipo)
            with open("users.csv", mode="w", encoding="UTF-8") as file:
                for element in lista_usuarios:
                    print(";".join(element), file=file)


        return nu

    def crear_usuario():

        with open("users.csv", "r", encoding="UTF-8") as users:
            lista_usuarios = []
            for i in users:

                b = i.split(",")
                b = b[0].split(";")
                lista_usuarios.append(b)

        nombres = lista_usuarios[0]
        for a in lista_usuarios:
            a[len(a) - 1] = a[len(a) - 1].rstrip()

        orders = nombres.index("orders: list")
        birthday = nombres.index('birthday: string')
        user = nombres.index('username: string')
        name = nombres.index('name: string')
        lastname = nombres.index("lastname: string")
        username = input("Ingrese su nombre de usuario:")

        for usuarios in lista_usuarios:
            if usuarios[user] == username:
                print("Lo lamento, ese nombre de usuario ya existe!")
                return False

        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")

        a = True
        while a == True:

            fecha_nac = input("Ingrese su fecha de nacimiento (yy-mm-dd):  ")
            año = fecha_nac[0:4]
            mes = fecha_nac[5:7]
            dia = fecha_nac[8:11]

            if len(fecha_nac) != 10 or fecha_nac[4] != "-"  or fecha_nac[7] != "-":
                print("Ingrese su fecha de la forma (yy-mm-dd)")

            else:
                try:
                    int(año)
                    int(mes)
                    int(dia)
                    if 1900 > int(año) or int(año) > 2017:
                        print("Ingrese un año entre 1900 y 2017.")
                    else:
                        break
                except:
                    print("Ingrese una fecha valida.")


        fecha_nac = (año + "-" + mes + "-" + dia)


        nu = Usuario(username, nombre, apellido, fecha_nac, "")

        hoy = date.today()

        fecha_nac = datetime.strptime(fecha_nac, "%Y-%m-%d").date()
        edad = hoy - fecha_nac
        edad = edad.days / 365.25

        if edad < 18:
            nu.tipo = "Underaged"

        else:
            nu.tipo = "Trader"
        nuevo = [0, 0, 0, 0, 0, 0]


        nuevo[5] = nu.tipo
        nuevo[orders] = ""
        fecha_nac = str(fecha_nac)
        nuevo[birthday] = fecha_nac
        nuevo[user] = username
        nuevo[name] = nombre
        nuevo[lastname] = apellido
        nuevo[5] = nu.tipo
        lista_usuarios.append(nuevo)

        with open("users.csv", mode="w", encoding="UTF-8") as file:
            for element in lista_usuarios:
                print(";".join(element), file=file)

        for algo in nu.dinero_disponible:
            if algo[0] == "DCC":
                algo[1] = Decimal(algo[1])+Decimal(100000)

        for algo in nu.dinero:
            if algo[0] == "DCC":
                algo[1] = Decimal(algo[1])+Decimal(100000)
        return nu

    def add_ask(self):

        # reviso primero si es que ha creado alguna order para ver si le
        # queda plata



        a = True
        while a == True:
            with open("orders.csv", "r", encoding="UTF-8") as orders:
                lista_orders = []
                for i in orders:

                    b = i.split(",")
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

            # para esto debo cargarlo primero en el csv
            if self.tipo == "Underaged":

                print("\nLo lamento, el tipo de usuario no permite crear orders.\n")
                break

            if len(self.mercados) == 0:
                print("Lo lamento, no estas registado en ningun mercado.")
                break
            #CREO MERCADO

            while True:


                print("\nEn que mercado te gustaria ingresar una ask?\n")
                j = []
                f = 1
                for i in range(len(self.mercados)):
                    if self.mercados[i] not in j:
                        print(str(f) + ". " + str(self.mercados[i]))
                        j.append(self.mercados[i])
                        f += 1

                print(str(f) + ". Volver al menu")


                mercado = input("\nElije un mercado:")
                mercado = int(mercado)

                if mercado == len(j)+1:

                    break


                elif len(self.mercados) >= mercado > 0:

                    nombrem = self.mercados[mercado - 1]
                    mercado = Mercado(nombrem)
                    cantidad1 = input("Cuanto {} quieres vender?".format(mercado.moneda1))
                    cantidad2 = input("A cuanto dinero de {} quieres "
                                      "vener la unidad de {}".format(
                        mercado.moneda2,mercado.moneda1))

                    if self.revisar_ask(mercado.moneda1, cantidad1) == True:
                        break

                    else:
                        pass

                else:
                    print("Ingrese una opcion valida.")

            if type(mercado) == int:
                break

            nuevo_add = ["", "", "", "", "", "", ""]

            nuevo_add[ticker] = mercado.nombre
            nuevo_add[order_id] = str(len(lista_orders))
            nuevo_add[date_created] = str(date.today())
            nuevo_add[price] = cantidad2
            nuevo_add[amount] = cantidad1
            nuevo_add[date_match] = ""
            nuevo_add[tipo] = "ask"
            lista_orders.append(nuevo_add)

            with open("users.csv", "r", encoding="UTF-8") as users:
                lista_usuarios = []
                for i in users:

                    b = i.split(",")
                    b = b[0].split(";")
                    lista_usuarios.append(b)

            nombres = lista_usuarios[0]
            for a in lista_usuarios:
                a[len(a) - 1] = a[len(a) - 1].rstrip()

            orders = nombres.index("orders: list")
            username = nombres.index('username: string')

            i = 0
            for users in lista_usuarios:
                if users[username] == self.Nombre_usuario:
                    break
                else:
                    i += 1
            posi = i

            if len(lista_usuarios[posi][orders]) != 0:
                lista_usuarios[posi][orders] = (lista_usuarios[posi][orders] + ":"+str(nuevo_add[order_id]))

            else:
                lista_usuarios[posi][orders] = (lista_usuarios[posi][orders] + str(nuevo_add[order_id]))

            self.orders = lista_usuarios[posi][orders]


            with open("users.csv", mode="w", encoding="UTF-8") as file:
                for element in lista_usuarios:
                    print(";".join(element), file=file)

            with open("orders.csv", mode="w", encoding="UTF-8") as file:
                for element in lista_orders:
                    print(";".join(element), file=file)


            print("\nFelicitaciones, tu ask se ha agregado correctamente\n")
            self.reiniciar()
            for i in self.dinero:
                i[0] = str(i[0])
                i[1] = str(i[1])

            a = mercado.match()
            if len(a)!= 0:
                total = a[0]
                cantidad = a[1]


                for algo in self.dinero_disponible:

                    if algo[0] == mercado.moneda2:
                        j = algo[1]
                        algo[1] = str(Decimal(j)+Decimal(total))

                    elif algo[0] == mercado.moneda1:
                        j = algo[1]
                        algo[1] = str(Decimal(j) - Decimal(cantidad))

                for algo in self.dinero:

                    if algo[0] == mercado.moneda2:
                        j = algo[1]
                        algo[1] = str(Decimal(j) + Decimal(total))

                    elif algo[0] == mercado.moneda1:
                        j = algo[1]
                        algo[1] = str(Decimal(j) - Decimal(cantidad))



            self.imprimir()

            return

    def add_bid(self):

        a = True
        while a == True:

            with open("orders.csv", "r", encoding="UTF-8") as orders:
                lista_orders = []
                for i in orders:

                    b = i.split(",")
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

            if self.tipo == "Underaged":

                print("\nLo lamento, el tipo de usuario no permite crear orders.\n")
                pass

            if len(self.mercados) == 0:
                print("Lo lamento, no estas registado en ningun mercado.")
                break


            #CREO MERCADO
            while True:

                print("\nEn que mercado te gustaria ingresar un bid?\n")
                j = []
                f = 1
                for i in range(len(self.mercados)):
                    if self.mercados[i] not in j:
                        print(str(f) + ". " + str(self.mercados[i]))
                        j.append(self.mercados[i])
                        f += 1

                print(str(f) + ". Volver al menu")

                mercado = input("\nElije un mercado:")
                mercado = int(mercado)

                if mercado == len(self.mercados) + 1:
                    break



                if len(self.mercados) >= mercado > 0:

                    nombrem = self.mercados[mercado - 1]
                    mercado = Mercado(nombrem)
                    cantidad1 = input("Cuanto {} quieres "
                                              "comprar?".format(
                        mercado.moneda1))
                    cantidad2 = input("A cuanto dinero de {} quieres "
                                       "comprar la unidad de {}".format(
                        mercado.moneda2, mercado.moneda1))

                    if self.revisar_bid(mercado.moneda2, Decimal(
                            cantidad1)*Decimal(cantidad2)) == True:
                        break


                else:
                    print("Ingrese una opcion valida.")

            if type(mercado) == int:
                break

            nuevo_bid = ["", "", "", "", "", "", ""]

            nuevo_bid[ticker] = mercado.nombre
            nuevo_bid[order_id] = str(len(lista_orders))
            nuevo_bid[date_created] = str(date.today())
            nuevo_bid[price] = cantidad1
            nuevo_bid[amount] = cantidad1
            nuevo_bid[date_match] = ""
            nuevo_bid[tipo] = "bid"
            lista_orders.append(nuevo_bid)

            with open("users.csv", "r", encoding="UTF-8") as users:
                lista_usuarios = []
                for i in users:

                    b = i.split(",")
                    b = b[0].split(";")
                    lista_usuarios.append(b)

            nombres = lista_usuarios[0]
            for a in lista_usuarios:
                a[len(a) - 1] = a[len(a) - 1].rstrip()

            orders = nombres.index("orders: list")
            username = nombres.index('username: string')

            i = 0
            for users in lista_usuarios:
                if users[username] == self.Nombre_usuario:
                    break
                else:
                    i += 1
            posi = i

            if len(lista_usuarios[posi][orders]) != 0:
                lista_usuarios[posi][orders] = (lista_usuarios[posi][orders] + ":"+str(nuevo_bid[order_id]))

            else:
                lista_usuarios[posi][orders] = (lista_usuarios[posi][orders] + str(nuevo_bid[order_id]))

            self.orders = lista_usuarios[posi][orders]


            with open("users.csv", mode="w", encoding="UTF-8") as file:
                for element in lista_usuarios:
                    print(";".join(element), file=file)

            with open("orders.csv", mode="w", encoding="UTF-8") as file:
                for element in lista_orders:
                    print(";".join(element), file=file)

            print("\nFelicitaciones, tu bid se ha agregado correctamente\n")
            self.reiniciar()
            for i in self.dinero:
                i[0] = str(i[0])
                i[1] = str(i[1])

            a = mercado.match()
            if len(a) != 0:
                total = a[0]
                cantidad = a[1]

                for algo in self.dinero_disponible:

                    if algo[0] == mercado.moneda2:
                        j = algo[1]
                        algo[1] = str(Decimal(j) + Decimal(total))

                    elif algo[0] == mercado.moneda1:
                        j = algo[1]
                        algo[1] = str(Decimal(j) - Decimal(cantidad))

                for algo in self.dinero:

                    if algo[0] == mercado.moneda2:
                        j = algo[1]
                        algo[1] = str(Decimal(j) + Decimal(total))

                    elif algo[0] == mercado.moneda1:
                        j = algo[1]
                        algo[1] = str(Decimal(j) - Decimal(cantidad))

            self.imprimir()

            return

    def agregar_mercado(self):

        True
        while True:
            print("\nEstos son los mercados disponibles.\n")
            print(self.mercados_totales)
            nombre = input("\nA que mercado te quieres registrar?")
            if nombre not in self.mercados and nombre in self.mercados_totales:

                print("\nFelicitaciones! Ya estas registrado en el mercado {}".format(nombre))
                mercado = Mercado(nombre)
                self.mercados.append(mercado.nombre)
                for moneda in self.dinero:
                    if moneda[0] == mercado.moneda1 or moneda[0] == \
                            mercado.moneda2 and moneda[0]:
                        mas = Decimal(50000)
                        moneda[1] = Decimal(moneda[1])
                        moneda[1] += mas
                        moneda[1] = str(moneda[1])



                for moneda in self.dinero_disponible:
                    if moneda[0] == mercado.moneda1 or moneda[0] == \
                            mercado.moneda2 and moneda[0]:
                        mas = Decimal(50000)
                        moneda[1] = Decimal(moneda[1])
                        moneda[1] += mas
                        moneda[1] = str(moneda[1])

                break

            elif nombre in self.mercados:
                print("\nLo lamento, ya estas registrado en este mercado.")
                break

            else:
                print("\nEse no es un mercado existente!.")
        self.imprimir()


    def ver_activas(self):

        if len(self.orders) == len(self.ask) + len(self.bid) + len(
                self.matches):
            print("\nEstos son tus orders activas:\n")
            print("Ask:")
            print(self.ask)
            print("\n Estos son tus bid:\n")
            print(self.bid)
            return

        else:
            nu = Usuario(self.Nombre_usuario, self.Nombre, self.Apellido,
                         self.Fecha_nacimiento, self.orders)
            nu.ver_activas()


        pass

    def revisar_ask(self, moneda, cantidad):

        with open("orders.csv", "r", encoding="UTF-8") as orders:
            lista_orders = []
            for i in orders:
                b = i.split(",")
                b = b[0].split(";")
                lista_orders.append(b)

            for a in lista_orders:
                a[len(a) - 1] = a[len(a) - 1].rstrip()
        nombres = lista_orders[0]
        date_created = nombres.index('date_created: string')

        i = 0
        for algo in self.ask:
            if algo[date_created] == str(date.today()):
                i += 1
        for algo in self.bid:
            if algo[date_created] == str(date.today()):
                i += 1
        for algo in self.matches_ask:
            if algo[date_created] == str(date.today()):
                i += 1
        for algo in self.matches_bid:
            if algo[date_created] == str(date.today()):
                i += 1

        if self.tipo == "Trader":
            if i >= 15:
                print("\nLo lamento, solo puedes hacer un maximo de 15 orders "
                      "en un dia\n")
                return False
            if len(self.ask) + len(self.bid) == 5:
                print("\nLo lamento, solo puedes tener 5 orders activas\n")
                return False


        for i in range(len(self.dinero_disponible)):

            if self.dinero_disponible[i][0] == moneda:

                if Decimal(cantidad) > Decimal(self.dinero_disponible[i][1]):
                    print("\nLo lamento, no tienes suficiente dinero de {} "
                          "para realizar esta transaccion.\n".format(moneda))
                    return False

                else:

                    return True

    def revisar_bid(self, moneda, cantidad):

        with open("orders.csv", "r", encoding="UTF-8") as orders:
            lista_orders = []
            for i in orders:
                b = i.split(",")
                b = b[0].split(";")
                lista_orders.append(b)

            for a in lista_orders:
                a[len(a) - 1] = a[len(a) - 1].rstrip()
        nombres = lista_orders[0]
        date_created = nombres.index('date_created: string')

        i = 0
        for algo in self.ask:
            if algo[date_created] == str(date.today()):
                i += 1
        for algo in self.bid:
            if algo[date_created] == str(date.today()):
                i += 1

        if self.tipo == "Trader":
            if i >= 15:
                print("\nLo lamento, solo puedes hacer un maximo de 15 orders "
                      "en un dia\n")
                return False
            if len(self.ask) + len(self.bid) == 5:
                print("\nLo lamento, solo puedes tener 5 orders activas\n")
                return False

        for i in range(len(self.dinero_disponible)):

            if self.dinero_disponible[i][0] == moneda:

                if Decimal(cantidad) > Decimal(self.dinero_disponible[i][1]):
                    print("\nLo lamento, no tienes suficiente dinero de {} "
                          "para realizar esta transaccion.\n".format(moneda))
                    return False

                else:

                    return True

    def reiniciar(self):

        self.actualizar()
        nu = Usuario(self.Nombre_usuario, self.Nombre, self.Apellido,
                     self.Fecha_nacimiento, self.orders)
        return nu

    def imprimir(self):
        with open("banco.csv", "r", encoding="UTF-8") as dinero:
            banco = []
            for i in dinero:
                banco.append(i)
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
            dcc = [0, 0]
            dcc[name] = "DCC CryptoCoin"
            dcc[symbol] = "DCC"
            if dcc not in lista_monedas:
                lista_monedas.append(dcc)

        if len(self.dinero_disponible) == 0:
            for i in range(len(lista_monedas)):
                self.dinero.append([lista_monedas[i][symbol]])
                self.dinero_disponible.append(
                    [lista_monedas[i][symbol]])

            for monedas in self.dinero:
                monedas.append(str(Decimal(0)))

            for monedas in self.dinero_disponible:
                monedas.append(str(Decimal(0)))

        with open("banco.csv", "w", encoding="UTF-8") as file:

            banco.append(self.Nombre_usuario)
            banco.append(self.dinero_disponible)
            banco.append(self.dinero)
            for cosa in banco:
                if cosa != "\n":
                    print("".join(str(cosa)), file=file)


    def monedas(self):

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

            dcc = [0, 0]
            dcc[name] = "DCC CryptoCoin"
            dcc[symbol] = "DCC"
            if dcc not in lista_monedas:
                lista_monedas.append(dcc)

        if len(self.dinero_disponible) == 0:
            for i in range(len(lista_monedas)):
                self.dinero.append([lista_monedas[i][symbol]])
                self.dinero_disponible.append(
                    [lista_monedas[i][symbol]])

            for monedas in self.dinero:
                monedas.append(str(Decimal(0)))

            for monedas in self.dinero_disponible:
                monedas.append(str(Decimal(0)))

    def investor(self):
        for algo in self.dinero:
            if algo[0] == "DCC":
                plata = Decimal(algo[1])
                if plata >= Decimal(300000):
                    self.tipo = "Investor"

                else:
                    print("\nLo lamento, no tienes suficiente dinero para "
                          "cambiarte a investor.\n")

        with open("users.csv", "r", encoding="UTF-8") as users:
            lista_usuarios = []
            for i in users:

                b = i.split(",")
                b = b[0].split(";")
                lista_usuarios.append(b)

        nombres = lista_usuarios[0]
        for a in lista_usuarios:
            a[len(a) - 1] = a[len(a) - 1].rstrip()

        username = nombres.index('username: string')

        i = 0
        for users in lista_usuarios:
            if users[username] == self.Nombre_usuario:
                break
            else:
                i += 1

        posi = i

        if len(lista_usuarios[posi]) == 6:
            self.tipo = lista_usuarios[posi][5]

        else:
            lista_usuarios[posi].append(nu.tipo)
            with open("users.csv", mode="w", encoding="UTF-8") as file:
                for element in lista_usuarios:
                    print(";".join(element), file=file)








