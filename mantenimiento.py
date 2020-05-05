print("Mantenimiento de PC")

#Datos
n_id1 = int(input("PC 1: "))
man1 = int(input("Tiempo de mantenimiento de la PC 1 (en minutos): "))
cau1 = int (input("Causa de la PC1 (1- Problema de Hardware 2- Problema de "
                  "Software): "))

n_id2 = int(input("PC 2: "))
man2 = int(input("Tiempo de mantenimiento de la PC 2 (en minutos): "))
cau2 = int (input("Causa de la PC2 (1- Problema de Hardware 2- Problema de "
                  "Software): "))

n_id3 = int(input("PC 3: "))
man3 = int(input("Tiempo de mantenimiento de la PC 3 (en minutos): "))
cau3 = int (input("Causa de la PC3 (1- Problema de Hardware 2- Problema de "
                  "Software): "))

#tiempo total de mantenimientp
t_total = man1 + man2 + man3

#PC con mayor tiempo de mantenimiento

if man1 > man2 and man1 > man3:
    may_tiempo = man1
    id = n_id1
else:
    if man2 > man3:
        may_tiempo = man2
        id = n_id2
    else:
        may_tiempo = man3
        id = n_id3

#Promedio de mantenimiento

t_prom = (man1 + man2 + man3) / 3

#Causa de mantenimiento

flag = False
if cau1 == 1 and cau2 == 1 and cau3 == 1:
    flag = True

#Resultados
print("Tiempo total de los mantenimientos:",t_total)
print("Mayor tiempo de mantenimiento:",may_tiempo,"y corresponde a la PC:",id)
print("Tiempo promedio de los mantenimientos:",t_prom)
if flag == True:
    print("Todas las PC tuvieron Problemas de Hardware")
else:
    print("No todas las PC tuvieron Problemas de Hardware")