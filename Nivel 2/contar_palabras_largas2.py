texto = input("Introduce un texto: ")
palabras = []
contador = 0

texto = texto.lower()
texto = texto.replace(".","").replace(",","").replace("!","").replace("?","")

palabras = texto.split()

for palabra in palabras:
    if len(palabra) > 5:
        contador +=1
    else:
        contador +=0

print(f"Hay {contador} palabras mayores a 5 letras")