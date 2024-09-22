num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))
num3 = int(input("Tercer número: "))
if num1 > num2 and num1 > num3:
    print(f"{num1} es el mayor.")
elif num2 > num1 and num2 > num3:
    print(f"{num2} es el mayor.")
else:
    print(f"{num3} es el mayor.")