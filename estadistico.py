print("Análisis estadístico")
print("=" * 60)

#datos

v1 = int(input("Ingrese valor 1: "))
v2 = int(input("Ingrese valor 2: "))
v3 = int(input("Ingrese valor 3: "))
print("=" * 60)
#proceso...

#valores múltiplos de 5

if v1 % 5 == 0 or v2 % 5 == 0 or v3 % 5 == 0:
    multiplo = "Algunos valores son múltiplos de 5"
else:
    multiplo = "No son múltiplos de 5"

#valores impares

impar = 0
if v1 % 2 != 0:
    impar += 1

if v2 % 2 != 0:
    impar += 1

if v3 % 2 != 0:
    impar += 1

#Mayor supera la suma de dos valores

if v1 > v2 and v1 > v3:
    mayor = v1
    suma = v2 + v3
else:
    if v2 > v3:
        mayor = v2
        suma = v1 + v3
    else:
        mayor = v3
        suma = v1 + v2

if mayor > suma:
    resultado = "Lo Supera"
else:
    resultado = "No lo supera"

#resultados
print(multiplo)
print("Cantidad de valores impares:",impar)
print("Mayor supera a la suma de dos valores:",resultado)