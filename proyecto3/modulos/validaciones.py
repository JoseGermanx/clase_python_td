
def leer_float(texto):
    while True:
        try:
            return float(input(texto))
        except ValueError:
            print("Error: Ingrese un valor válido!!")


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

