# En qué consistirá la Demo?
# Tenemos un sistema de reservas de un cine. Dependiendo del tipo de usuario (cliente regular, estudiante, jubilado, etc.), el sistema debe aplicar un descuento diferente en la compra del boleto. Si el tipo de usuario no está en la lista, el precio se mantiene normal.

# ¿Cuántas condiciones debemos evaluar en este problema?
# Tipo de usuario es quien marca la pauta para las condiciones
tipo_usuario = "regular"

valor_ticket = 100

def calculo_descuento(tipo_de_usuario):
    pass


# ¿Qué estructura condicional nos ayudaría a organizarlo mejor?

#if elif
if tipo_usuario == "regular":
    valor_ticket = 10
elif tipo_usuario == "estudiante":
    valor_ticket = 5

#switch


# ¿Cómo evitar repetir código innecesario?
# Revisar el códido y encontrar patrones que se repiten.

# ¿Qué pasaría si el usuario ingresa un tipo no reconocido?
