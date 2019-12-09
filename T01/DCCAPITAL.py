
""" CLASE DCCAPITAL """

# AQUI ABRIMOS ORDERS Y COPIAMOS TODAS LAS ORDERS EN UNA LISTA

def orders():
    with open("orders.csv", "r", encoding="UTF-8") as orders:
        lista_orders = []
        for i in orders:
            b = i.split(",")
            b = b[0].split(";")
            lista_orders.append(b)

        for a in lista_orders:
            a[len(a) - 1] = a[len(a) - 1].rstrip()
        nombreso = lista_orders[0]
        order_id = nombreso.index('order_id: int')
        date_created = nombreso.index('date_created: string')
        price = nombreso.index('price: float')
        amount = nombreso.index('amount: float')
        date_match = nombreso.index('date_match: string')
        ticker = nombreso.index('ticker: string')
        tipo = nombreso.index('type: string')
