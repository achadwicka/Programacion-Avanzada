from functools import reduce

def estadisticas(sim):
    """
    Funcion que ejecuta las estadisticas y las presenta en consola
    :param sim: la instancia de class simulacion ejecutada anteriormetne
    :return: nada
    """
    total_confiscado = 0
    for vendedor in sim.vendedores_originales:
        total_confiscado += vendedor.dinero_requisado

    productos = list(sim.prod_originales.keys())
    promedio_req = total_confiscado / sim.cantidad_vendedores
    abandona = sim.abandona_cola / sim.dias
    sin_stock = sim.total_sin_stock / sim.dias
    valores = list(sim.prod_originales2.values())
    maxi = valores.index(max(valores))
    prod_max = productos[maxi]
    maximo = max(valores)
    mini = valores.index(min(valores))
    prod_mini = productos[mini]
    minimo = min(valores)
    total = reduce(lambda x, y: x + y, valores)
    promedio_prod = total / len(productos) / sim.dias
    maximo = maximo / sim.dias
    minimo = minimo / sim.dias
    descomponen = 0
    for vend in sim.vendedores_originales:
        for prod in vend.productos:
            if prod.calidad(420) < 0.2:
                descomponen += 1

    print('\n'*2)
    print('------------------------- ESTADISTICAS -------------------------\n')
    print('1. Cantidad promedio de dinero confiscado: {}\n'.format(
        promedio_req))
    print('2. Cantidad vendida de productos por dia:')
    print('     Cantidad mínima: {} de {}'.format(minimo, prod_mini))
    print('     Cantidad máxima: {} de {}'.format(maximo, prod_max))
    print('     Promedio por dia: {}\n'.format(promedio_prod))
    print('3. Cantidad de confiscaciones que realizó: -Mr Hyde: {0}'.
          format(sim.cantidad_requisado_hyde))
    print('                                           -Mr Jekyll: {}\n'.
          format(sim.cantidad_requisado_jekyll))
    print('4. Cantidad de veces que Quick Devil llamo a carabineros: {}\n'.
          format(sim.cantidad_llamadas))
    print('5. Número de veces que se realizó la Concha Estéreo: {}\n'.
          format(sim.cantidad_concha))
    print('6. Número de veces que hubo temperaturas extremas: {}\n'.format(
        sim.cantidad_temperaturas))
    print('7. Número de veces que hubo Lluvia de Hamburguesas: {}\n'.format(
        sim.lluvias))
    print('8. Cantidad promedio que almorzó entre 12 y 13 hrs: {}'.format(
        sim.almuerza12 / sim.dias))
    print('   Cantidad promedio que almorzó entre 13 y 14 hrs: {}'.format(
        sim.almuerza1 / sim.dias))
    print('   Cantidad promedio que almorzó entre 14 y 15 hrs: {}\n'.format(
        sim.almuerza2 / sim.dias))
    print('9. Cantidad de alumnos que no almorzaron por mes:')
    for mes in range(sim.mes - 1):
        print('     En el mes {} no almorzaron {} alumnos.'.format(mes + 1,
                sim.no_almuerza_mes[mes - 1]))
    print('\n10. Calidad promedio de los productos por escenario: {}\n')
    print('11. Cantidad de MiembrosUC que se intoxican por vendedor: \n')
    for vende in sim.vendedores_originales:
        print('     El vendedor {} hizo que se enfermaran {} '
              'miembros.'.format(vende, vende.enfermos))
    print('\n12. Cantidad de productos que se descomponen: {}\n'.format(
        descomponen))
    print('13. Cantidad promedio de miembrosUC que abandonan cola: {}\n'.
          format(abandona))
    print('14. Cantidad promedio de vendedores que se quedan sin stock: {}\n'.
          format(sin_stock))
    print('15. Cantidad de veces que se engaño a carabineros con '
          'personalidad: -Mr Hyde: {}'.format(sim.enganos_hyde))
    print('                                                            '
          '        -Mr Jekyll: {}\n'.format(sim.enganos_jekyll))

def desempeño(sim, n):
    """
    Funcion que retorna el numero de desempeño, que corresponde a la suma de
    TODOS los valores que se piden en las estadisticas
    :param sim: class simulacion
    :return: la suma de la variable a evaluar
    """
    total_confiscado = 0
    for vendedor in sim.vendedores_originales:
        total_confiscado += vendedor.dinero_requisado

    productos = list(sim.prod_originales.keys())
    promedio_req = total_confiscado / sim.cantidad_vendedores
    abandona = sim.abandona_cola / sim.dias
    sin_stock = sim.total_sin_stock / sim.dias
    valores = list(sim.prod_originales2.values())
    maxi = valores.index(max(valores))
    prod_max = productos[maxi]
    maximo = max(valores)
    mini = valores.index(min(valores))
    prod_mini = productos[mini]
    minimo = min(valores)
    total = reduce(lambda x, y: x + y, valores)
    promedio_prod = total / len(productos) / sim.dias
    maximo = maximo / sim.dias
    minimo = minimo / sim.dias
    descomponen = 0
    enferman = 0
    for vend in sim.vendedores_originales:
        enferman += vend.enfermos
        for prod in vend.productos:
            if prod.calidad(420) < 0.2:
                descomponen += 1

    suma_meses = 0
    for mes in range(sim.mes - 1):
        suma_meses += sim.no_almuerza_mes[mes - 1]

    if n == 1:
        return promedio_req
    elif n == 2:
        return minimo + maximo + promedio_prod
    elif n == 3:
        return sim.cantidad_requisado_jekyll + sim.cantidad_requisado_hyde
    elif n == 4:
        return sim.cantidad_llamadas
    elif n == 5:
        return sim.cantidad_concha
    elif n == 6:
        return sim.cantidad_temperaturas
    elif n == 7:
        return sim.lluvias
    elif n == 8:
        return sim.almuerza2 + sim.almuerza1 + sim.almuerza12
    elif n == 9:
        return suma_meses
    elif n == 10:
        return 0
    elif n == 11:
        return enferman
    elif n == 12:
        return descomponen
    elif n == 13:
        return abandona
    elif n == 14:
        return sin_stock
    else:
        return sim.enganos_hyde + sim.enganos_jekyll


