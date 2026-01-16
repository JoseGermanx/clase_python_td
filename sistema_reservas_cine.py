# Consigna: ✍️
# Mostrar una lista de películas disponibles con horarios.
# Permitir al usuario seleccionar una película y la cantidad de boletos.
# Validar la disponibilidad de boletos.
# Mostrar el resumen final con la película, el número de boletos y el precio total.
# Permitir nuevas reservas hasta que el usuario decida salir.

# Paso a paso: ⚙️
# 1️⃣ Definir un diccionario con películas y horarios.
# 2️⃣ Usar un while para mostrar el menú y permitir que el usuario haga selecciones repetidas hasta que decida salir.
# 3️⃣ Solicitar la película y la cantidad de boletos.
# 4️⃣ Verificar disponibilidad de boletos antes de confirmar la compra.
# 5️⃣ Calcular el precio total basado en la cantidad de boletos comprados.
# 6️⃣ Permitir agregar más reservas o finalizar la compra.
# 7️⃣ Mostrar un resumen final con todas las reservas realizadas y el costo total.

catelera = {
    "Avatar": {"horario": "18:00", "precio": 10, "asientos": 50},
    "Titanic": {"horario": "20:00", "precio": 8, "asientos": 2 },
    "Toy Story": {"horario": "17:00", "precio": 5, "asientos": 20},
}

reserva_realizada = [] # Guardaremos una lista de diccionarios
total_precio_reserva = 0

print("----Bienvenido al cine----")

while True:
    print("Peliculas disponibles: ")
    for pelicula, informacion_pelicula in catelera.items():
        print(f" - {pelicula} |  Horario: {informacion_pelicula["horario"]} | Asientos disponibles: {informacion_pelicula["asientos"]} | Precio: ${informacion_pelicula["precio"]}" )
    
    pelicula_seleccionada = input("Ingresa el nombre de la película: ").capitalize()

    if pelicula_seleccionada not in catelera:
        print("Error: Esa película no está en cartelera.")
        continue

    try:
        cantidad_de_boletos = int(input("¿Cúantos boletos deseas?: "))
    except ValueError:
        print("Ingrese un número válido, por favor!")
        continue

    asientos_disponibles = catelera[pelicula_seleccionada]["asientos"]

    if cantidad_de_boletos <= asientos_disponibles:

        #lógica de descuento de asientos disponibles

        catelera[pelicula_seleccionada]["asientos"] -= cantidad_de_boletos

        #lógica cálculo de precio total de la película

        precio_pelicula = cantidad_de_boletos * catelera[pelicula_seleccionada]["precio"]

        reserva_realizada.append({
            "pelicula": pelicula_seleccionada,
            "cantidad": cantidad_de_boletos,
            "total": precio_pelicula
        })

        total_precio_reserva += precio_pelicula

        print(f"El precio a pagar por la película {pelicula_seleccionada} es: ${precio_pelicula}")
        print(f"Tu total parcial a pagar es: {total_precio_reserva}")

    else:
        print(f"Lo sentimos, sólo quedan {asientos_disponibles} asientos para las película {pelicula_seleccionada}")

    desea_continuar = input("¿Desea realizar otra reserva? (s/n): ")
    if desea_continuar != "s":
        break

print("Resumen de su compra")
for reserva in reserva_realizada:
    print(f"Película: {reserva["pelicula"]} - Boletos comprados: {reserva["cantidad"]} | Precio de la película: ${reserva["total"]} ")

print(f"Total de la compra: ${total_precio_reserva}")