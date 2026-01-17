
def leer_float(texto):
    while True:
        try:
            return float(input(texto))
        except ValueError:
            print("Error: Ingrese un valor válido!!")

def leer_int(texto):
    while True:
        try:
            return int(input(texto))
        except ValueError:
            print("Error: Ingrese un entero")

def clasificar_temperaturas(temperatura):
    if temperatura < 5:
        return "Muy frío"
    elif 5 <= temperatura < 15:
        return "Frío"
    elif 15 <= temperatura < 25:
        return "Agradable"
    elif 25 <= temperatura < 35:
        return "Caluroso"
    else:
        return "Extremo"

def clasificar_edad(edad):
    if edad > 60:
        return "Adulto mayor"
    else:
        return "No es adulto mayor"