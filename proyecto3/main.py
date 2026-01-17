# Pedir al usuario que ingrese una temperatura en grados Celsius.
# Validar que la entrada sea un número.
# Clasificar la temperatura usando condiciones múltiples (if, elif, else) en categorías como:
# Muy frío: t < 5
# Frío: 5 ≤ t < 15
# Agradable: 15 ≤ t < 25
# Caluroso: 25 ≤ t < 35
# Extremo: t ≥ 35
# Gestionar errores si el usuario ingresa un valor no numérico.
# Separar la lógica en módulos de validación.
from modulos.validaciones import leer_float, clasificar_temperaturas

temp_input = leer_float("Ingresa la temperatura en C: ")

temperatura = clasificar_temperaturas(temp_input)

print(f"Es estado actual de cliente es: {temperatura}")