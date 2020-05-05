print("Ordenar números")
print("=" * 80)

#datos
n1 = int(input("Ingrese número 1: "))
n2 = int(input("Ingrese número 2: "))
n3 = int(input("Ingrese número 3: "))
print("=" * 80)

#proceso
if n1 > n2 and n1 > n3:
    mayor = n1
    if n2 > n3:
        medio = n2
        menor = n3
    else:
        medio = n3
        menor = n2
elif n2 > n3:
    mayor = n2
    if n1 > n3:
        medio = n1
        menor = n3
    else:
        medio = n3
        menor = n1
else:
    mayor = n3
    if n1 > n2:
        medio = n1
        menor = n2
    else:
        medio = n2
        menor = n1

#Sobre el resto

if n3 == (n1 % n2):
    mensaje = "El tercer número es igual al resto de los dos primeros"
else:
    mensaje = "El tercer número no es igual al resto de los dos primeros"

#Resultados
print("Mayor:",mayor,"\nMedio:",medio,"\nMenor:",menor)
print(mensaje)
