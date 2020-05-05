print("Elecciones presidenciales")
print("=" * 80)

#Datos
for1 = input("Formula presidencial 1: ")
c1 = int(input("Cantidad de votos de la formula 1: "))
for2 = input("Formula presidencial 2: ")
c2 = int(input("Cantidad de votos de la formula 2: "))
for3 = input("Formula presidencial 3: ")
c3 = int(input("Cantidad de votos de la formula 3: "))
print("=" * 80)

#Proceso...
total_votos = c1 + c2 + c3
pf1 = round((c1 * 100) / total_votos, 2)
pf2 = round((c2 * 100) / total_votos, 2)
pf3 = round((c3 * 100) / total_votos, 2)

if pf1 > pf2 and pf1 > pf3:
    primero = pf1
    f1 = for1
    if pf2 > pf3:
        segundo = pf2
        f2 = for2
        tercero = pf3
        f3 = for3
    else:
        segundo = pf3
        f2 = for3
        tercero = pf2
        f3 = for2
elif pf2 > pf3:
    primero = pf2
    f1 = for2
    if pf1 > pf3:
        segundo = pf1
        f2 = for1
        tercero = pf3
        f3 = for3
    else:
        segundo = pf3
        f2 = for3
        tercero = pf1
        f3 = for1
else:
    primero = pf3
    f1 = for3
    if pf1 > pf2:
        segundo = pf1
        f2 = for1
        tercero = pf2
        f3 = for2
    else:
        segundo = pf2
        f2 = for2
        tercero = pf1
        f3 = for1
diferencia = primero - segundo
flag = False
if primero >= 45 or primero >= 40 and diferencia > 10:
    flag = True

#Resultados
print("Formula ganadora:",f1,"porcentaje:",primero)
if flag == True:
    print("La formula",f1,"ganó las elecciones y no habrá segunda vuelta")
else:
    print("Habrá segunda vuelta entre:",f1,"y",f2)





