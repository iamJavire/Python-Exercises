enteros = input("Introduce números enteros separados por comas: ")
qPalindromo = 0

listaEnteros = [int(num.strip()) for num in enteros.split(",")]

for num in listaEnteros:
    if str(num) == str(num)[::-1]:
        qPalindromo += 1

print(f"Hay {qPalindromo} palíndromos")