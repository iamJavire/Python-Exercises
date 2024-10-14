import random

listaPalabras = ["marina","javier","gato","perro","casa"]
palabraSecreta = random.choice(listaPalabras)
listaLetras = palabraSecreta.split()

letra = ""
letrasAdivinadas = []

nLimite = 6

progresoPalabra = []
mostrarProgreso = []

print(f"Bienvenido al juego del ahorcado, averigua la palabra {progresoPalabra}")

# Unir la lista en una cadena separada por espacios y mostrarla



for i in range (0,nLimite):
    letra = input("Introduce una letra: ")

    if letra in listaLetras:
        letrasAdivinadas.append(letra)
    
    for i in palabraSecreta:
        if i in letrasAdivinadas:
            progresoPalabra.append(letra)
        else:
            progresoPalabra.append("_")
    
    progresoMostrado = " ".join(progresoPalabra)
    print(progresoMostrado)

    if progresoMostrado == listaLetras and i <= nLimite:
        print("¡Ganaste!")
    else:
        print("Perdiste. Juega de nuevo.")

