with open("original.txt", "r") as archivo_origen:
    contenido = archivo_origen.read()

with open("copia.txt", "w") as archivo_destino:
    archivo_destino.write(contenido)