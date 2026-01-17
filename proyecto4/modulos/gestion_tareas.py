
tareas = []


def agregar_tarea(tarea):
    tarea = {
        "tarea": tarea,
        "completada": False
    }
    tareas.append(tarea)


def listar_tareas():
    print("--Estas son tus tareas--")
    print("------------------------")
    for indice, tarea in enumerate(tareas, start=1):
        print(f"{indice}. {tarea["tarea"]}  {tarea["completada"]}  ")

# 0 1 2 3 
def marcar_completada(indice):
    tareas[indice]["completada"] = True


def eliminar_tarea(indice):
    tareas.pop(indice)
