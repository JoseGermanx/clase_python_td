
from modulos.validacion_datos import leer_str, leer_int, leer_float

# Declarar variables para capturar nombre, edad, tipo de usuario, etc.
# Validar tipo de dato con int(), float(), str(), etc.
# Utilizar operadores aritméticos, de comparación y lógicos.
# Crear los primeros registros usando listas y diccionarios.
# 📂 Archivos esperados:
# /main.py (actualizado)
# /modulos/validacion_datos.py (funciones de carga de datos)

lista_destacada = []

nombre = leer_str("Indique su nombre: ")
edad = leer_int("Ingrese su edad: ")
promedio_notas = leer_float("Ingrese su nota: ")

#Creamos diccionario
estudiante = {
    "nombre": nombre,
    "edad": edad,
    "promedio": promedio_notas
}

if estudiante["promedio"] >= 6:
#Guardamos diccionario en lista
    lista_destacada.append(estudiante)


#Imprimimos resultado

print(lista_destacada)

