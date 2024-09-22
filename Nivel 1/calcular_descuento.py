precioProducto = float(input("Introduce el precio del producto: "))
descuento = float(input("Introduce el descuento (%): "))
precioFinal = precioProducto-precioProducto*descuento/100
print(f"El precio final es: {precioFinal:.2f}")