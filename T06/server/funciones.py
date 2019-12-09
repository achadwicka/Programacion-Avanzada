import zlib
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPixmap

# listo
def blurry(j):
    nc = len(j)
    nf = len(j[0])
    n = []

    # creo matriz nueva
    for x in range(nc):
        fila = []
        for y in range(nf):
            if y == nf - 1:
                fila.append([0,0,0])
                n.append(fila)
            else:
                fila.append([0,0,0])


    ls = []
    for x in range(nc):
        lps = []
        for y in range(nf):

            if x == 0 and y == 0:
                for i in range(3):
                    a = j[x][y][i] * 4
                    b = j[x][y + 1][i] * 2
                    c = j[x + 1][y + 1][i]
                    d = j[x + 1][y][i] * 2

                    suma = a + b + c + d
                    valor = round(suma / 16)

                    n[x][y][i] = valor

            elif x == nc - 1 and y == 0:
                for i in range(3):
                    a = j[x][y][i] * 4
                    b = j[x - 1][y][i] * 2
                    c = j[x - 1][y + 1][i]
                    d = j[x][y + 1][i] * 2

                    suma = a + b + c + d
                    valor = round(suma / 16)

                    n[x][y][i] = valor

            elif x == nc - 1 and y == nf - 1:
                for i in range(3):
                    a = j[x][y][i] * 4
                    b = j[x - 1][y][i] * 2
                    c = j[x - 1][y - 1][i]
                    d = j[x][y - 1][i] * 2

                    suma = a + b + c + d
                    valor = round(suma / 16)

                    n[x][y][i] = valor

            elif x == 0 and y == nf - 1:
                for i in range(3):
                    a = j[x][y][i] * 4
                    b = j[x][y - 1][i] * 2
                    c = j[x + 1][y - 1][i]
                    d = j[x + 1][y][i] * 2

                    suma = a + b + c + d
                    valor = round(suma / 16)

                    n[x][y][i] = valor

            elif x == 0:
                for i in range(3):
                    a = j[x][y][i] * 4
                    b = j[x][y - 1][i] * 2
                    c = j[x + 1][y - 1][i]
                    d = j[x + 1][y][i] * 2
                    e = j[x + 1][y + 1][i]
                    f = j[x][y + 1][i] * 2

                    suma = a + b + c + d + e + f
                    valor = round(suma / 16)

                    n[x][y][i] = valor

            elif y == nf - 1:
                for i in range(3):
                    a = j[x][y][i] * 4
                    b = j[x - 1][y][i] * 2
                    c = j[x - 1][y - 1][i]
                    d = j[x][y - 1][i] * 2
                    e = j[x + 1][y - 1][i]
                    f = j[x + 1][y][i] * 2

                    suma = a + b + c + d + e + f
                    valor = round(suma / 16)

                    n[x][y][i] = valor

            elif y == 0:
                for i in range(3):
                    a = j[x][y][i] * 4
                    b = j[x][y + 1][i] * 2
                    c = j[x - 1][y][i] * 2
                    d = j[x + 1][y][i] * 2
                    e = j[x + 1][y + 1][i]
                    f = j[x - 1][y + 1][i]

                    suma = a + b + c + d + e + f
                    valor = round(suma / 16)

                    n[x][y][i] = valor

            elif x == nc - 1:
                for i in range(3):
                    a = j[x][y][i] * 4
                    b = j[x][y - 1][i] * 2
                    c = j[x - 1][y][i] * 2
                    d = j[x - 1][y - 1][i]
                    e = j[x - 1][y + 1][i]
                    f = j[x][y + 1][i] * 2

                    suma = a + b + c + d + e + f
                    valor = round(suma / 16)

                    n[x][y][i] = valor

            else:
                for i in range(3):
                    a = j[x][y][i] * 4
                    b = j[x - 1][y][i] * 2
                    c = j[x + 1][y][i] * 2
                    d = j[x][y - 1][i] * 2
                    e = j[x][y + 1][i] * 2
                    f = j[x + 1][y + 1][i]
                    g = j[x - 1][y + 1][i]
                    h = j[x + 1][y - 1][i]
                    p = j[x - 1][y - 1][i]

                    suma = a + b + c + d + e + f + g + h + p
                    valor = round(suma / 16)
                    n[x][y][i] = valor



            lps.append([n[x][y][0], n[x][y][1], n[x][y][2]])
        ls.append(lps)
    return ls

def retorna_matriz(nombre):
    nombre = 'act/' + nombre
    #### lee imagen .png ####
    with open(nombre, 'rb') as file:
        ima = file.read()
        imagen = bytearray(ima)
        header = imagen[:8]

        ihdr = bytearray()
        idat = bytearray()
        c = 8
        while c - len(imagen) < - 12:
            lb = imagen[c:c + 4]
            la = int.from_bytes(lb, byteorder='big')
            ti = imagen[c + 4:c + 8]
            inf = imagen[c + 8: c + 8 + la]
            crc = imagen[c + 8 + la:c + 12 + la]
            chunk = bytearray(lb + ti + inf + crc)
            c += 12 + la

            if ti == b'IHDR':
                ihdr = chunk
                crcihdr = crc

            elif ti == b'IDAT':
                la12 = lb
                idat = chunk
                matriz = inf

    lidat = int.from_bytes(idat[:4], 'big')

    laih = int.from_bytes(ihdr[:4], 'big')
    infoihdr = ihdr[8:laih + 8]
    ancho = int.from_bytes(infoihdr[:4], 'big')

    ide = zlib.decompress(idat[8:lidat + 8])

    cf = 1
    c = 0
    a = 0
    mat = []
    fila = []
    while c < len(ide):
        if a == 0:
            a += 1
            c += 1
            continue
        pixel = [ide[c], ide[c + 1], ide[c + 2]]
        fila.append(pixel)
        c += 3
        if cf == ancho:
            cf = 1
            mat.append(fila)
            a = 0
            fila = []
        else:
            cf += 1

    return mat

