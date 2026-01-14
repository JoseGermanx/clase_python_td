# ¿En qué consistirá la Demo?
# Crear un asistente bancario que reciba una opción numérica del usuario y devuelva información útil según el área seleccionada. El sistema debe permitir:
# Elegir entre opciones del 1 al 5
# Mostrar la respuesta según el área elegida
# Mostrar un mensaje de advertencia si el número no es válido
# 🔢 Opciones disponibles:
# Consultar saldo
# Transferencias
# Pago de servicios
# Préstamos y créditos
# Atención al cliente


#definir la función principal

def asistente_bancario():
    print("----Bienvenido a tu Banco-----")
    print("1. Consultar Saldo")
    print("2. Transferencias")
    print("3. Pago de servicios")
    print("4. Préstamos y créditos")
    print("5. Atención al cliente")

    opcion = int(input("Por favor, el ige una opción (1-5):"))

    #Mapeo de las opciones
    acciones_bancarias = {
        1: "Gerando el reporte...",
        2: "Iniciando transferencia",
        3: "Indica que servicio que quieres pagar",
        4: "Calculando para ti un opción de crédito",
        5: "Conectando con un ejecutivo"
    }

    #Lógica para validar la opción ingresada por el usuario
    resultado = acciones_bancarias.get(opcion, "Error: opción no válida!!")

    print(f"Respuesta del sistema: {resultado}")




#Invocar la función principal
asistente_bancario()