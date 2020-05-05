print("Estudiantes")
print("=" * 80)

materia1 = int(input("Número de materias del E1: "))
materia2 = int(input("Número de materias del E2: "))
materia3 = int(input("Número de materias del E3: "))
plan = int(input("Cantidad total de materias del plan: "))
print("=" * 80)
if materia1 > materia2 and materia1 > materia3:
    mayor = materia1
    emayor = "Estudiante 1"
else:
    if materia2 > materia3:
        mayor = materia2
        emayor = "Estudiante 2"
    else:
        mayor = materia3
        emayor = "Estudiante 3"
#Medio
if materia2 > materia1 > materia3 or materia3 > materia1 > materia2:
    medio = materia1
    emedio = "Estudiante 1"
else:
    if materia1 > materia2 > materia3 or materia3 > materia2 > materia1:
        medio = materia2
        emedio = "Estudiante 2"
    else:
        medio = materia3
        emedio = "Estudiante 3"

#Menor
if materia1 < materia2 and materia1 < materia3:
    menor = materia1
    emenor = "Estudiante 1"
else:
    if materia2 < materia3:
        menor = materia2
        emenor = "Estudiante 2"
    else:
        menor = materia3
        emenor = "Estudiante 3"

diferencia = mayor - menor

if diferencia > menor + 10:
    mensaje1 = "Los estudiantes avanzan de forma despareja"
else:
    mensaje1 = "Los estudiantes van parejos"
#promedio
promedio = round((materia1 + materia2 + materia3) / 3, 2)
if materia1 >= promedio:
    print("Estudiante 1 tiene más materias que el promedio o igual")

if materia2 >= promedio:
    print("Estudiante 2 tiene más materias que el promedio o igual")

if materia3 >= promedio:
    print("Estudiante 3 tiene más materias que el promedio o igual")
print("=" * 80)
#porcentaje del plan

porcentaje1 = round((materia1 * 100) / plan, 2)
porcentaje2 = round((materia2 * 100) / plan, 2)
porcentaje3 = round((materia3 * 100) / plan, 2)

#Cantidad que falta para cursar
cf1 = plan - materia1
cf2 = plan - materia2
cf3 = plan - materia3

#Porcentaje faltante
pf1 = round((cf1 * 100) / plan, 2)
pf2 = round((cf2 * 100) / plan, 2)
pf3 = round((cf3 * 100) / plan, 2)

#Mostrar resultados
print("Mayor cantidad de materias:",mayor,"Y corresponde:",emayor)
print("El medio es:",medio,"y corresponde:",emedio)
print("Menor cantidad de materias:",menor,"Y corresponde:",emenor)
print("Promedio de materia:",promedio)
print("La diferencia es:",diferencia)
print("=" * 80)
print("Porcentaje de aprobadas del 1:",porcentaje1)
print("Porcentaje de aprobadas del 2:",porcentaje2)
print("Porcentaje de aprobadas del 3:",porcentaje3)
print("=" * 80)
print("Cantidad que le falta al 1:",cf1)
print("Cantidad que le falta al 2:",cf2)
print("Cantidad que le falta al 3:",cf3)
print("=" * 80)
print("Porcentaje que le falta al 1:",pf1)
print("Porcentaje que le falta al 2:",pf2)
print("Porcentaje que le falta al 3:",pf3)
print("=" * 80)
print("¿Avance?:",mensaje1)
