dias_semana = ["lunes","martes","miércoles","jueves","viernes","sábado","domingo"]
numDia = int(input("Introduce un número del 1 al 7: "))

if 1 <= numDia <= 7:
    print(f"Es {dias_semana[numDia - 1]}")
else:
    print("Número inválido: debe ser entre el 1 y el 7")