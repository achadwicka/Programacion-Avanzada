import Funciones as func
import datetime
ass = datetime.datetime.now()
# creamos una lista por compresion para obtener los datos de los archivos
with open("genomas.txt", "r", encoding="UTF-8") as file:
    datos = [line.rstrip() for line in file]
with open("listas.txt", "r", encoding="UTF-8") as file:
    lists = [line.rstrip() for line in file]

# cantidad de letras que tiene cada nombre
cantidad_nombre = [dato[0]+dato[1] if dato[1].isdigit() else dato[0] for
                   dato in datos]

datos = [dato[2:] if dato[1].isdigit() else dato[1:] for dato in datos]

# con la cantidad de letras de cada nombre obtenemos los nombres
nombres = [datos[i][:int(cantidad_nombre[i])] for i in range(len(datos))]

# vemos cuantas letras tiene cada apellido
cantidad_apellido = [datos[i][int(cantidad_nombre[i])] + datos[i][int(
    cantidad_nombre[i]) + 1] if datos[i][int(cantidad_nombre[i])+1].isdigit()
    else datos[i][int(cantidad_nombre[i])] for i in range(len(datos))]

datos = [datos[i][int(cantidad_nombre[i])+2:] if len(cantidad_apellido[i]) == 2
         else datos[i][int(cantidad_nombre[i])+1:] for i in range(len(datos))]

apellidos = [datos[i][:int(cantidad_apellido[i])] for i in range(len(datos))]
datos = [datos[i][int(cantidad_apellido[i]):] for i in range(len(datos))]

# con los datos ya obtenidos obtenemos los nombres mas apellidos de cada uno
todos = [nombres[i]+" "+apellidos[i] for i in range(len(datos))]

# aca creamos un diccionario por comprension con los datos de cada lista,
# en donde la key es el id de la lista
id_listas = [lists[i].replace(" ","").split(";") for i in range(len(lists))]
tipo_lista = [i[1] for i in id_listas]
listaas = [tipo_lista[i].split(",") for i in range(len(lists))]
listas = {int(id_listas[i][0]): listaas[i] for i in range(len(lists))}

# obtenemos los numeros de lista para cada persona en cada caracteristica
altura = func.rellenar(datos, "AAG")
datos = func.acortar(datos, "AAG")
color_ojos = func.rellenar(datos, "GTC")
datos = func.acortar(datos,"GTC")
color_pelo = func.rellenar(datos, "GGA")
datos = func.acortar(datos, "GGA")
tono_piel = func.rellenar(datos, "TCT")
datos = func.acortar(datos, "TCT")
forma_nariz = func.rellenar(datos, "GTA")
datos = func.acortar(datos, "GTA")
porte_pies = func.rellenar(datos, "CTC")
datos = func.acortar(datos, "CTC")
vello_corporal = func.rellenar(datos, "CGA")
datos = func.acortar(datos, "CGA")
porte_guata = func.rellenar(datos, "TGG")
datos = func.acortar(datos, "TGG")
problemas_vision = func.rellenar(datos, "TAG")
datos = func.acortar(datos, "TAG")
# lista por compresion para cada persona con todos los genomas separados
lista_datos = [[datos[i][3*j]+datos[i][3*j+1]+datos[i][3*j+2] for j in range(
    len(datos[0])//3)] for i in range(len(datos))]


# creamos una lista por compresion para cada dato
gen_altura = list(map(lambda x: func.atributos(lista_datos[x], altura[x],
                  listas), range(len(datos))))
gen_color_ojos = list(map(lambda x: func.atributos(lista_datos[x],
                      color_ojos[x], listas), range(len(datos))))
gen_color_pelo = list(map(lambda x: func.atributos(lista_datos[x],
                      color_pelo[x], listas), range(len(datos))))
gen_tono_piel = list(map(lambda x: func.atributos(lista_datos[x],
                     tono_piel[x], listas), range(len(datos))))
gen_forma_nariz = list(map(lambda x: func.atributos(lista_datos[x],
                       forma_nariz[x], listas), range(len(datos))))
gen_porte_pies = list(map(lambda x: func.atributos(lista_datos[x],
                      porte_pies[x], listas), range(len(datos))))
gen_vello_corporal = list(map(lambda x: func.atributos(lista_datos[x],
                          vello_corporal[x], listas), range(len(datos))))
gen_porte_guata = list(map(lambda x: func.atributos(lista_datos[x],
                       porte_guata[x], listas), range(len(datos))))
gen_problemas_vision = list(map(lambda x: func.atributos(lista_datos[x],
                            problemas_vision[x], listas), range(len(datos))))

# aqui creamos el diccionario final que usaremos el resto del programa,
# en donde las keys son los nombres de las personas, y los values son otro
# diccionario que tiene cada dato con los propios genes :)
genotipos = {todos[i]: {"Altura": gen_altura[i], "Ojos":
            gen_color_ojos[i], "Pelo": gen_color_pelo[i], "Piel":
            gen_tono_piel[i], "Nariz": gen_forma_nariz[i], "Pies":
            gen_porte_pies[i], "Vello": gen_vello_corporal[i],
            "Guata": gen_porte_guata[i], "Problemas":
            gen_problemas_vision[i]} for i in range(len(datos))}
