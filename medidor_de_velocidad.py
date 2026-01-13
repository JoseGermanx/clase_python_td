# ¿En qué consistirá la Demo?
# Aplicar un condicional simple (if) para detectar si un vehículo supera el límite de velocidad permitido.
# Vamos a imaginar que estamos diseñando un sistema que detecta si un conductor excede la velocidad máxima permitida en una zona. Si supera los 60 km/h, el sistema debe advertirlo
# Lo primero que haremos es pedirle al usuario que ingrese su velocidad actual. Como es un número con decimales, lo convertiremos a float.
# Luego usaremos una estructura if para verificar si la velocidad ingresada es mayor a 60. Si lo es, mostraremos un mensaje de advertencia.

velocidad_actual = float(input("Ingrese su velocidad actual: "))

if velocidad_actual > 60:
    print("Vas muy rápido, baja la velocidad!!")