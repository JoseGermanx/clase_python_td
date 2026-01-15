# Simular un cajero automático que solicite un PIN al usuario.
# Permitir hasta 3 intentos antes de bloquear el acceso.
# Configurar variables iniciales
# Almacenar un PIN correcto (ejemplo: pin_correcto = "1234").
# Usar un ciclo while para validar intentos
# Permitir al usuario ingresar el PIN.
# Reducir el número de intentos después de cada intento fallido.
# Bloquear el acceso tras 3 intentos incorrectos.
# Usar break para finalizar el ciclo
# Si el usuario ingresa el PIN correcto, terminar el ciclo.
# Mostrar un mensaje de bienvenida si el PIN es correcto.
# Ejecutar y Validar.

pin_correcto = "1234"

intentos = 3  #  ---> 0

while intentos > 0:
    pin = input("Ingresa tu PIN: ")

    if pin == pin_correcto:
        print("Bienvenido!!")
        break
    else:
        intentos -= 1
        if intentos == 0:
            print("Acceso bloquedo. Demasiados intentos fallidos!!! ")
        else:
            print(f"PIN Incorrecto. Tienes {intentos} intentos.")
