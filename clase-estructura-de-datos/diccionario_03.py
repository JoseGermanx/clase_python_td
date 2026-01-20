
from collections import defaultdict, Counter

visitas = defaultdict(int)


usuarios = ["ana", "juan", "ana", "pedro", "juan", "ana"]

for usuario in usuarios:
    visitas[usuario] += 1

# print("Visitas usuarios")
# for usuario, cantidad in visitas.items():
#     print(f"{usuario}: {cantidad}")



colores = ["rojo", "azul", "verde", "rojo", "verde", "naranja"]

contador_de_colores = Counter(colores)

for color, cantidad in contador_de_colores.items():
    print(f"{color}: {cantidad}")
