# Desarrolle un programa completo en Python, sin usar las funciones
# predefinidas
# min() y max(), que permita cargar por teclado dos números.
# Determine y muestre el mayor, el cuadrado del mayor y el cubo del mayor.

a = int(input("Cargue el primer número: "))
b = int(input("Cargue el segundo número: "))

if a > b:
    mayor = a
else:
    mayor = b

cuadrado = mayor ** 2
cubo = mayor ** 3

print("El mayor es:",mayor)
print("El cuadrado del mayor es:",cuadrado,"\nY el cubo del mayor es:",cubo)