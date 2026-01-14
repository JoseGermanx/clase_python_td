# Una tienda de electrónicos necesita un sistema que ayude a clasificar los productos según su disponibilidad y tipo. Dependiendo de si un producto está en stock o no, y de la categoría a la que pertenece (electrodoméstico, teléfono, computadora, accesorio, etc.), el sistema debe proporcionar información adecuada al cliente.

# Paso a paso: ⚙️
# Identificar qué condición debe evaluarse primero: Determinar si el producto está disponible o no.
# Aplicar una condición simple: Si el producto está agotado, se muestra un mensaje de "Sin stock".
# Implementar condicional múltiple: Si el producto está disponible, evaluar a qué categoría pertenece y mostrar un mensaje específico.
# Considerar el caso en el que el producto no pertenezca a ninguna categoría conocida: Manejar una salida alternativa.
# Validar entradas: Pensar en qué ocurriría si se introduce un valor no válido o vacío.

productos_en_stock = ["iphone 15", "lavadora", "teclado"]
categorias = ["electrodomestico", "telefono", "accesorio"]

producto = input("Indique un producto: ")


if producto.lower().strip() not in productos_en_stock:
    print("El producto no está en stock")
else:
    categoria  = input("Indique una categoria: ")
    if categoria not in categorias:
        print("Categoría no existente!")
    elif categoria == "electrodomestico" and producto.lower().strip() == "lavadora":
        print(f"El producto {producto} está en stock y pertenece a la categoría {categoria}")
    elif categoria == "telefono" and producto.lower().strip() == "iphone 15":
        print(f"El producto {producto} está en stock y pertenece a la categoría {categoria}")
    elif categoria == "accesorio" and producto.lower().strip() == "teclado":
        print(f"El producto {producto} está en stock y pertenece a la categoría {categoria}")
    else:
        print(f"El producto {producto} se encuentra en stock pero no pertenece a esa categoría.")



print("Programa finalizado!!")