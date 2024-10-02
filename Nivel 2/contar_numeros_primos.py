def es_primo(num):
    if num <= 1:
        return False
    if num == 1:
        return True
    if num % 2 == 0:
        return False
    for i in range (3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True


numEntero = input("Introduce un número o 'fin': ")
listaEnteros = []
qPrimos = 0

while numEntero != "fin":
    listaEnteros.append(int(numEntero))
    numEntero = input("Introduce un número o 'fin': ")

for num in listaEnteros:
    if es_primo(num):
        qPrimos += 1

print(f"Hay {qPrimos} números primos")