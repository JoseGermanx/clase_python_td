# Simularemos dos listas de usuarios de diferentes plataformas y usaremos sets para encontrar coincidencias, diferencias y valores únicos.


# Crear dos listas de usuarios con posibles repetidos
plataforma_a = ["ana", "juan", "maria", "ana", "pedro"]

plataforma_b = ["lucas", "maria", "juan", "juan", "sofia"]

# Convertir las listas en conjuntos para eliminar duplicados
set_a = set(plataforma_a)
set_b = set(plataforma_b)

# Mostrar los usuarios únicos de cada plataforma
print("Set Plataforma a:", set_a)
print("Set Plataforma b:", set_b)

# Calcular la intersección (usuarios en ambas plataformas)
print("Usuarios en ambas Plataformas:", set_a & set_b)

# Calcular la unión (todos los usuarios sin duplicados)
print("Usuarios en ambas Plataformas:", set_a | set_b)

# Calcular diferencia (usuarios solo en una plataforma)
print("Solo usuarios en A:", set_a - set_b) # Resultado sólo los que están en A
print("Solo usuarios en B:", set_b - set_a) # Resultado sólo los que están en B

# Usar add() y remove() para modificar un set
set_a.add("carlos")
set_b.remove("lucas")

print("Usuarios en ambas Plataformas:", set_a | set_b)

# Recorrer un set con for e imprimir los resultados

todos_los_usuarios = set_a | set_b


for usuario in todos_los_usuarios:
    print(usuario)
