#Ejercicio 1 Crea una lista con al menos 5 elementos. Recorre la lista e imprime cada elemento con su índice.

frutas = ["manzana", "plátano", "naranja", "uva", "sandía"]
for i, fruta in enumerate(frutas):
    print(f"Índice {i}: {fruta}")


#Ejercicio 2 Crea una lista con al menos 5 elementos. Recorre la lista e imprime cada elemento con su índice.
colores = ["rojo", "azul", "verde", "amarillo", "morado"]

for i, color in enumerate(colores):
    print(f"Color en posición {i}: {color}")


#Ejercicio 3 Crea una lista con al menos 5 elementos. Recorre la lista e imprime cada elemento con su índice.
numeros = [10, 20, 30, 40, 50]

for i, num in enumerate(numeros):
    print(f"Índice {i} → Número: {num}")


#Ejercicio 4 Crea una lista con al menos 5 elementos. Recorre la lista e imprime cada elemento con su índice.

animales = ["perro", "gato", "conejo", "loro", "tortuga"]

for i, animal in enumerate(animales):
    print(f"Animal {i}: {animal}")

#Ejercicio 5 Crea una lista con al menos 5 elementos. Recorre la lista e imprime cada elemento con su índice.
paises = ["Ecuador", "Perú", "Colombia", "Brasil", "Argentina"]

for i, pais in enumerate(paises):
    print(f"País {i}: {pais}")


#Ejercicio 6 Crea una lista con al menos 5 elementos. Recorre la lista e imprime cada elemento con su índice.
ciudades = ["Quito", "Guayaquil", "Cuenca", "Loja", "Ambato"]

for i, ciudad in enumerate(ciudades):
    print(f"Ciudad {i}: {ciudad}")

#Ejercicio 7 Crea una lista con al menos 5 elementos. Recorre la lista e imprime cada elemento con su índice.
lenguajes = ["Python", "Java", "C++", "JavaScript", "Ruby"]

for i, lenguaje in enumerate(lenguajes):
    print(f"Lenguaje en índice {i}: {lenguaje}")


#Ejercicio 8 Crea una lista con al menos 5 elementos. Recorre la lista e imprime cada elemento con su índice.
comidas = ["pizza", "sushi", "hamburguesa", "tacos", "ensalada"]

for i, comida in enumerate(comidas):
    print(f"Comida {i}: {comida}")


#Ejercicio 9 Crea una lista con al menos 5 elementos. Recorre la lista e imprime cada elemento con su índice.
profesiones = ["Ingeniero", "Doctor", "Profesor", "Arquitecto", "Abogado"]

for i, profesion in enumerate(profesiones):
    print(f"Profesión {i}: {profesion}")


#Ejercicio 10 Crea una lista con al menos 5 elementos. Recorre la lista e imprime cada elemento con su índice.
compañeros = ["Carlos", "Lucía", "José", "Andrea", "Fernando"]

for i, nombre in enumerate(compañeros):
    print(f"Compañero {i}: {nombre}")


#Ejercicio 11 Pide al usuario que ingrese varias palabras. Almacénalas en una lista y muestra la palabra más larga.
palabras = input("Ingresa varias palabras separadas por espacios: ").split()

mas_larga = max(palabras, key=len)

print(f"La palabra más larga es: '{mas_larga}' con {len(mas_larga)} letras.")


#Ejercicio 12 Pide al usuario que ingrese varias palabras. Almacénalas en una lista y muestra la palabra más larga.
frases = input("Escribe varias palabras: ").split()

larga = max(frases, key=len)

print(f"Palabra más larga: '{larga}' ({len(larga)} caracteres)")


#Ejercicio 13 Pide al usuario que ingrese varias palabras. Almacénalas en una lista y muestra la palabra más larga.
palabras_usuario = input("Introduce palabras separadas por espacio: ").split()

palabra_larga = max(palabras_usuario, key=len)

print(f"Resultado: {palabra_larga} ({len(palabra_larga)} letras)")


