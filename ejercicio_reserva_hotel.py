# Un hotel necesita un sistema para gestionar reservas de habitaciones. Dependiendo del tipo de habitación que el usuario seleccione (ingresando un número del 1 al 5), el programa debe mostrar la categoría de la habitación y su precio por noche.
# Consigna: ✍️
# Genera un diagrama de flujo que muestre el funcionamiento del programa y permita:
# Usar switch (con diccionarios en Python) para definir las habitaciones y sus precios.
# Permitir que el usuario ingrese la cantidad de noches y calcular el total a pagar.
# Aplicar snake_case en las variables.
# Manejar errores si el usuario ingresa un número incorrecto o un valor no válido.
# Paso a paso: ⚙️
# 1️⃣ Solicitar entrada al usuario
# 2️⃣ Definir las habitaciones y sus precios en un diccionario:
# 3️⃣ Usar get() en el diccionario:
# 4️⃣ Calcular el total a pagar:
# 5️⃣ Mostrar el resultado en pantalla:
# 6️⃣ Manejo de errores:


# habitaciones
# 1 simple,
# 2 doble,
# 3 suite 

habitaciones = {
    1: {"categoria": "simple", "precio": 50},
    2: {"categoria": "doble", "precio": 80},
    3: {"categoria": "suite", "precio": 150},
    4: {"categoria": "presidencial", "precio": 250}
}


#Menú de bienvenida
print("Bienvenido al hotel Paraiso")
print("Opciones disponibles")
for num, datos in habitaciones.items():
    # 1. Habitación simple - Precio: 50/noche
    print(f"{num}. Habitación {datos["categoria"]} - Precio: {datos["precio"]}/noche.")
try:
    seleccion = int(input("Ingresa que tipo de habitación deseas: [1-4]: "))

    habitación_seleccionada = habitaciones.get(seleccion)

    #validar si exite el tipo de habitación y la cantidad de noches es mayor a 0
    if habitación_seleccionada:
        cantidad_de_noches = int(input("Ingresa la cantidad de noches: "))
        if cantidad_de_noches > 0:
            total_a_pagar = habitación_seleccionada["precio"] * cantidad_de_noches

            # Generar reserva
            print("---Datos de su reserva-----")
            print(f"Habitación {habitación_seleccionada["categoria"]}")
            print(f"Precio unitario: {habitación_seleccionada["precio"]}")
            print(f"Total de la reserva: {total_a_pagar}")
        else:
            print("Error: La cantidad de noches debe ser mayor a 0")
    else:
         print("Tipo de habitación no exite.")
except ValueError:
    print("Error: Por favor ingresa un número entero!!")























# Preguntas de Reflexión:

# ¿Cómo mejoraría este sistema con más funcionalidades (por ejemplo, descuentos por estadías largas)?
# ¿Por qué switch (o diccionarios en Python) es más eficiente que múltiples if-elif-else en este caso?
# ¿Cómo podemos asegurarnos de que el usuario no ingrese valores incorrectos?
