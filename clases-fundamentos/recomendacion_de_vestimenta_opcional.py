

try:
    temperatura_actual = float(input("Indica la temperatura actual, por favor: "))

    if temperatura_actual < 10:
       print("🧥 Usa abrigo grueso y bufanda")
    elif temperatura_actual <= 20:
       print("🧣 Usa chaqueta ligera")
    elif temperatura_actual <= 30:
       print("🩳 Usa ropa cómoda y fresca")
    else:
       print("🧢 Usa ropa ligera y protector solar")

except ValueError:
   print("Error: Ingresaste un valor incorrecto!!")