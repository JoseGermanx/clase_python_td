# Consigna: ✍️
# Desarrollar un programa que permita:
# Registrar múltiples estudiantes representados por tuplas dentro de una lista.
# Mostrar todos los registros con formato legible.
# Permitir consultar cuántos estudiantes son de una ciudad específica.
# Mostrar la edad promedio de los estudiantes registrados.
# Paso a paso: ⚙️
# Crear una lista vacía llamada estudiantes.

# Cada entrada será una tupla con 3 datos: (nombre, edad, ciudad).

# Agregar al menos 5 estudiantes con datos variados.

# Recorrer la lista e imprimir cada estudiante con el formato:
# "Nombre: Ana, Edad: 25, Ciudad: Córdoba"

# Pedir al usuario que ingrese una ciudad, y contar cuántos estudiantes son de esa ciudad.

# Calcular la edad promedio de todos los estudiantes (sumar edades / total).

# Bonus: Permitir agregar un nuevo estudiante desde consola.  


estudiantes = [("Ana", 25, "Santiago"),("Luis", 30, "Rancagua"), ("María", 22, "Valparaiso"), ("Pedro", 28, "Quilpué"), ("Alberto", 45, "Santiago")]

while True:
    print("------Menú-------")
    print("1. Listar Estudiantes.")
    print("2. Buscar por ciudad.")
    print("3. Calcular edad promedio.")
    print("4. Agregar un nuevo estudiante.")
    print("5. Salir.")

    opcion = input("Selección una opción: ")

    if opcion == "1":
        for nombre, edad, ciudad in estudiantes:
            print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")
    elif opcion == "2":
        ciudad_busqueda = input("Ingrese la ciudad: ")
        total_estudiantes_por_ciudad = 0
        for _, _, ciudad in estudiantes:
            if ciudad_busqueda.lower() == ciudad.lower():
                total_estudiantes_por_ciudad += 1
        print(f"Estudiantes de {ciudad_busqueda.capitalize()}: {total_estudiantes_por_ciudad}")
    elif opcion == "3":
        sumatoria_edades = 0
        for _, edad, _, in estudiantes:
            sumatoria_edades += edad
        promedio_edades = sumatoria_edades / len(estudiantes)
        print(f"Edad promedio: {promedio_edades: 2f}")
    elif opcion == "4":
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))
        ciudad = input("Ingrese la ciudad: ")
        estudiantes.append((nombre, edad, ciudad))
        print("Estudiante agregado correctamente!")
    elif opcion == "5":
        print("Saliendo del programa!")
        break
    else:
        print("Opción inválida!")