#  Author: Alberto Chadwick A.

from MERCADO import *
from DCCAPITAL import *
from USUARIO import *

""" MENU """



app = True
while app == True:

    if os.path.exists("banco.csv") == False:
        with open("banco.csv", "w", encoding="UTF-8") as dinero:
            pass

    ingreso = True
    while ingreso == True:

        print("Bienevenido a DCCAPITAL Exchange!\n"
              "Que desea hacer?\n"
              "1. Iniciar sesion.\n"
              "2. Crear un nuevo usuario.\n")

        opcion = input("Elija una opcion: ")

        if opcion == "1":

            ua = input("Ingrese su nombre de usuario: ")

            nu = Usuario.cargar_usuario(ua)

            if nu != False:
                print("\nBienvenido nuevamente a DCCAPITAL Exchange {}!\n".
                    format(ua))
                break


        elif opcion == "2":

            nu = Usuario.crear_usuario()
            if nu != False:
                break

        elif opcion != "1" and opcion != "2":
            print("\nNo existe esa opcion.\n")

    u = True
    while u == True:

        if nu.tipo == "Trader":

            print("\n Estas son tus opciones:\n"
                  "\n1. Lista de mercados disponibles.\n"
                  "2. Lista de mercados en los cuales esta registrado.\n"
                  "3. Registrarse en un mercado especifico.\n"
                  "4. Lista de orders.\n"
                  "5. Lista de orders activas.\n"
                  "6. Ingresar ask.\n"
                  "7. Ingresar bid.\n"
                  "8. Desplegar informacion de mercado.\n"
                  "9. Banco.\n"
                  "10. Salir del sistema.\n"
                  "11. Consultas.\n"
                  "12. Ver dinero disponible\n"
                  "13. Cambiar a tipo investor\n")



            respuesta = input("Que desea hacer?")

            if respuesta == "1":
                print("\nLos mercados disponibles son los siguientes:\n")
                print(nu.mercados_totales)

            elif respuesta == "2":
                print("\nLos mercados en que estas registrado son:\n")
                print(nu.mercados)

            elif respuesta == "3":
                nu.agregar_mercado()

            elif respuesta == "4":
                # aca ver que quiere, si las de un mercado o entre fechas.
                nu.ver_orders()
                #print(nu.orders)

            elif respuesta == "5":
                nu.ver_activas()
                pass

            elif respuesta == "6":
                nu.add_ask()


            elif respuesta == "7":
                nu.add_bid()
                pass

            elif respuesta == "8":
                pass

            elif respuesta == "9":
                nu.ver_dinero()
                pass

            elif respuesta == "10":
                print("\nHasta pronto!\n")
                u = False

            elif respuesta == "11":
                pass

            elif respuesta == "12":
                print("\nEsto es tu dinero (incluyendo lo que tienes ingresado "
                      "en ask y bids)\n")
                nu.actualizar()
                for todo in nu.dinero_disponible:
                    todo[1] = str(Decimal(todo[1]))
                print(nu.dinero_disponible)
                pass

            elif respuesta == "13":
                nu.investor()
                pass

            else:
                print("Ingrese una opcion correcta.")

        if nu.tipo == "Investor":

            print("\n Estas son tus opciones:\n"
                  "\n1. Lista de mercados disponibles.\n"
                  "2. Lista de mercados en los cuales esta registrado.\n"
                  "3. Registrarse en un mercado especifico.\n"
                  "4. Lista de orders.\n"
                  "5. Lista de orders activas.\n"
                  "6. Ingresar ask.\n"
                  "7. Ingresar bid.\n"
                  "8. Desplegar informacion de mercado.\n"
                  "9. Banco.\n"
                  "10. Salir del sistema.\n"
                  "11. Consultas.\n"
                  "12. Ver dinero disponible\n")

            respuesta = input("Que desea hacer?")

            if respuesta == "1":
                print("\nLos mercados disponibles son los siguientes:\n")
                print(nu.mercados_totales)

            elif respuesta == "2":
                print("\nLos mercados en que estas registrado son:\n")
                print(nu.mercados)

            elif respuesta == "3":
                nu.agregar_mercado()

            elif respuesta == "4":
                pass
            elif respuesta == "5":
                nu.ver_activas()
                pass

            elif respuesta == "6":
                nu.add_ask()

            elif respuesta == "7":
                nu.add_bid()
                pass

            elif respuesta == "8":
                pass

            elif respuesta == "9":
                nu.ver_dinero()
                pass

            elif respuesta == "10":
                print("\nHasta pronto!\n")
                u = False

            elif respuesta == "11":
                print("\nQue deseas consultar?:\n"
                      "\n1. Informacion de usuarios.\n"
                      "2. Historial de matches.\n"
                      "3. Informacion de una moneda.\n")
                opcion = input("Que opcion eliges?:")

                pass

            elif respuesta == "12":
                print(
                    "\nEsto es tu dinero (incluyendo lo que tienes ingresado "
                    "en ask y bids)\n")
                nu.actualizar()
                print(nu.dinero_disponible)
                pass


            else:
                print("Ingrese una opcion correcta.")

        if nu.tipo == "Underaged":

            print("\n Estas son tus opciones:\n"
                  "\n1. Lista de mercados disponibles.\n"
                  "2. Lista de mercados en los cuales esta registrado.\n"
                  "3. Registrarse en un mercado especifico.\n"
                  "4. Lista de orders.\n"
                  "5. Desplegar informacion de mercado.\n"
                  "6. Banco.\n"
                  "7. Salir del sistema.\n"
                  "8. Consultas.\n"
                  "9. Ver dinero disponible\n")

            respuesta = input("Que desea hacer?")

            if respuesta == "1":
                print("\nLos mercados disponibles son los siguientes:\n")
                print(nu.mercados_totales)

            elif respuesta == "2":
                print("\nLos mercados en que estas registrado son:\n")
                print(nu.mercados)

            elif respuesta == "3":
                nu.agregar_mercado()

            elif respuesta == "4":
                pass

            elif respuesta == "5":
                pass

            elif respuesta == "6":
                nu.ver_dinero()
                pass

            elif respuesta == "7":
                print("\nHasta pronto!\n")
                u = False

            elif respuesta == "8":
                print("\nQue deseas consultar?:\n"
                      "\n1. Informacion de usuarios.\n"
                      "2. Historial de matches.\n"
                      "3. Informacion de una moneda.\n")
                opcion = input("Que opcion eliges?:")

                pass

            elif respuesta == "9":
                print(
                    "\nEsto es tu dinero (incluyendo lo que tienes ingresado "
                    "en ask y bids)\n")
                nu.actualizar()
                print(nu.dinero_disponible)
                pass

            else:
                print("Ingrese una opcion correcta.")









