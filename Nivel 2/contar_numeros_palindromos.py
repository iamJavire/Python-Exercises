enteros = input("Introduce números enteros separados por comas: ")
qPalindromo = 0

listaEnteros = enteros.split(",")

for num in listaEnteros:
    if num == num[::-1]:
        qPalindromo += 1

print(f"Hay {qPalindromo} palíndromos")