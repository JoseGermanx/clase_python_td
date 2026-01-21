# Contexto: 🙌
# Una biblioteca necesita un sistema básico para gestionar su colección de libros. Cada libro tiene un código, título, autor, género y cantidad disponible. Además, se desea consultar libros por género, verificar stock y contar cuántos libros únicos hay.
# Consigna: ✍️
# Crear un sistema que:
# Registre libros usando diccionarios anidados
# Permita consultar libros por género usando sets
# Use tuplas para representar datos fijos como (autor, año)
# Genere estadísticas usando listas y Counter

# Paso a paso: ⚙️
# Crear un diccionario llamado libros donde la clave sea un ID ("B001", "B002", etc.)
# Cada valor será un diccionario con:

# "titulo": cadena
# "autor": tupla con (nombre, año de nacimiento)
# "genero": cadena
# "stock": entero

# Mostrar todos los libros disponibles
# Permitir buscar libros por género ingresado por el usuario
# Calcular cuántos libros hay por género usando Counter
# Mostrar solo los libros con stock menor a 3 unidades
# Agregar un nuevo libro y actualizar el stock de uno existente
# Bonus: Eliminar un libro del diccionario por su código

from collections import Counter

libros = {
    "B001": {
        "titulo": "1984",
        "autor": ("George Orwell", 1903),
        "genero": "Distopía",
        "stock": 5
    },
    "B002": {
        "titulo": "El Hobbit",
        "autor": ("J. R. R. Tolkien", 1892),
        "genero": "Fantasía",
        "stock": 2
    },
    "B003": {
        "titulo": "Fahrenheit 451",
        "autor": ("Ray Bradbury", 1920),
        "genero": "Distopía",
        "stock": 1
    }
}

while True:
    print("--Menú Sistema Biblioteca--")
    print("1. Mostrar todos los libros")
    print("2. Buscar libros por género")
    print("3. Estadísticas por género")
    print("4. Mostrar libros con bajo stock")
    print("5. Agregar nuevo libro")
    print("6. Actualizar stock")
    print("7. Eliminar libro")
    print("8. Salir")

    opcion = input("Selección una opción: ")

    if opcion == "1":
        for codigo, datos in libros.items():
            print(f"{codigo} - {datos["titulo"]} | Stock: {datos["stock"]}")

    elif opcion == "2":
        genero = input("Ingrese el género: ")
        genero_encontrado = False
        for info in libros.values():
            if info["genero"].lower() == genero.lower():
                print(f"Título: {info["titulo"]}")
                genero_encontrado = True
           
        if not genero_encontrado:
            print("No tenemos libros de ese género!")
    
    elif opcion == "3":
        contador = Counter(datos["genero"] for datos in libros.values())
        print(contador) #TODO --> Mostrar un mejor formato
    
    elif opcion == "4":
        bajo_stock = False
        for libro in libros.values():
            if libro["stock"] < 3:
                print(f"{libro["titulo"]} - {libro["stock"]}")
                bajo_stock = True
        
        if not bajo_stock:
            print("Todos los libros estan con buen stock! ")

    elif opcion == "5":
        codigo = input("Código: ")
        titulo = input("Título: ")
        autor = input("Autor: ")
        anio = int(input("Año: "))
        genero = input("Género: ")
        stock = int(input("Stock: "))

        libros[codigo] = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "stock": stock
         }
        print("Libro agregado!!")

    elif opcion == "6":
        codigo = input("Código del libro: ")
        if codigo in libros:
            nueva_cantidad = int(input("Indica la cantidad: "))
            libros[codigo]["stock"] = nueva_cantidad # Cual es la operación depende del escenario.
            print("Stock Actualizado")
        else:
            print("Código no encontrado")
    
    elif opcion == "7":
        codigo = input("Código del libro: ")
        if codigo in libros:
            libros.pop(codigo)
            print("Libro Eliminado")
        else:
            print("Código no encontrado")

    elif opcion == "8":
        print("Saliendo del sistema!!!")
        break
    else:
        print("Opción no valida")