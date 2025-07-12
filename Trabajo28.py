with open("nombres.txt", "w") as archivo:
    for i in range(5):
        nombre = input(f"Ingrese el nombre {i+1}: ")
        archivo.write(nombre + "\n")