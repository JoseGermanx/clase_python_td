
# Verificar si un número es positivo, negativo o cero
# Pide al usuario que ingrese un número decimal.
# Convierte la entrada a número (float).
# Usa una estructura if para verificar si es mayor a cero.
# Si no lo es, agrega una condición elif para comprobar si es menor a cero.
# Si ninguna de las anteriores se cumple, usa else para indicar que el número es cero.
# Muestra un mensaje apropiado según el caso.

# recepción de input y conversióna float en un sólo paso
# valor = float(input("Ingrese un número: ")) 

valor_recibido = input("Ingrese un número: ")  #Recibe el dato como un str (tipo texto)

valor_recibido_convertido = float(valor_recibido) # Convirtiendo la entrada del input a float

if valor_recibido_convertido > 0:
    print("El número es positivo!!")
elif valor_recibido_convertido < 0:
    print("El número es negativo!!")
else:
    print("El número es cero!!")