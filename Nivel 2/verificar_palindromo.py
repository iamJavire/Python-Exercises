palindromo = input("Introduce una frase: ")
palindromo = palindromo.lower().replace(" ","")
alreves = palindromo[::-1]

if alreves == palindromo:
    print("Es un palindromo")
else:
    print("No es un palindromo")