#Ejercicio 14 Pide al usuario que ingrese varias palabras. Almacénalas en una lista y muestra la palabra más larga.
lista_palabras = input("Teclea algunas palabras: ").split()

mas_larga = max(lista_palabras, key=len)

print("La más extensa es:", mas_larga)


#Ejercicio 15 Pide al usuario que ingrese varias palabras. Almacénalas en una lista y muestra la palabra más larga.
palabras_ingresadas = input("Palabras separadas por espacio: ").split()

larga = max(palabras_ingresadas, key=len)

print(f"La palabra con más letras es '{larga}'")

#Ejercicio 16 Pide al usuario que ingrese varias palabras. Almacénalas en una lista y muestra la palabra más larga.
entrada = input("Escriba una lista de palabras: ").split()

mas_larga = max(entrada, key=len)

print("Palabra más larga encontrada:", mas_larga)


#Ejercicio 17 Pide al usuario que ingrese varias palabras. Almacénalas en una lista y muestra la palabra más larga.
texto = input("Ingresa varias palabras: ").split()

larga = max(texto, key=len)

print(f"Larga palabra: {larga}")

#Ejercicio 18 Pide al usuario que ingrese varias palabras. Almacénalas en una lista y muestra la palabra más larga.
linea = input("Palabras separadas por espacio: ").split()

palabra_larga = max(linea, key=len)

print(f"Más larga: {palabra_larga} ({len(palabra_larga)} letras)")


#Ejercicio 19 Pide al usuario que ingrese varias palabras. Almacénalas en una lista y muestra la palabra más larga.
coleccion = input("Introduce tus palabras: ").split()

larga = max(coleccion, key=len)

print(f"Palabra ganadora: {larga}")


#Ejercicio 20 Pide al usuario que ingrese varias palabras. Almacénalas en una lista y muestra la palabra más larga.
palabras_varias = input("Palabras separadas por espacio: ").split()

larga = max(palabras_varias, key=len)

print(f"La palabra más larga es: {larga}")


#Ejercicio 21 Usa un diccionario para contar la frecuencia de palabras en una línea de texto ingresada por el usuario.
texto = input("Escribe una línea de texto: ").split()
frecuencia = {}

for palabra in texto:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

print("Frecuencia de palabras:", frecuencia)



#Ejercicio 22 Usa un diccionario para contar la frecuencia de palabras en una línea de texto ingresada por el usuario.
linea = input("Ingresa una frase: ").split()
conteo = {}

for palabra in linea:
    conteo[palabra] = conteo.get(palabra, 0) + 1

print("Conteo:", conteo)


#Ejercicio 23 Usa un diccionario para contar la frecuencia de palabras en una línea de texto ingresada por el usuario.
entrada = input("Introduce tu oración: ").split()
diccionario = {}

for palabra in entrada:
    diccionario[palabra] = diccionario.get(palabra, 0) + 1

print("Palabras contadas:", diccionario)


#Ejercicio 24 Usa un diccionario para contar la frecuencia de palabras en una línea de texto ingresada por el usuario.
frase = input("Escriba un texto: ").split()
frecuencias = {}

for palabra in frase:
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

print("Frecuencias:", frecuencias)



#Ejercicio 25 Usa un diccionario para contar la frecuencia de palabras en una línea de texto ingresada por el usuario.
texto_usuario = input("Texto separado por espacios: ").split()
palabras_contadas = {}

for palabra in texto_usuario:
    palabras_contadas[palabra] = palabras_contadas.get(palabra, 0) + 1

print("Recuento:", palabras_contadas)



#Ejercicio 26 Usa un diccionario para contar la frecuencia de palabras en una línea de texto ingresada por el usuario.
palabras = input("Línea de texto: ").split()
conteo_palabras = {}

for palabra in palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1

print(conteo_palabras)

#Ejercicio 27 Usa un diccionario para contar la frecuencia de palabras en una línea de texto ingresada por el usuario.
linea_texto = input("Frase: ").split()
contador = {}

