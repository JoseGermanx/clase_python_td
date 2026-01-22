
# Retorno de múltiples valores

def operaciones_matematicas(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1*num2
    return suma, resta, multiplicacion

resultado_suma, resultado_resta, resultado_multi = operaciones_matematicas(4,5)

#print(f"Resultado 1: {resultado_suma}, Resultado 2: {resultado_resta}, Resultado 3: {resultado_multi}")

# Scope - Contexto de uso de las variables

contador = 10 # variables global


def aumentar_contador():
    variable = 5 # variables local
    print(f"Variable dentro de una función: {contador}")


# aumentar_contador()
# print(f"Varible fuera de una función: {contador}")


# Recursividad (contar hasta cero)

def contar_hasta_cero(numero):
    if numero == 0:
        print("Fin")
        return
    print(numero)
    contar_hasta_cero(numero - 1)


contar_hasta_cero(5)