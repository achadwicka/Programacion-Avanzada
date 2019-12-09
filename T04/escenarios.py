from funciones import  *

escenarios = leer_escenario('escenarios.csv')
para = leer_parametros('parametros_iniciales.csv')

def elegir_escenario(n):
    if n not in escenarios.keys():
        return para
    return escenarios[n]