listaNum = []
listaNumDif = []
num = input("Introduce un número o 'fin' para terminar: ")

while num != "fin":
    listaNum.append(int(num))
    num = input("Introduce un número o 'fin' para terminar: ")

for n in listaNum:
    if n not in listaNumDif:
        listaNumDif.append(n)

print(f"Los números son {listaNumDif}")