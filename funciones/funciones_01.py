

#1era parte

#Función que no recibe parámetros ni retorna ningún valor

def saludar():  #declaración de la función
    print("Hola, bienvenido a Python")

# saludar() # Invocar la función
# saludar() # Invocar la función
# saludar() # Invocar la función

#2da parte

# Función que recibe parámetros y retorna un valor
def multiplicar(a, b): #declaración de la función
    return a * b
    

# num_1 = int(input("Ingrese un número: "))
# num_2 = int(input("Ingrese un número: "))

# resultado = multiplicar(num_1,num_2) # Invocar la función
resultado_1 = multiplicar(5,4) # Invocar la función

# print(f"Resultado es: {resultado}")
# print(f"Resultado 1 es: {resultado_1}")

#3er parte

# Función que recibe parámetros y no retorna nada
def bienvenida(nombre):
    print(f"Hola {nombre}, que tengan un buen día.!!")

nombre_usuario = input("Dime tu nombre: ")

bienvenida(nombre_usuario)