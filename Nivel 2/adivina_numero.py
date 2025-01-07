secreto = 4
print("El juego consiste en adivinar el número del 1 al 10 \nPodrás repetir hasta que lo aciertes")
num = int(input("Introduce un número: "))

if num != secreto:
    while num != secreto:
        print("Incorrecto, prueba otra vez: ")
        num = int(input("Introduce un número: "))

print("¡Enhorabuena, has acertado!")