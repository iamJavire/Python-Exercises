listaNum = []
num = input("Introduce un número hasta que ingreses 'fin': ")

while num != "fin":
    listaNum.append(float(num))
    num = input("Introduce un número hasta que ingreses 'fin': ")

if len(listaNum) >0:
    suma = sum(listaNum)
    promedio = suma / len(listaNum)
    print(f"El promedio es {promedio:.2f}")
else:
    print("No se introdujeron números")