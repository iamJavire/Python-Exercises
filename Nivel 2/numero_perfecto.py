numero = int(input("Introduce un número entero: "))
numeroPerfecto = 0
sumaPerfecto = 0

divisores = []

for i in range (1, numero):

    if numero % i == 0:
        divisores.append(i)
        sumaPerfecto += i

if numero == sumaPerfecto:
    print(f"{numero} es un número perfecto. Sus divisores son {divisores}.")
else:
    print(f"{numero} NO es un número perfecto.")
