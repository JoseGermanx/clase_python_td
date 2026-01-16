
#Creación de la clase

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


#Instancia

persona1 = Persona("José", 25)
persona2 = Persona("Alicia", 40)

print(persona2.edad)

persona2.apellido = "Díaz"

print(persona2.apellido)

persona2.edad = 30
print(persona2.edad)