texto = input("Introduce las palabras: ")
texto = texto.lower()
texto = texto.replace(",","").replace(".","").replace("!","").replace("?","")

listaPalabras = texto.split()
listaPalabras.sort(key=lambda palabra: (len(palabra), palabra))

# Mostramos la lista ordenada
print(f"La lista ordenada es: {listaPalabras}")