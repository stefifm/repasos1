#Se tienen los datos de tres postulantes a un empleo a los que se les realizó
# un test de capacitación. Por cada postulante se tiene la siguiente información:
# nombre del postulante, cantidad total de preguntas que se le realizaron y
# cantidad de preguntas que contestó correctamente.

#Se pide confeccionar un programa que lea los datos de los tres postulantes,
# informe el nivel de cada uno según los criterios de aprobación que se indican
# mas abajo, e indique finalmente el nombre del postulante que ganó el puesto.
# Los criterios de aprobación son los siguientes, en función del porcentaje de
# respuestas correctas sobre el total de preguntas realizadas a cada postulante:
#     Nivel Superior:       Porcentaje >= 90%
#    Nivel Medio:          75% <= Porcentaje < 90%
#     Nivel Regular:        50% <= Porcentaje < 75%
#     Fuera de Nivel:       Porcentaje < 50%

print("Postulantes a un empleo")
print("=" * 80)
#Datos
nom1 = input("Nombre del postulante 1: ")
pre_total1 = int(input("Cantidad de preguntas realizadas al postulante 1: "))
pre_cor1 = int(input("Preguntas correctas que respondió el postulante 1: "))

nom2 = input("Nombre del postulante 2: ")
pre_total2 = int(input("Cantidad de preguntas realizadas al postulante 2: "))
pre_cor2 = int(input("Preguntas correctas que respondió el postulante 2: "))

nom3 = input("Nombre del postulante 3: ")
pre_total3 = int(input("Cantidad de preguntas realizadas al postulante 3: "))
pre_cor3 = int(input("Preguntas correctas que respondió el postulante 3: "))
print("=" * 80)

#Proceso...
por1 = round((pre_cor1 * 100) / pre_total1, 2)
por2 = round((pre_cor2 * 100) / pre_total2, 2)
por3 = round((pre_cor3 * 100) / pre_total3, 2)
#Para saber el nivel de cada postulante
if por1 >= 90:
    nivel1 = "Superior"
elif 75 <= por1 < 90:
    nivel1 = "Medio"
elif 50 <= por1 < 75:
    nivel1 = "Regular"
else:
    nivel1 = "Fuera de nivel"

if por2 >= 90:
    nivel2 = "Superior"
elif 75 <= por2 < 90:
    nivel2 = "Medio"
elif 50 <= por2 < 75:
    nivel2 = "Regular"
else:
    nivel2 = "Fuera de nivel"

if por3 >= 90:
    nivel3 = "Superior"
elif 75 <= por3 < 90:
    nivel3 = "Medio"
elif 50 <= por3 < 75:
    nivel3 = "Regular"
else:
    nivel3 = "Fuera de nivel"

#Para saber quién se cada con el puesto
if por1 > por2 and por1 > por3:
    mayor = nivel1
    postulante = nom1
else:
    if por2 > por3:
        mayor = nivel2
        postulante = nom2
    else:
        mayor = por3
        postulante = nivel3

#Resultados
print("Nivel de",nom1,":",nivel1)
print("Nivel de",nom2,":",nivel2)
print("Nivel de",nom3,":",nivel3)

print("El postulante",postulante,"se queda con el puesto por tener un "
                                 "nivel",mayor)