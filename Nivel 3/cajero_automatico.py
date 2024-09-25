solicitaRetirar = input("¿Cuánto dinero (€) quiere retirar? ")
solicitaRetirar = int(solicitaRetirar)
Qbillete100 = 0
Qbillete50 = 0
Qbillete20 = 0
Qbillete10 = 0
Qbillete5 = 0

if (solicitaRetirar % 5 == 0):

    while solicitaRetirar >= 100:
        Qbillete100 += 1
        solicitaRetirar = solicitaRetirar - 100

    while solicitaRetirar >= 50:
        Qbillete50 += 1
        solicitaRetirar = solicitaRetirar - 50

    while solicitaRetirar >= 20:
        Qbillete20 += 1
        solicitaRetirar = solicitaRetirar - 20

    while solicitaRetirar >= 10:
        Qbillete10 += 1
        solicitaRetirar = solicitaRetirar - 10

    while solicitaRetirar >= 5:
        Qbillete5 += 1
        solicitaRetirar = solicitaRetirar - 5
    print(f"Ha retirado {Qbillete100} billetes de 100€, {Qbillete50} billetes de 50€, {Qbillete20} billetes de 20€, {Qbillete10} billetes de 10€ y {Qbillete5} billetes de 5€")

else:
    print("ERROR, debe ser un múltiplo de 5.")