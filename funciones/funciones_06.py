usuarios = [
    {
        "nombre": "Ana",
        "edad": 20,
        "intereses": ["programación", "música", "fotografía"]
    },
    {
        "nombre": "Luis",
        "edad": 17,
        "intereses": ["videojuegos", "diseño", "tecnología"]
    }
]

#procedimientos 
def listar_usuarios(usuarios):
    for usuario in usuarios:
        print("Datos de usuario:")
        print(f"Nombre: {usuario["nombre"]}")
        print(f"Edad: {usuario["edad"]}")
        print("Intereses:")
        for interes in usuario["intereses"]:
            print(f"{interes}")
        print("--------------------")

def imprimir_nombres_de_usuarios(usuarios):
    for usuario in usuarios:
        print(f"Nombre: {usuario["nombre"]}")


def get_user_by_name(usuario):
    pass


# listar_usuarios(usuarios)
# imprimir_nombres_de_usuarios(usuarios)

def verficar_acceso(edad):
    if edad >= 18:
        print("Acceso permitido")
    else:
        print("Acceso denegado.")

verficar_acceso(usuarios[1]["edad"])