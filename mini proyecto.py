def calcular_propina():
    try:
        # Pedir al usuario que ingrese el valor de la cuenta total (en dólares).
        cuenta = float(input("Ingrese el valor de la cuenta total en dólares: $"))

        # Ofrecer tres opciones de porcentaje de propina: 10%, 15% y 20%
        print("Seleccione el porcentaje de propina:")
        print("1. 10%")
        print("2. 15%")
        print("3. 20%")

        opcion = input("Ingrese 1, 2 o 3: ")

        #Calcular el valor de la propina multiplicando el valor de la cuenta por el porcentaje elegido.
        if opcion == "1":
            porcentaje = 0.10
        elif opcion == "2":
            porcentaje = 0.15
        elif opcion == "3":
            porcentaje = 0.20
        else:
            print("Opción no válida. Se aplicará el 15% por defecto.")
            porcentaje = 0.15

        #Calcular el total a pagar sumando la cuenta y la propina.
        propina = cuenta * porcentaje
        total = cuenta + propina

        #Mostrar un resumen al usuario con el desglose: cuenta, propina y total a pagar.
        print("\n--- Resumen ---")
        print(f"Cuenta: ${cuenta:.2f}")
        print(f"Propina ({porcentaje*100:.0f}%): ${propina:.2f}")
        print(f"Total a pagar: ${total:.2f}")

    except ValueError:
        print("Por favor, ingrese un número válido para el valor de la cuenta.")

# Ejecutar la función
calcular_propina()
