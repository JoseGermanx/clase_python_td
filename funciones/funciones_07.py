
def saludar_usuario(nombre):
    print(f"Hola, {nombre}. Bienvenido/a.")

def imprimir_numeros(numero):
    for numero in range(1, numero + 1):
        print(numero)


# saludar_usuario("Alberto")
# imprimir_numeros(20)


# Gestión de un menú de comida

menu = {
    "Pizza": 8000,
    "Hamburguesa": 6500,
    "Ensalada": 5000,
    "Bebida": 2000
}

pedido_del_cliente = ["Pizza", "Bebida", "Ensalada"]

def mostrar_menu(menu):
    print("Menú del Restaurante:")
    for plato, precio in menu.items():
        print(f"{plato}: {precio}")


def calcular_total_del_pedido(menu, listas_de_platos):
    total = 0
    for plato in listas_de_platos:
        total += menu.get(plato, 0)
    print(f"El total de la cuenta del cliente es: ${total}")


# mostrar_menu(menu)
calcular_total_del_pedido(menu, pedido_del_cliente)