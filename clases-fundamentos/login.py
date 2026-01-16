
# Simulación login de usuario

#Datos previamente guardados
usuario_guardado = "usuario"
contrasena_guardada = "1234"


# capturar datos del usuario
usuario_ingresado = input("Ingresa tu nombre de usuario: ")
contrasena_ingresada = input("Ingresa tu contraseña: ")

#Comparación de datos

if usuario_guardado == usuario_ingresado and contrasena_guardada == contrasena_ingresada:
    print("Usuario logueado de manera correcta.")
else:
    print("Datos erroneos!")
