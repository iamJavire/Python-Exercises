frase = input("Introduce una frase: ")
frase = frase.lower()
contador = 0

for n in frase:
    if n == "a" or n == "e" or n == "i" or n == "o" or n == "u":
        contador += 1

print(f"Un total de {contador} vocales")