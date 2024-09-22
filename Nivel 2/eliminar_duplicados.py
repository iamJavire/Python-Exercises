numEnteros = []
num = input("Introduce un número entero (o 'fin' para terminar): ")

while num != "fin":
    numEnteros.append(int(num))
    num = input("Introduce un número entero (o 'fin' para terminar): ")

conjEnteros = set(numEnteros)
numEnteros = list(conjEnteros)
numEnteros.sort()

print(f"Los números de la lista son: {numEnteros}")