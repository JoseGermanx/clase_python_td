

# Funciones de conversión y tipo

edad_en_texto = "25"
edad = int(edad_en_texto)

precio_en_texto = "199.99"
precio = float(precio_en_texto)

numero = 10
numero_en_texto = str(numero)



print(f"1. {edad}")
print(f"2. {precio}")
print(f"3. {numero_en_texto}")

#Verificar tipos

x = 10
y = "Python"

print(type(x))
print(type(y))

print(isinstance(x, str))
print(isinstance(y, str))

#Trabajos con listas

texto = "Python"
numeros = [1,2,3,4,5]

print(len(texto))
print(len(numeros))

cadena = "Hola"
lista_caracteres = list(cadena)

print(lista_caracteres)

tupla = tuple([1,2,3])
dicccionario = dict(nombre="ana", edad=30)

print(tupla)
print(dicccionario)

for num in range(1,6):
    print(num)

num_4 = 3.4
print(round(num_4))

pi = 3.143172
print(round(pi, 4))