for palabra in linea_texto:
    contador[palabra] = contador.get(palabra, 0) + 1

print("Resultado del conteo:", contador)


#Ejercicio 28 Usa un diccionario para contar la frecuencia de palabras en una línea de texto ingresada por el usuario.
texto_ingresado = input("Introduce palabras: ").split()
frecuencia_palabras = {}

for palabra in texto_ingresado:
    frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1

print(frecuencia_palabras)



#Ejercicio 29 Usa un diccionario para contar la frecuencia de palabras en una línea de texto ingresada por el usuario.
frase_usuario = input("Línea de texto para analizar: ").split()
dicc_frecuencia = {}

for palabra in frase_usuario:
    dicc_frecuencia[palabra] = dicc_frecuencia.get(palabra, 0) + 1

print(dicc_frecuencia)


#Ejercicio 30 Usa un diccionario para contar la frecuencia de palabras en una línea de texto ingresada por el usuario.
linea_entrada = input("Ingresa una oración: ").split()
conteo_dict = {}

for palabra in linea_entrada:
    conteo_dict[palabra] = conteo_dict.get(palabra, 0) + 1

print("Frecuencia:", conteo_dict)



#Ejercicio 31 Lee un archivo de texto `datos.txt` y muestra las 3 palabras más repetidas utilizando un diccionario.
with open("datos.txt", "r", encoding="utf-8") as archivo:
    texto = archivo.read().split()

frecuencia = {}
for palabra in texto:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

top3 = sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)[:3]

print("Top 3 palabras más frecuentes:")
for palabra, veces in top3:
    print(f"{palabra}: {veces} veces")


#Ejercicio 32 Lee un archivo de texto `datos.txt` y muestra las 3 palabras más repetidas utilizando un diccionario.
with open("datos.txt", "r", encoding="utf-8") as f:
    palabras = f.read().split()

conteo = {}
for p in palabras:
    conteo[p] = conteo.get(p, 0) + 1

top3 = sorted(conteo.items(), key=lambda x: x[1], reverse=True)[:3]

print("Palabras más comunes:")
for palabra, frecuencia in top3:
    print(f"{palabra} ({frecuencia})")



#Ejercicio 33 Lee un archivo de texto `datos.txt` y muestra las 3 palabras más repetidas utilizando un diccionario.
archivo = open("datos.txt", "r", encoding="utf-8")
contenido = archivo.read()
archivo.close()

palabras = contenido.split()
frecuencia = {}

for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

mas_usadas = sorted(frecuencia.items(), key=lambda item: item[1], reverse=True)[:3]

print("Top 3 palabras más usadas:")
for palabra, cantidad in mas_usadas:
    print(f"{palabra}: {cantidad}")

#Ejercicio 34 Lee un archivo de texto `datos.txt` y muestra las 3 palabras más repetidas utilizando un diccionario.
with open("datos.txt", encoding="utf-8") as archivo:
    palabras = archivo.read().split()

contador = {}

for palabra in palabras:
    contador[palabra] = contador.get(palabra, 0) + 1

top_tres = sorted(contador.items(), key=lambda x: x[1], reverse=True)[:3]

print("Las 3 palabras más repetidas son:")
for palabra, veces in top_tres:
    print(f"{palabra} → {veces}")



#Ejercicio 35 Lee un archivo de texto `datos.txt` y muestra las 3 palabras más repetidas utilizando un diccionario.
with open("datos.txt", "r", encoding="utf-8") as doc:
    palabras = doc.read().split()

conteo = {}
for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1

top = sorted(conteo.items(), key=lambda x: x[1], reverse=True)[:3]

for palabra, cantidad in top:
    print(f"{palabra}: {cantidad} veces")




#Ejercicio 36 Lee un archivo de texto `datos.txt` y muestra las 3 palabras más repetidas utilizando un diccionario.
f = open("datos.txt", "r", encoding="utf-8")
datos = f.read()
f.close()

palabras = datos.split()
frecuencia = {}

for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

top = sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)[:3]

