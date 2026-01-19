
# Crear una lista inicial con tareas
# Mostrar todas las tareas actuales
# Agregar una nueva tarea a la lista
# Marcar una tarea como completada (eliminarla)
# Recorrer e imprimir la lista de tareas con un for
# Usar pop() para eliminar tareas por índice
# Validar si la lista está vacía
# Mostrar mensaje de cierre: "¡Todas las tareas completadas!"

tareas = ["Estudiar Python", "Hacer ejercicios", "Leer documentación de listas"] #lista inicial
#              0                    1                          2

while True:
    if not tareas:
        print("¡Todas las tareas completadas!")
        break
    print("Lista de tareas actuales: ")
    for indice, tarea in enumerate(tareas, start=1):
        print(f"{indice}. {tarea}")
    
    print("Opciones [1-3]: ")
    print("1. Agregar tarea.")
    print("2. Eliminar (completar) tarea.")
    print("3. Salir.")

    opcion = input("Elige la opción: ")

    if opcion == "1":
        nueva_tarea = input("Nueva tarea: ")
        tareas.append(nueva_tarea)
    elif opcion == "2":
        indice = input("Indica el indice de tarea completada: ")
        if indice.isdigit():
            indice = int(indice) - 1
            tareas.pop(indice)
        else:
            print("Debes ingresar un número")
    elif opcion == "3":
        print("Cerrando sistema de tareas")
        break
    else:
        print("Opción inválida!")
