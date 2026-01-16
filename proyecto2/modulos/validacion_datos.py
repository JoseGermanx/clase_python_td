

# Función para eliminar espacios en blanco en un input

def leer_str(texto):
    return input(texto).upper() #Convirtiendo a mayúsculas

def leer_int(texto):
    while True:
        try:
            return int(input(texto))
        except ValueError:
            print("Error: Ingrese un entero")


def leer_float(texto):
    while True:
        try:
            return float(input(texto))
        except ValueError:
            print("Error: Ingrese un número")