print("Palabras frecuentes:")
for p, c in top:
    print(f"{p}: {c}")




#Ejercicio 37 Lee un archivo de texto `datos.txt` y muestra las 3 palabras más repetidas utilizando un diccionario.
with open("datos.txt", "r", encoding="utf-8") as archivo:
    texto = archivo.read().split()

conteo = {}

for palabra in texto:
    conteo[palabra] = conteo.get(palabra, 0) + 1

top3 = sorted(conteo.items(), key=lambda x: x[1], reverse=True)[:3]

for palabra, veces in top3:
    print(f"{palabra}: {veces}")




#Ejercicio 38 Lee un archivo de texto `datos.txt` y muestra las 3 palabras más repetidas utilizando un diccionario.
archivo = open("datos.txt", encoding="utf-8")
contenido = archivo.read()
archivo.close()

palabras = contenido.split()
frecuencias = {}

for palabra in palabras:
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

top3 = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)[:3]

print("Top 3 palabras:")
for palabra, repeticiones in top3:
    print(f"{palabra} ({repeticiones})")



#Ejercicio 39 Lee un archivo de texto `datos.txt` y muestra las 3 palabras más repetidas utilizando un diccionario.
with open("datos.txt", "r", encoding="utf-8") as archivo:
    palabras = archivo.read().split()

frecuencia = {}
for p in palabras:
    frecuencia[p] = frecuencia.get(p, 0) + 1

top3 = sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)[:3]

print("Palabras más frecuentes:")
for palabra, veces in top3:
    print(f"{palabra}: {veces}")




#Ejercicio 40 Lee un archivo de texto `datos.txt` y muestra las 3 palabras más repetidas utilizando un diccionario.
with open("datos.txt", "r", encoding="utf-8") as archivo:
    texto = archivo.read().split()

dicc = {}

for palabra in texto:
    dicc[palabra] = dicc.get(palabra, 0) + 1

top = sorted(dicc.items(), key=lambda x: x[1], reverse=True)[:3]

print("Top 3:")
for palabra, cantidad in top:
    print(f"{palabra}: {cantidad}")



#Ejercicio 41 Simula una tienda usando diccionarios: muestra productos y precios, permite al usuario buscar productos.
tienda = {
    "pan": 0.50,
    "leche": 1.20,
    "queso": 2.50,
    "huevos": 1.80,
    "jugo": 1.00
}

print("Productos disponibles:")
for producto in tienda:
    print(f"- {producto} : ${tienda[producto]}")

busqueda = input("¿Qué producto deseas consultar? ").lower()

if busqueda in tienda:
    print(f"El precio de {busqueda} es: ${tienda[busqueda]}")
else:
    print("Producto no encontrado.")



#Ejercicio 42 Simula una tienda usando diccionarios: muestra productos y precios, permite al usuario buscar productos.
productos = {
    "arroz": 0.90,
    "azúcar": 0.85,
    "aceite": 3.00,
    "sal": 0.40,
    "café": 2.20
}

print("Catálogo:")
for p, precio in productos.items():
    print(f"{p}: ${precio}")

nombre = input("Producto a buscar: ").lower()

if nombre in productos:
    print(f"Precio de {nombre}: ${productos[nombre]}")
else:
    print("Ese producto no está disponible.")


#Ejercicio 43 Simula una tienda usando diccionarios: muestra productos y precios, permite al usuario buscar productos.
stock = {
    "camisa": 15.00,
    "pantalón": 25.00,
    "zapatos": 40.00,
    "gorra": 5.00,
    "chaqueta": 60.00
}

print("Lista de ropa en tienda:")
for item, precio in stock.items():
    print(f"{item}: ${precio}")

buscar = input("¿Qué prenda buscas? ").lower()

if buscar in stock:
    print(f"{buscar} cuesta ${stock[buscar]}")
else:
    print("No tenemos ese producto.")



#Ejercicio 44 Simula una tienda usando diccionarios: muestra productos y precios, permite al usuario buscar productos.
mercado = {
    "tomate": 0.30,
    "cebolla": 0.25,
    "papa": 0.40,
    "zanahoria": 0.35,
    "lechuga": 0.50
}

