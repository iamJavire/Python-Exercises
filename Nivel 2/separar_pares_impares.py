listaNum = []
num = input("Introduce un número o 'fin': ")

while num != "fin":
    listaNum.append(int(num))
    num = input("Introduce un número o 'fin': ")

listaPar = []
listaImpar = []

for numero in listaNum:
    if numero % 2 == 0:
        listaPar.append(numero)
    else:
        listaImpar.append(numero)

print(f"Los número pares son: {listaPar} y los impares son: {listaImpar}.")