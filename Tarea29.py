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

#Contar dígitos de un número entero (ej: 456 → 3).

#Generar la secuencia de Fibonacci hasta un límite.

#Encontrar números primos en un rango dado.

#Simular un temporizador (contar regresivamente desde N).

#Leer archivos línea por línea hasta fin de archivo.



# Mientras - While
# Visualizar los 5 primeros numeros con mientras = while 
