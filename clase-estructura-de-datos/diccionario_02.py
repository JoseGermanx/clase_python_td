# Solicitar al usuario que ingrese una frase
# Dividir la frase en palabras usando .split()
# Crear un diccionario vacío llamado frecuencia
# Recorrer las palabras con un for
# Usar get() para contar cuántas veces aparece cada palabra
# Guardar cada conteo como clave: valor (palabra: cantidad)
# Imprimir el diccionario final con las frecuencias
# Bonus: Ordenar el diccionario por frecuencia descendente


frase = input("Ingrese una frase: ").lower()

palabras = frase.split()

frecuencia = {}

# palabras = [ "Esta", "es", "la", "frase", "Esta" ]
for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1  # { "Esta": 2, "es": 1, "la": 1, "frase": 1  }

frecuencia_ordenada = dict(
    sorted(frecuencia.items(), key=lambda item:item[1], reverse=True)
)

for palabra, cantidad in frecuencia_ordenada.items():
    print(f"{palabra}: {cantidad}")