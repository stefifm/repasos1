print("Institución Educativa")

#datos
id_grado1 = input("Ingrese el primer código de indentifación: ")
ninos1 = int(input("Cantidad de niños del grado1: "))
ninas1 = int(input("Cantidad de niñás del grado1: "))
print("=" * 40)
id_grado2 = input("Ingrese el segundo código de indentifación: ")
ninos2 = int(input("Cantidad de niños del grado2: "))
ninas2 = int(input("Cantidad de niñás del grado2: "))
print("=" * 40)
id_grado3 = input("Ingrese el tercer código de indentifación: ")
ninos3 = int(input("Cantidad de niños del grado3: "))
ninas3 = int(input("Cantidad de niñás del grado3: "))
print("=" * 40)
cupo = int(input("Cupo máximo (igual para los 3 cursos): "))
print("=" * 40)
#El que tenga menos alumnos inscritos
#primero....
grado1 = ninos1 + ninas1
grado2 = ninos2 + ninas2
grado3 = ninos3 + ninas3

#Determinar el menor

if grado1 < grado2 and grado1 < grado3:
    menor = grado1
    id = id_grado1
else:
    if grado2 < grado3:
        menor = grado2
        id = id_grado2
    else:
        menor = grado3
        id = id_grado3
#Porcentaje de niñas en cada curso
p_gninas1 = (ninas1 * 100) / grado1
p_gninas2 = (ninas2 * 100) / grado2
p_gninas3 = (ninas3 * 100) / grado3

#Porcentaje de niños en cada curso
p_gninos1 = (ninos1 * 100) / grado1
p_gninos2 = (ninos2 * 100) / grado2
p_gninos3 = (ninos3 * 100) / grado3

#Promedio General de alumnos
prom_gral = (grado1 + grado2 + grado3) / 3

#Algunos de los tres grados supera el cupo
flag = False
if grado1 > cupo or grado2 > cupo or grado3 > cupo:
    flag = True

#Resultados
print("El curso", id, "es el de menor cantidad de alumnos y tiene:",menor)
print("=" * 40)

print("Porcentaje de niñas del",id_grado1,":",p_gninas1)
print("Porcentaje de niñas del",id_grado2,":",p_gninas2)
print("Porcentaje de niñas del",id_grado3,":",p_gninas3)
print("=" * 40)
print("Porcentaje de niños del",id_grado1,":",p_gninos1)
print("Porcentaje de niños del",id_grado2,":",p_gninos2)
print("Porcentaje de niños del",id_grado3,":",p_gninos3)
print("=" * 40)
print("Promedio General de alumnos:",prom_gral)
print("=" * 40)
if flag == True:
    print("Apertura de nueva división porque algunos grados supera el cupo")
else:
    print("No se necesita de abrir otra división")

