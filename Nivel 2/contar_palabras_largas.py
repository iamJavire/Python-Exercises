texto = input("Introduce un texto: ")
texto = texto.lower()
texto = texto.replace(",", "").replace(".", "").replace("?", "").replace("!", "")

listaPalabras = []
listaPalabras = texto.split()
mayCinco = 0

for palabra in listaPalabras:
    if len(palabra) > 5:
        mayCinco += 1

print(f"Hay {mayCinco} palabras con más de 5 letras.")