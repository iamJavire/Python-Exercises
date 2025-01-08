palabra = input("Introduce una palabra: ").lower()

if palabra == palabra[::-1]:
    print("Palíndromo")

else:
    print("No es palíndromo")


"""La palabra se debe leer igual de un lado que del otro
Por ejemplo: radar
"""