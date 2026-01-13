# Sistema de recomendación de vestimenta 
# Pídele al usuario que ingrese la temperatura del día.
# Convierte ese valor a tipo numérico (usá int() o float()).

temperatura_actual = input("Indica la temperatura actual, por favor: ")

# Si el usuario ingresa un valor inválido (texto, negativo, etc.), muestra un mensaje de error
if temperatura_actual.isdigit():
    temperatura_convertida = float(temperatura_actual)
    if temperatura_convertida < 10:
        print("🧥 Usa abrigo grueso y bufanda")
    elif temperatura_convertida <= 20:
        print("🧣 Usa chaqueta ligera")
    elif temperatura_convertida <= 30:
        print("🩳 Usa ropa cómoda y fresca")
    else:
        print("🧢 Usa ropa ligera y protector solar")

else:
    print("Error: Ingresaste un valor incorrecto!!")


# Implementa una estructura condicional (if, elif, else) que cubra los siguientes rangos:


# Menos de 10°C → Mostrar: "🧥 Usá abrigo grueso y bufanda"
# Entre 10°C y 20°C → Mostrar: "🧣 Usá chaqueta ligera"
# Entre 21°C y 30°C → Mostrar: "🩳 Usá ropa cómoda y fresca"
# Más de 30°C → Mostrar: "🧢 Usá ropa ligera y protector solar"

