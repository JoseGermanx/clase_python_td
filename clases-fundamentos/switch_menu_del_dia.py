
#Definición de una función principal
def menu_restaurante():
 try:
    print("----Menú del día-----")

    dia_input = int(input("Ingresa un número para el día de la semana: 1: Lun al 7: Dom -> "))

    menu_semana = {
     1: "Lentejas",
     2: "Tacos",
     3: "Fideos",
     4: "Carne",
     5: "Pizza",
     6: "Paella",
     7: "Cazuela"
    }

    plato_del_dia = menu_semana.get(dia_input, "Error")


    if "Error" in plato_del_dia:
        print("La opción no es válida!!")
    else:
        print(f"Hoy servimos: {plato_del_dia}")
        
 except ValueError:
    print("Debes ingresar una opción válida")

#Invocación de la función
menu_restaurante()