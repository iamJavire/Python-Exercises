frase = input("Introduce la frase: ")
frase = frase.lower()

dicCaracter = {}

for caracter in frase:
    if caracter in dicCaracter:
        dicCaracter[caracter] += 1
    else:
        dicCaracter[caracter] = 1

print(f"Los caracteres son: {dicCaracter}")
