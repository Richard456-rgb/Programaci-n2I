palabra_buscada = input("Palabra a buscar: ").lower()
contador = 0

with open("libro.txt", "r") as archivo:
    for linea in archivo:
        palabras = linea.lower().split()
        contador += palabras.count(palabra_buscada)

print(f"La palabra '{palabra_buscada}' aparece {contador} veces.")