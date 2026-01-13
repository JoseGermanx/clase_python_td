# Clasificación de edades
# Pide al usuario que ingrese su edad.
# Convierte la entrada a entero (int).
# Verifica que sea un número válido (mayor o igual a cero).
# Si la edad es de 0 a 12, imprime que es un niño o niña.
# Si está entre 13 y 17, indica que es adolescente.
# Si está entre 18 y 64, que es adulto.
# Si tiene 65 años o más, clasificalo como adulto mayor.
# Muestra el resultado final en pantalla.


edad = int(input("Ingrese su edad: "))

if edad < 0:
    print("Edad no válida!")
elif edad <= 12:
    print("Es niño o niña")
elif edad <= 17:
    print("Es adolescente!")
elif edad <= 64:
    print("Es un adulto")
else:
    print("Es adulto mayor!!")