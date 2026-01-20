# Crear un diccionario con los datos: nombre, edad, email
# Acceder a valores usando claves (persona["nombre"])
# Modificar un dato (por ejemplo, actualizar la edad)
# Agregar un nuevo dato ("país": "Argentina")
# Eliminar un campo con pop() o del
# Mostrar todas las claves, valores y pares con keys(), values(), items()
# Iterar sobre el diccionario e imprimir: "clave: valor"
# Usar get() para obtener un dato sin error si no existe

persona = {
    "nombre": "Juan",
    "edad": 25,
    "email": "email@email.com",
    "telefono": "56900000000"
}

edad_persona = persona["edad"]

print(f" El email de la persona es: {persona["email"]} y su edad es {edad_persona} ")

persona["email"] = "correo@correo.com"

print(f" El email de la persona es: {persona["email"]}")

persona["pais"] = "Chile"

print(f" El pais de la persona es: {persona["pais"]} ")

persona.pop("email")

# print(persona)

print(persona.keys()) # Muestra las claves

print(persona.values()) # Muestra los valores

print(persona.items()) #Muestra el conjunto clave-valor

for clave, valor in persona.items():
    print(f"{clave}: {valor}")

print(f"Teléfono: {persona.get("telefono", "No tiene teléfono")}")