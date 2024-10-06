entrada = input("Introduce números enteros separados por comas: ")

listaEnteros = [int(num.strip()) for num in entrada.split(",")]
setEnteros = set(listaEnteros)
listaEnteros = list(setEnteros)
listaEnteros.sort()

print(f"El segundo mayor número es {listaEnteros[-2]}")