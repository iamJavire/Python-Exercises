num = int(input("Introduce un número entero: "))
num2 = num
factorial = 1

while num >= 1:
    factorial = num*factorial
    num -= 1

print(f"{factorial} es el factorial de {num2}")