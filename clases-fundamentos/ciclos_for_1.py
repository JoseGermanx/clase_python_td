# ¿En qué consistirá la Demo?
# Mostrar cómo recorrer listas en Python usando for y numerarlas de manera ordenada.
# Crear una lista de elementos
# Definir una lista con 8 elementos.


lista_de_tareas = ["Estudiar", "Leer", "Programar", "Hacer ejercicio", "Cocinar", "Descansar", "Escuchar música", "Corregir tareas"]
              #        0         1        2



# Agregar el ciclo for
# Imprimir cada elemento en una nueva línea.

for tarea in lista_de_tareas:
    print(f"Ahora te toca hacer la tarea: {tarea}")

# Incluir enumerate()
# Utilizar enumerate() para obtener el índice de cada elemento.
# Configurar start=1 para numeración desde 1.
for num, tarea in enumerate(lista_de_tareas, start=1):
    print(f"{num}: {tarea}")


# Ejecutar y verificar la salida
