# Contexto: 🙌
# Una agencia de diseño gráfico está integrando productos de dos catálogos distintos. Necesitan identificar los colores que se repiten, los únicos de cada catálogo y todos los colores disponibles sin duplicados. Además, desean poder agregar y quitar colores según decisiones del equipo creativo.

# Consigna: ✍️
# Construir un programa que:
# Compare dos listas de colores y elimine duplicados.
# Informe qué colores están en ambos catálogos.
# Determine qué colores son exclusivos de cada uno.
# Permita agregar un nuevo color al catálogo A y eliminar uno del catálogo B.
# Presente todos los resultados de manera clara.

# Paso a paso: ⚙️
# Crear dos listas: catalogo_a = [...] y catalogo_b = [...] con al menos 6 colores cada una (incluyendo duplicados).

# Convertir ambas listas a sets: set_a y set_b.

# Mostrar los siguientes resultados:

# Unión: todos los colores disponibles sin duplicados.
# Intersección: colores que están en ambos catálogos.
# Diferencia A - B: colores únicos del catálogo A.
# Diferencia B - A: colores únicos del catálogo B.

# Agregar un nuevo color al set_a (usando add()).

# Eliminar un color específico del set_b (usando discard()).

# Mostrar los sets actualizados con mensajes claros.

catalogo_a = ["rojo", "azul", "verde", "negro", "blanco", "azul"]
catalogo_b = ["amarillo", "verde", "negro", "gris", "blanco", "verde"]

set_a = set(catalogo_a)
set_b = set(catalogo_b)

print("Todos los colores disponibles: ", set_a | set_b) #Unión sin duplicados

print("Colores que están en ambos catálogos: ", set_a & set_b) 

print("Colores únicos en el catálogo A: ", set_a - set_b)
print("Colores únicos en el catálogo B: ", set_b - set_a)

set_a. add("Violeta")

set_b.discard("amarillo")

print("Catálogo A, actualizado: ", set_a)
print("Catálogo B, actualizado: ", set_b)


