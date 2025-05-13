#Sumar números ingresados por el usuario hasta que ingrese 0.

suma = 0
numero =int(input("ingrasa un numero (0 para terminar):"))
while numero != 0:
    suma +=numero
    numero = int(input ("ingresa otro numero (0 para terminar): "))
print("la suma total es:", suma)


#Adivinar un número aleatorio entre 1 y 100 (pistas: "mayor" o "menor").

numero_secreto = 7 
intento = int(input("Adivina el número (1-100): "))
while intento != numero_secreto:
    if intento < numero_secreto:
        print("El número es mayor.")
    elif intento > numero_secreto:
        print("El número es menor.")
    else:
        print("¡Correcto! Adivinaste el número.")
    intento= int(input("intenta de nuevo: "))
    
#Validar contraseña (repetir hasta que coincida con una guardada).

contrasena_correcta = "zhumir"
while True:
    entrada = input("Ingresa la contraseña: ")
    if entrada == contrasena_correcta:
        print("Acceso concedido.")
    else:
        print("Contraseña incorrecta. Intenta de nuevo.")

#Simular un cajero automático (menú: retirar, depositar, salir).

opcion = ""

while opcion != "3":
    
    print(" Bienvenido a Nuestro cajero ")
    print(" Ingrese 1 para retirar dinero")
    print(" Ingrese 2 para depositar dinero")
    print(" Ingrese 3 para salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        monto = float(input("¿Cuánto deseas retirar? "))
        print("Has retirado $",monto )
    elif opcion == "2":
        monto = float(input("¿Cuánto deseas depositar? "))
        print("Has depositado $",monto)
    elif opcion == "3":
        print("Gracias por usar el cajero. ¡Hasta luego!")
    else:
        print("Opción no válida. Intenta de nuevo.")



#Calcular la raíz cuadrada por aproximación (método babilónico).

numero = int(input("Ingresa un número: "))
x = numero
y = 1
contador = 0

while contador < 10:
    x = (x + numero // x) // 2
    contador = contador + 1

print("Raíz cuadrada aproximada:", x)

#Contar dígitos de un número entero (ej: 456 → 3).

numero = int(input("Ingresa un número entero: "))
numero = abs(numero)
contador = 0

while numero > 0:
    numero = numero // 10
    contador = contador + 1

print("Cantidad de dígitos:", contador)

#Generar la secuencia de Fibonacci hasta un límite.

limite = int(input("Ingresa el límite: "))
a, b = 0, 1
while a <= limite:
    print(a, end=" ")
    a, b = b, a + b
print()

#Encontrar números primos en un rango dado.

inicio = int(input("Inicio del rango: "))
fin = int(input("Fin del rango: "))
for num in range(inicio, fin + 1):
    if num > 1:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
print()

#Simular un temporizador (contar regresivamente desde N).

import time
n = int(input("Cuenta regresiva desde: "))
for i in range(n, -1, -1):
    print(i)
    time.sleep(1)

#Leer archivos línea por línea hasta fin de archivo.
print("Ingresa líneas de texto. Escribe 'FIN' para terminar.")
linea = ""

while linea != "FIN":
    linea = input()
    if linea != "FIN":
        print("Leído:", linea)