def genera_png(elemento, nombre):

    for linea in elemento:
        linea.insert(0, 0)

    nombre = 'images/' + nombre

    #### lee imagen .png ####
    with open(nombre, 'rb') as file:
        ima = file.read()
        imagen = bytearray(ima)
        header = imagen[:8]

        ihdr = bytearray()
        idat = bytearray()
        c = 8
        while c - len(imagen) < - 12:
            lb = imagen[c:c + 4]
            la = int.from_bytes(lb, byteorder='big')
            ti = imagen[c + 4:c + 8]
            inf = imagen[c + 8: c + 8 + la]
            crc = imagen[c + 8 + la:c + 12 + la]
            chunk = bytearray(lb + ti + inf + crc)
            c += 12 + la

            if ti == b'IHDR':
                ihdr = chunk
                crcihdr = crc

            elif ti == b'IDAT':
                la12 = lb
                idat = chunk
                matriz = inf

    lidat = int.from_bytes(idat[:4], 'big')

    laih = int.from_bytes(ihdr[:4], 'big')
    infoihdr = ihdr[8:laih + 8]
    ancho = int.from_bytes(infoihdr[:4], 'big')


    matrizf = bytearray()
    for linea in elemento:
        for pixel in linea:
            if pixel == 0:
                matrizf.extend(int.to_bytes(pixel, 1, 'big'))
            else:
                a, b, c = pixel
                matrizf.extend(int.to_bytes(a, 1, 'big'))
                matrizf.extend(int.to_bytes(b, 1, 'big'))
                matrizf.extend(int.to_bytes(c, 1, 'big'))

    final = zlib.compress(matrizf, 9)

    ##### CREANDO IDAT #####

    # largo, bien
    # largo = int.to_bytes(len(mat) * ((len(mat[0]) - 1) * 3 + 1), 4, 'big')
    lp = len(final)
    largo = int.to_bytes(lp, 4, 'big')

    # tipo, bien
    casi = bytearray(b'IDAT')

    # matriz mal :S
    casi.extend(final)

    # crc, bien
    crc = zlib.crc32(casi)
    crc = int.to_bytes(crc, 4, 'big')

    idatlisto = largo + casi + crc

    ##### CREANDO IHDR ######  no hay para que cambiarlo!

    ihdrfinal = bytearray()
    # ancho
    ihdrfinal.extend(int.to_bytes(len(elemento[0]) - 1, 4, 'big'))
    # alto
    ihdrfinal.extend(int.to_bytes(len(elemento), 4, 'big'))
    # profundidad
    ihdrfinal.extend(int.to_bytes(8, 1, 'big'))
    # tipo color
    ihdrfinal.extend(int.to_bytes(2, 1, 'big'))
    # tipo compresion
    ihdrfinal.extend(int.to_bytes(0, 1, 'big'))
    # tipo filtro
    ihdrfinal.extend(int.to_bytes(0, 1, 'big'))
    # entrelazado
    ihdrfinal.extend(int.to_bytes(0, 1, 'big'))
    # concatenamos todo
    bytefinal = bytearray(b'IHDR')
    bytefinal.extend(ihdrfinal)

    # largo
    largo = int.to_bytes(len(ihdrfinal), 4, 'big')

    crc = zlib.crc32(bytefinal)
    crc = int.to_bytes(crc, 4, 'big')

    ihdrlisto = largo + bytefinal + crc

    ###### CREANDO IEND ######

    largo = bytearray(int.to_bytes(0, 4, 'big'))
    tipo = bytearray(b'IEND')
    crc = zlib.crc32(tipo)
    crc = int.to_bytes(crc, 4, 'big')

    iendlisto = largo + tipo + crc

    return header + ihdrlisto + idatlisto + iendlisto

def recorta(elemento):
    largo = len(elemento)
    ancho = len(elemento[0])

    for x in range(largo):
        for y in range(ancho):
            if 250 < x < 500 and 200 < y < 300:
                for i in range(3):
                    elemento[x][y][i] = 255

    return elemento

def blade(j, color, pix):
    nc = len(j)
    nf = len(j[0])

    if color == 'blanco':
        pixel = [255, 255, 255]
    elif color == 'rojo':
        pixel = [255, 0, 0]
    elif color == 'amarillo':
        pixel = [255, 255, 0]
    elif color == 'azul':
        pixel = [0, 0, 255]
    else:
        pixel = [0, 0, 0]

    for x in range(nc):
        for y in range(nf):
            if j[x][y] == pix:
                j[x][y] = pixel

    return j
