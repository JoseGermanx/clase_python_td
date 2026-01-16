# Verificar la instalación de Python y configurar VS Code.
# Crear una estructura mínima de proyecto con módulos separados.
# Definir una función para sumar dos números enteros.
# Usar input() para capturar los números desde la consola.
# Llamar a una función del módulo e imprimir el resultado usando f-string.
# Añadir comentarios en el código explicando su propósito y estructura.
# Probar ejecución desde terminal o desde el entorno.

from modulos.operaciones import sumar 

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

resultado = sumar(num1, num2)

print(f"El resultado de la suma de {num1} + {num2} es igual {resultado}")

lista = []

lista.append(3)
