# Pedir al usuario que introduzca una lista de números enteros separados por espacios
entrada = input("Introduce una lista de números enteros separados por espacios: ")

# Convertir la entrada en una lista de enteros
listaNumeros = [int(num) for num in entrada.split()]

qPares = 0
qImpares = 0

for num in listaNumeros:
    if num % 2 == 0:
        qPares += 1
    else:
        qImpares += 1

print(f"Hay un total de {qPares} números pares y {qImpares} númeroes impares")