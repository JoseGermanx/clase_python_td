#1. Uso de break para detener un bucle
# Se detiene la búsqueda de un número en una lista cuando se encuentra el número 7.


numeros = [3, 6, 8, 1, 2, 7, 45, 78, 90]

for numero in numeros:
    print(f"Número {numero}")
    if numero == 7:
        print("Se encontro el número 7")
        break



#2. Uso de continue para saltar iteraciones
# Imprimir los números del 1 al 10, pero saltar los múltiplos de 3.

for numero in range(1, 11):
    if numero % 3 == 0:
        continue
    print(numero)
