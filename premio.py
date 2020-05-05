print("Premio por ventas")
print("=" * 80)

#Datos
monto1 = float(input("Ingrese monto 1: "))
monto2 = float(input("Ingrese monto 2: "))
monto3 = float(input("Ingrese monto 3: "))
print("=" * 80)

#proceso...
if monto1 < monto2 and monto1 < monto3:
    menor = monto1
else:
    if monto2 < monto3:
        menor = monto2
    else:
        menor = monto3
premio = round((menor * 50) / 100, 2)

flag = False
if monto1 > 1000 and monto2 > 1000 and monto3 > 1000:
    adicional = round((premio * 10) / 100, 2)
    premio += adicional
    flag = True

if flag == True:
    mensaje = "Si incluye adicional"
else:
    mensaje = "No incluye adicional"

#resultados
print("Premio de un vendedor:",premio)
print("¿Hay adicional?",mensaje)