print("Productos en venta:")
for k, v in mercado.items():
    print(f"{k}: ${v}")

consulta = input("Consulta precio de producto: ").lower()

if consulta in mercado:
    print(f"Precio de {consulta}: ${mercado[consulta]}")
else:
    print("No encontrado.")



#Ejercicio 45 Simula una tienda usando diccionarios: muestra productos y precios, permite al usuario buscar productos.
almacen = {
    "celular": 250.00,
    "tablet": 300.00,
    "laptop": 700.00,
    "monitor": 150.00,
    "mouse": 20.00
}

print("Inventario de tecnología:")
for art, precio in almacen.items():
    print(f"{art}: ${precio}")

producto = input("¿Qué producto deseas buscar?: ").lower()

if producto in almacen:
    print(f"{producto} cuesta ${almacen[producto]}")
else:
    print("Producto no disponible.")


#Ejercicio 46 Simula una tienda usando diccionarios: muestra productos y precios, permite al usuario buscar productos.
menu = {
    "hamburguesa": 4.50,
    "pizza": 6.00,
    "empanada": 1.50,
    "hot dog": 3.00,
    "sánduche": 2.80
}

print("Menú del día:")
for item, precio in menu.items():
    print(f"{item}: ${precio}")

pedido = input("¿Qué deseas consultar del menú?: ").lower()

if pedido in menu:
    print(f"El precio de {pedido} es ${menu[pedido]}")
else:
    print("No está en el menú.")


#Ejercicio 47 Simula una tienda usando diccionarios: muestra productos y precios, permite al usuario buscar productos.
ferreteria = {
    "martillo": 5.00,
    "clavos": 1.00,
    "taladro": 45.00,
    "destornillador": 3.00,
    "alicate": 4.50
}

print("Herramientas disponibles:")
for producto, precio in ferreteria.items():
    print(f"{producto}: ${precio}")

consulta = input("Producto a buscar: ").lower()

if consulta in ferreteria:
    print(f"{consulta} cuesta ${ferreteria[consulta]}")
else:
    print("Producto no encontrado.")


#Ejercicio 48 Simula una tienda usando diccionarios: muestra productos y precios, permite al usuario buscar productos.
papeleria = {
    "cuaderno": 1.20,
    "lápiz": 0.30,
    "borrador": 0.25,
    "regla": 0.90,
    "colores": 2.50
}

print("Papelería:")
for item, precio in papeleria.items():
    print(f"{item}: ${precio}")

buscar = input("Consulta un artículo: ").lower()

if buscar in papeleria:
    print(f"{buscar} cuesta ${papeleria[buscar]}")
else:
    print("Artículo no encontrado.")



#Ejercicio 49 Simula una tienda usando diccionarios: muestra productos y precios, permite al usuario buscar productos.
cafeteria = {
    "café": 1.00,
    "té": 0.80,
    "jugo natural": 1.50,
    "agua": 0.70,
    "leche": 1.20
}

print("Bebidas disponibles:")
for bebida, precio in cafeteria.items():
    print(f"{bebida}: ${precio}")

busqueda = input("¿Qué bebida deseas consultar?: ").lower()

if busqueda in cafeteria:
    print(f"{busqueda} vale ${cafeteria[busqueda]}")
else:
    print("No tenemos esa bebida.")


#Ejercicio 50 Simula una tienda usando diccionarios: muestra productos y precios, permite al usuario buscar productos.
libreria = {
    "novela": 10.00,
    "cuento": 7.00,
    "revista": 3.50,
    "enciclopedia": 25.00,
    "diccionario": 12.00
}

print("Librería:")
for libro, precio in libreria.items():
    print(f"{libro}: ${precio}")

consulta = input("¿Qué libro deseas ver?: ").lower()

if consulta in libreria:
    print(f"El precio de {consulta} es ${libreria[consulta]}")
else:
    print("No lo tenemos en stock.")
