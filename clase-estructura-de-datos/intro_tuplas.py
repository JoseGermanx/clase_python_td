# Crear una tupla con las coordenadas de una ciudad
# Mostrar las coordenadas por pantalla
# Acceder al valor de latitud y longitud por índice
# Intentar modificar la tupla (y provocar un error)
# Reemplazar la tupla completa si es necesario (no un solo valor)
# Usar tuplas dentro de una lista para múltiples registros
# Iterar sobre la lista de tuplas y mostrar cada ciudad
# Imprimir mensajes como: "La ciudad está ubicada en (lat, long)"

ciudad = ("Santiago", -33.4489, -70.6693)
#             0           1        2
print(ciudad)
comuna = ciudad[0]
latitud = ciudad[1]
longitud = ciudad[2]

print(f"La ubicación de {comuna} es Latitud: {latitud} - Longitud: {longitud}")

# ciudad[1] = 34.0 TypeError: 'tuple' object does not support item assignment

ciudad = ("Santiago", -34.00, -70.6693)

print(ciudad)

ciudades = [("Santiago", -34.00, -70.6693), ("Lima", -14.00, -77.6693), ("Buenos Aires", -40.00, 58.6693)]

for nombre, lat, long in ciudades:
    print(f"La ciudad {nombre} está ubicada en ({lat}, {long})")