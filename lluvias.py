print("Lluvias")
print("=" * 80)

#datos
c_m1 = int(input("Cantidad de lluvias en el mes 1: "))
c_m2 = int(input("Cantidad de lluvias en el mes 2: "))
c_m3 = int(input("Cantidad de lluvias en el mes 3: "))
print("=" * 80)

#proceso
prom_lluvias = round((c_m1 + c_m2 + c_m3) / 3, 2)

superior = 0
if c_m1 >= prom_lluvias:
    superior += 1
if c_m2 >= prom_lluvias:
    superior += 1
if c_m3 >= prom_lluvias:
    superior += 1

#Menor
if c_m1 < c_m2 and c_m1 < c_m3:
    menor = c_m1
    mes = "Enero"
else:
    if c_m2 < c_m3:
        menor = c_m2
        mes = "Febrero"
    else:
        menor = c_m3
        mes = "Marzo"
flag = False
if menor == 0:
    flag = True
#Resultados
print("Promedio de milímiteros caídos:",prom_lluvias)
print("Cantidad de meses que superen o igualen el promedio:",superior)
print("Mes con menos lluvias:",mes,"y cantidad de mm caídos:",menor)
if flag == True:
    print("El mes de",mes,"tuvo 0 mm caídos")
else:
    print("El mes de",mes,"no tuvo 0 mm caídos")
