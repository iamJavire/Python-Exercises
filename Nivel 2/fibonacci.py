num, num2, num3 = 0, 0, 0

for i in range(0, 10):
    print(num)
    num3 = num2
    num2 = num
    if num == 0:
        num += 1
    else:
        num = num3+num2

"""Necesito almacenar el número usado para Print -> num1

FIBONACCI: 0 1 1 2 3 5 8 13 21 34
Bucle for con cantidad de 10 iteraciones
Primera iteración: print al número -> 0
Segunda iteración: Sumar 1
Tercera iteración: Número = Hace 2 números (num3) y Anterior número (num2) y actualizar num 2 y num 3

"""