# Desarrolle un programa completo en Python, sin usar funciones predefinidas
# min() y max(), que permita cargar por teclado 3 valores (3 números reales).
# Si el primer valor ingresado es Par, determinar y mostrar el mayor y menor
# entre el segundo y tercer valor ingresado. Caso contrario, determinar y
# mostrar el mayor y menor entre el primer y segundo valor ingresado. Además,
# calcular y mostrar el promedio entre el mayor y el menor

print("Valores reales")
print("=" * 80)

#Datos
n1 = int(input("Ingrese el número 1: "))
n2 = int(input("Ingrese el número 2: "))
n3 = int(input("Ingrese el número 3: "))
print("=" * 80)
#proceso...
if n1 % 2 == 0:
    if n2 > n3:
        mayor = n2
        menor = n3
    else:
        mayor = n3
        menor = n2
else:
    if n1 > n2:
        mayor = n1
        menor = n2
    else:
        mayor = n2
        menor = n1

promedio = round((mayor + menor) / 2, 2)

#resultado
print("Mayor:",mayor,"\nMenor:",menor)
print("Promedio entre mayor y menor",promedio)
