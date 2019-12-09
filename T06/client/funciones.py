import zlib


def nuevo_png(cambios, imagen):


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
            pass


    laih = int.from_bytes(ihdr[:4], 'big')
    infoihdr = ihdr[8:laih + 8]
    ancho = int.from_bytes(infoihdr[:4], 'big')


    matrizf = bytearray()
    for linea in cambios:
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
    ihdrfinal.extend(int.to_bytes(len(cambios[0]) - 1, 4, 'big'))
    # alto
    ihdrfinal.extend(int.to_bytes(len(cambios), 4, 'big'))
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

def recorta(elemento, nombre):
    largo = len(elemento)
    ancho = len(elemento[0])

    for x in range(largo):
        for y in range(ancho):
            if 250 < x < 500 and 200 < y < 300:
                for i in range(3):
                    elemento[x][y][i] = 255

    return elemento



