listaNum = []
num = input("Introduce un número ('fin' para salir): ")

while num != "fin":
    listaNum.append(int(num))
    num = input("Introduce un número ('fin' para salir): ")

if len(listaNum) > 0:
    maximo = listaNum[0]
    minimo = listaNum[0]

    for n in listaNum:
        if n > maximo:
            maximo = n
        if n < minimo:
            minimo = n
    
    # Mostrar el resultado
    print(f"El número máximo es {maximo} y el número mínimo es {minimo}.")
else:
    print("No se introdujeron números.")