# ingrese 4 numeros enteros
# determine
# a) promedio entre mayor y menor
# b) porcentaje de números mayores a 10
# c) informe cuantos números son iguales a 50
# d) qué números son iguales a 50


# Datos
n1 = int(input("Ingrese número 1: "))
n2 = int(input("Ingrese número 2: "))
n3 = int(input("Ingrese número 3: "))
n4 = int(input("Ingrese número 4: "))

# Determinar mayor y menor
if n1 > n2 and n1 > n3 and n1 > n4:
    mayor = n1
else:
    if n2 > n3 and n2 > n4:
        mayor = n2
    else:
        if n3 > n4:
            mayor = n3
        else:
            mayor = n4

if n1 < n2 and n1 < n3 and n1 < n4:
    menor = n1
else:
    if n2 < n3 and n2 < n4:
        menor = n2
    else:
        if n3 < n4:
            menor = n3
        else:
            menor = n4

# Conocer el promedio entre mayor y menor
prom = (mayor + menor) / 2

# Porcentaje de números mayor a 10
cant10 = 0
if n1 > 10:
    cant10 += 1

if n2 > 10:
    cant10 += 1

if n3 > 10:
    cant10 += 1

if n4 > 10:
    cant10 += 1

porcentaje = (cant10 * 100) / 4

# Cantidad de números iguales a 50
igual50 = 0
if n1 == 50:
    igual50 += 1

if n2 == 50:
    igual50 += 1

if n3 == 50:
    igual50 += 1

if n4 == 50:
    igual50 += 1

# números iguales a 50
nigual50 = ""
if n1 == 50:
    nigual50 += "El primer número"
if n2 == 50:
    nigual50 += "El segundo número"
if n3 == 50:
    nigual50 += "El tercer número"
if n4 == 50:
    nigual50 += "El cuarto número"


# Resultados
print("Mayor es:",mayor)
print("Menor es:",menor)
print("Promedio mayor y menor:",prom)
print("Porcentaje de números mayores a 10:",porcentaje)
print("Cantidad de números iguales a 50:",igual50)
print("Números iguales a 50:",nigual50)