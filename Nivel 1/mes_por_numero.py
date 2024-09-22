meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
numMes = int(input("Pon el número del mes: "))

if 1<=numMes<=12:
    print(f"Haz ingresado el número {numMes} que corresponde a {meses[numMes-1]}")
else:
    print("Número no válido")