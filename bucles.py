# 1. Uso de for para recorrer una lista
# Queremos imprimir los nombres de una lista de estudiantes.

# Ocupamos for cuando conocemos la cantidad de iteraciones

estudiantes = ["Ana", "Luis", "Pedro", "Lucia", "Alexandra", "Diego", "Marcelo"]

# for nombre in estudiantes:
#     print(f"El nombre del estudiantes es: {nombre}")




#2.  Uso de while con una condición de parada
# Pedimos un número al usuario y seguimos sumando hasta llegar o superar 50.

suma = 0

while suma < 50:
    numero = int(input("Ingrese un número: "))
    suma += numero
    print(f"valor actual de la suma: {suma} ")

print("La suma superó los 50!")