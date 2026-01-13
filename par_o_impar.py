# Determinar si un número es par, impar o múltiplo de 3

# Pide al usuario un número entero.
# Convierte la entrada con int.
# Usa una condición if con un operador lógico (and) para verificar si el número es divisible por 2 y por 3.
# Si no se cumple, agrega más condiciones para verificar si es par solamente, o si es impar y múltiplo de 3.
# En el caso contrario, indica que es impar y no múltiplo de 3.
# Usa mod (%) para evaluar divisibilidad.


numero = int(input("Ingrese un número: "))

if numero % 2 == 0 and numero % 3 == 0:
    print(f"El número {numero} es divisible por 2 y por 3!!")
elif numero % 2 == 0:
    print("El número es par!!")
elif numero % 3 == 0:
    print("El número es impar y múltiplo de 3!!")
else:
    print("El número es impar y no es múltiplo de 3!!")