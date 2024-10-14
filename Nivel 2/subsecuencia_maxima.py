numero = ""
listaNumeros = []

# Recoger números del usuario
while numero != "fin":
    numero = input("Introduzca un número o 'fin': ")
    if numero != "fin":
        listaNumeros.append(int(numero))  # Convertimos a entero antes de añadir

# Algoritmo de Kadane para encontrar la subsecuencia de máxima suma
sumaMaxima = listaNumeros[0]  # Inicializamos la suma máxima con el primer número
sumaActual = 0

for numero in listaNumeros:
    sumaActual += numero  # Vamos sumando los números

    if sumaActual > sumaMaxima:
        sumaMaxima = sumaActual  # Actualizamos la suma máxima si encontramos una mayor

    if sumaActual < 0:
        sumaActual = 0  # Reiniciamos la suma si es negativa

# Mostrar la suma máxima encontrada
print(f"La suma máxima de la subsecuencia es: {sumaMaxima}")