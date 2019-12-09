# aca creamos un menu para que se corra la simulacion elegida
from clase_simulacion import Simulacion
from variables import *
from escenarios import *
from estadisticas import estadisticas, desempeño

if __name__ == '__main__':
    while True:
        print('Bienvenido! Que deseas hacer?\n')
        print('1. Correr solo un escenario.')
        print('2. Comparar escenarios.\n')
        a = int(input('Elije opción'))
        if a != 1 and a != 2:
            print('Elige una correcta.\n')
        else:
            break
    if a == 1:
        print('Tienes los siguientes escenarios para elegir:')
        for es in escenarios:
            print('Escenario {}'.format(es))
        print('Otro - Escenario con los parametros iniciales.\n')
        ele = int(input('Cual deseas?'))
        escenario_eje = elegir_escenario(ele)
        imprimir = True

    else:
        print('\nQue estadística deseas comparar?\n')
        print('1. Cantidad promedio de dinero confiscado')
        print('2. Cantidad vendida de productos por dia')
        print('3. Cantidad de confiscaciones que realizaron en total')
        print('4. Cantidad de veces que Quick Devil llamo a carabineros')
        print('5. Número de veces que se realizó la Concha Estéreo')
        print('6. Número de veces que hubo temperaturas extremas')
        print('7. Número de veces que hubo Lluvia de Hamburguesas')
        print('8. Cantidad promedio que almorzaron por día')
        print('9. Cantidad de alumnos que no almorzaron por mes')
        print('10. Calidad promedio de los productos por escenario')
        print('11. Cantidad de MiembrosUC que se intoxican por vendedor')
        print('12. Cantidad de productos que se descomponen')
        print('13. Cantidad promedio de miembrosUC que abandonan cola')
        print('14. Cantidad promedio de vendedores que se quedan sin stock')
        print('15. Cantidad de veces que se engaño a carabineros')

        e = int(input('\nCual deseas?'))
        escenario_eje = []
        cant = int(input('Cuantas réplicas deseas hacer?'))
        imprimir = False
        for i in escenarios:
            escenario_eje.append(elegir_escenario(i))


    i = 0
    j = 0
    desempeno = []
    if imprimir:
        while i < cantidad_simulaciones:
            s = Simulacion()
            s.poblar(escenario_eje)
            s.imprimir = True
            s.run()
            i += 1
        estadisticas(s)

    else:
        for escen in escenario_eje:
            i = 0
            while i < cant:
                s = Simulacion()
                s.poblar(escen)
                s.imprimir = False
                s.run()
                i += 1
            desempeno.append((desempeño(s, e), j))
            j += 1

        desempeno = sorted(desempeno)
        desempeno.reverse()

        print('\nEl mejor escenario fue el {} con estadística de {}'.format(
            desempeno[0][1], desempeno[0][0]))
        print('El segundo mejor escenario fue el {} con estadística de {}'
            .format(desempeno[1][1], desempeno[1][0]))
        print('El tercer mejor escenario fue el {} con estadística de {}'
            .format(desempeno[2][1], desempeno[2][0]))
