frase = input("Introduce una frase: ")
frase = frase.lower()

# Eliminar puntuación común
frase = frase.replace(",", "").replace(".", "").replace("?", "").replace("!", "")

listaPalabras = frase.split()

dicPalabras = {}

for palabra in listaPalabras:
    if palabra in dicPalabras:
        dicPalabras[palabra] += 1
    else:
        dicPalabras[palabra] = 1

print(f"Las palabras son: {dicPalabras}")