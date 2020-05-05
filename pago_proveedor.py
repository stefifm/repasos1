#Un comercio necesita informar el importe final a pagar a un determinado
# proveedor.
# Para ello debe ingresar la categoría (que puede ser categoría 'A' o 'B') y
# el importe original a abonar.

#Considerar las siguientes condiciones para el cálculo del importe final a
# pagar:

#Si el cliente es categoría A y el monto a pagar supera a los 1000 pesos
# debe aplicarse un descuento del 5%.
#Si el cliente es categoría B y el importe a pagar oscila entre 1500 y 2500
# pesos debe aplicarse un descuento del 2%.
#Para ambas categorías en caso de no cumplirse las condiciones especificadas
# no se aplicará ningún tipo de descuento sobre el importe que se le debe abonar.

print("Importe a pagar")
print("=" * 80)

cat = int(input("Categoría del cliente (1-A, 2-B): "))
imp_ori = float(input("Importe original: "))
print("=" * 80)

#proceso...
if cat == 1 and imp_ori > 1000:
    descuento = round((imp_ori * 5) / 100, 2)
    imp_pagar = imp_ori - descuento
elif cat == 2 and 1500 < imp_ori < 2500:
    descuento = round((imp_ori * 2) / 100, 2)
    imp_pagar = imp_ori - descuento
else:
    descuento = 0
    imp_pagar = imp_ori

#resultado...
print("Importe final a pagar:",imp_pagar)