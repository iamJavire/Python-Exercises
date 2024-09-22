num = input("Introduce un número o 'fin': ")
listaNum = []

while num != "fin":
    listaNum.append(int(num))
    num = input("Introduce un número o 'fin': ")

suma = 0

for i in range(1, len(listaNum), 2):
    suma += listaNum[i]

print(f"La suma de números en posiciones impares es: {suma}")