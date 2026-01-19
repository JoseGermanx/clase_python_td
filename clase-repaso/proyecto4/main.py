# Crear un menú con while True que permita al usuario interactuar con una lista de tareas.
# Las opciones del menú deben incluir: agregar tarea, ver tareas, marcar tarea como hecha, y salir.
# Utilizar break para salir del programa y continue para volver al menú sin ejecutar código extra.
# Simular la gestión de tareas usando listas y diccionarios con campos como "tarea" y "completado".
# Separar el código en módulos menu.py y gestion_tareas.py.

from modulos.mostrar_menu import mostrar_menu, leer_int
from modulos.gestion_tareas import agregar_tarea, listar_tareas, marcar_completada, eliminar_tarea

while True:
    mostrar_menu()
    opcion = leer_int("Selecciona una opción: ")

    if opcion == 1:
        texto_tarea = input("Ingresa la nueva tarea: ")
        agregar_tarea(texto_tarea)
    
    if opcion == 2:
        listar_tareas()

    if opcion == 3:
        indice = leer_int("Número de tarea completadar: ") - 1
        marcar_completada(indice)
        listar_tareas()
    
    if opcion == 4:
        indice = leer_int("Número de tarea a eliminar: ") - 1
        eliminar_tarea(indice)
        listar_tareas()

    if opcion == 5:
        print("Saliendo del sistema, gracias por usar nuestro gestor de tareas!")
        break

    


        




