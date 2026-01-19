

def mostrar_menu():
    print("-------- MENÚ GESTIÓN TAREAS --------")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea completada")
    print("4. Eliminar tarea")
    print("5. Salir")

def leer_int(texto):
    while True:
        try:
            return int(input(texto))
        except ValueError:
            print("Error: Ingrese un entero")