# Contexto: 🙌
# El objetivo del ejercicio es practicar la creación y uso de funciones en Python. Deberán escribir dos funciones: una para convertir grados Celsius a Fahrenheit, y otra para calcular el área de un triángulo. Luego, deberán llamar a esas funciones con diferentes valores y mostrar los resultados.

# Consigna: ✍️
# Escribe una función llamada celsius_a_fahrenheit que convierta una temperatura de grados Celsius a Fahrenheit. Usa la fórmula:

def celsius_a_fahrenheit(celsius):
    resultado = (celsius * 9/5) + 32
    return resultado


# Escribe una función llamada area_triangulo que calcule el área de un triángulo dados su base y altura, usando la fórmula:

def area_triangulo(base, altura):
    resultado = (base*altura) / 2
    return resultado

while True:
    print("Calculadora y convertidor")
    print("1. Convertir Celsius a fahrenheit.")
    print("2. Calcular área de un triángulo.")
    print("3. Salir")

    opcion = input("Indique que desea realizar [1 -3]: ")

    if opcion == "1":
        celsius = float(input("Ingrese los grados centígrados: "))
        print(f"Los {celsius} grados celsius, equivalen a {celsius_a_fahrenheit(celsius)} fahrenheit.")
    elif opcion == "2":
        base = float(input("Ingresa el valor de la base: "))
        altura = float(input("Ingresa el valor de la altura: "))
        print(f"El área del triángulo es: {area_triangulo(base, altura)}")
    elif opcion == "3":
        print("Saliendo del sistema.")
        break

