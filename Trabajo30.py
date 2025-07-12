with open('numeros.txt','r', encoding='utf-8') as archivo:
    numeros = [int(linea.strip()) for linea in archivo]

print("Suma total:", sum(numeros))