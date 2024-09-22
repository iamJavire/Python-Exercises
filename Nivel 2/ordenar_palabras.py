listaPalabras = []
palabra = input("Añade una palabra ('fin' para terminar): ")

while palabra != "fin":
    listaPalabras.append(palabra)
    palabra = input("Añade otra palabra ('fin' para terminar): ")

# Ordenamos la lista
listaPalabras.sort()

# Mostramos las palabras ordenadas
print(f"Las palabras ordenadas son: {listaPalabras}")