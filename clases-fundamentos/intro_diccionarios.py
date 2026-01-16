#Diccionarios

dias = {
  1: "Lunes",
  2: "Martes",
  3: "Miércoles",
  4: "Jueves",
  5: "Viernes",
  6: "Sábado",
  7: "Domingo"
}

dia_input = int(input("Ingresa un número para el día de la semana: 1: Lun al 7: Dom -> "))

#método para obtener el valor de una clave.
resultado = dias.get(dia_input, "No encontrado")

print(F"{resultado}")
