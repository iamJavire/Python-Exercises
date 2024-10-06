numero = ""
suma = 0
sumaMaxima = 0
listaNumeros = []

while numero != "fin":
    numero = input("Introduzca un número o 'fin': ")
    if numero != "fin":
        listaNumeros.append(numero)

for i in listaNumeros:
    suma = listaNumeros[int.i]+listaNumeros[int.i+1]
    if suma > sumaMaxima:
        sumaMaxima = suma

print(f"{sumaMaxima}")