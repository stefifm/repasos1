# Desarrolle un programa completo en Python, sin usar funciones predefinidas
# min() y max(), que permita cargar por teclado 3 variables (3 valores enteros).
# Si el primer valor ingresado es igual a cero, calcule y muestre
# la siguiente fórmula: √ bᶟ + cᶟ .
# Si el primer valor ingresado es mayor a la suma del segundo y tercer valor,
# calcule y muestre el cociente entre b/c. Caso contrario, mostrar el mayor
# valor entre el segundo valor ingresado y el tercero.

print("Formulas con tres valores")
print("=" * 80)
#datos
n1 = int(input("Ingrese el primer valor: "))
n2 = int(input("Ingrese el segundo valor: "))
n3 = int(input("Ingrese el tercer valor: "))
print("=" * 80)

#proceso
if n1 == 0:
    formula = (n2 ** 3 + n3 ** 3) ** 0.5
    print("n1 es igual a cero y calcular √ n2ᶟ + n3ᶟ:",formula)
elif n1 > (n2 + n3):
    formula = n2 / n3
    print("n1 es mayor a la suma n2 + n3 y calcular el cociente entre n2 y "
          "n3:",formula)
else:
    if n2 > n3:
        mayor = n2
        menor = n3
        print("Mayor:",mayor,"\nMenor:",menor)
    else:
        mayor = n3
        menor = n2
        print("Mayor:",mayor,"\nMenor:",menor)