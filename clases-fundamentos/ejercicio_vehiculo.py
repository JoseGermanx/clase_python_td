
# Consigna: ✍️
# Crea una clase Coche con los atributos marca, modelo, año y color.
class Coche:
    def __init__(self,marca, anio, modelo, color):
        self.marca = marca
        self.anio = anio
        self.modelo = modelo
        self.color = color

# Solicita al usuario los datos del coche y crea una instancia de la clase.

print("Bienvenido al sistema de gestión de vehículos")

marca_in = input("Ingrese la marca: ")
modelo_in = input("Ingrese el modelo: ")
anio_in = input("Ingrese el año: ")
color_in = input("Ingrese el color: ")

coche = Coche(marca_in, anio_in, modelo_in, color_in)

# Usa condicionales (if-else) para verificar si el coche es nuevo (año >= 2022) o usado (año < 2022).

if int(coche.anio) >= 2022:
    print("El coche es nuevo")
else:
    print("El coche es usado")

# Implementa un bucle while para permitir modificar atributos del coche hasta que el usuario decida salir.
# Utiliza break para salir del menú cuando el usuario lo indique.
# Usa continue para repetir el menú sin realizar cambios si el usuario ingresa una opción inválida.

while True:
    print("Indica el número de la opción a modificar: ")
    print("1. Modificar la marca ")
    print("2. Modificar el Modelo ")
    print("3. Modificar el Año ")
    print("4. Modificar el color ")
    print("5. Salir")

    opcion = input("Elige la opción: ")

    if opcion not in ["1","2","3","4","5"]:
        print("Opción incorrecta....")
        continue

    if opcion == "5":
        break


    if opcion == "1":
        coche.marca = input("Corrige la marca: ")
    elif opcion =="2":
        coche.modelo = input("Corrige el modelo: ")
    elif opcion == "3":
        coche.anio = input("Corrige el año: ")
    elif opcion == "4":
        coche.color = input("Corrige el color: ")

    print("Datos actualizados!!!!")

# Imprime la información final del coche antes de terminar el programa.
print("Estos son los datos que se registraron en el sistema: ")
print("------------------------------------------------------")
print("-------------------Datos del Coche--------------------")
print(f"Marca:{coche.marca}")
print(f"Modelo:{coche.modelo}")
print(f"Año:{coche.anio}")
print(f"Color:{coche.color}")

