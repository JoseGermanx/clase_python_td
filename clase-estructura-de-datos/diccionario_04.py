# Crear un diccionario productos donde cada clave sea un ID ("P001", "P002", etc.)
# Cada valor será un diccionario con los campos: nombre, precio, stock
# Acceder a los datos de un producto por su ID
# Agregar un nuevo producto al diccionario
# Modificar el stock de un producto existente
# Eliminar un producto usando pop()
# Iterar sobre todos los productos mostrando:
# "Producto: Teclado | Precio: $5000 | Stock: 10"
# Bonus: Mostrar solo los productos con stock menor a 10

productos = {
    "P001": {"nombre": "Teclado", "precio": 5000, "stock": 10},
    "P002": {"nombre": "Mouse", "precio": 3000, "stock": 25},
    "P003": {"nombre": "Monitor", "precio": 80000, "stock": 5},
}

print("Datos del producto: ", productos["P001"])

productos["P004"] = {"nombre": "Auriculares", "precio": 12000, "stock": 8}

productos["P002"]["stock"] = 24

productos.pop("P001")

for id_producto, producto in productos.items():
    print(f"id: {id_producto} - Producto: {producto["nombre"]} | Precio: {producto["precio"]} | Stock: {producto["stock"]}")

print("Productos con stock menor a 1o unidades!!")
for id_producto, producto in productos.items():
    if producto["stock"] < 10:
        print(f"id: {id_producto} - Producto: {producto["nombre"]} | Precio: {producto["precio"]} | Stock: {producto["stock"]}")

