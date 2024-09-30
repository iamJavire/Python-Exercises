def nuevo_producto():
    nProducto = input("Por favor, cree el nuevo producto: ")
    QnProducto = int(input("Por favor, añade la cantidad del nuevo producto: "))
    inventario [nuevo_producto.nProducto] = nuevo_producto.QnProducto

def actualizar_producto():
    nProducto = input("¿Qué producto quiere actualizar? ")
    QnProducto = int(input("Por favor, añade la cantidad del producto: "))
    for nProducto in inventario:
        inventario [nuevo_producto.nProducto] = nuevo_producto.QnProducto

def eliminar_producto():
    nProducto = input("¿Qué producto quiere eliminar? ")
    del nProducto

def ver_inventario():
    print(f"El inventario es {inventario}")

accion = input("Bienvenido, ¿qué quiere hacer? Nuevo-Actualizar-Eliminar-Ver-Fin: ")
accion = accion.lower()
inventario = {}

while accion != "nuevo" or accion != "actualizar" or accion != "eliminar" or accion != "ver" or accion != "fin":

    # Nuevo producto
    if accion != "fin" and accion == "nuevo":
        nuevo_producto
            
    ### Actualizar producto
    elif accion != "fin" and accion == "actualizar":
        actualizar_producto

    ### Eliminar producto
    elif accion != "fin" and accion == "eliminar":
        eliminar_producto

    ### Ver producto
    elif accion != "fin" and accion == "ver":
        ver_inventario
    
    accion = input("Introduce: Nuevo-Actualizar-Eliminar-Ver-Fin")

