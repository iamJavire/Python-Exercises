entrada = input("Introduce números enteros separados por comas: ")

listaEnteros = [int(num.strip()) for num in entrada.split(",")]
setEnteros = set(listaEnteros)
listaEnteros = list(setEnteros)
listaEnteros.sort()

if len(listaEnteros) >= 2:
    print(f"El segundo mayor número es {listaEnteros[-2]}")
else:
    print("No hay suficientes números únicos para determinar el segundo mayor.")