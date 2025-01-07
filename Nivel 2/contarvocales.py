palabra = input("Introduce una palabra: ").lower()
vocal = 0

for letra in palabra:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        vocal += 1

print(f"Hay {vocal} vocales en {palabra}")