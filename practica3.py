#Desarrolle un programa completo en Python, sin usar funciones predefinidas
#min() y max(), que permita cargar por teclado un número que representa un día
#de la semana (un valor entero). Muestre por pantalla el día de la semana al
# que
#corresponde (por ejemplo: 1-Domingo, 2-Lunes, etc). En el caso de no ser un
#valor entre 1 a 7, mostrar un mensaje de “Error”.
#Si el valor ingresado corresponde al día Sábado o Domingo, mostrar por
# pantalla el mensaje: “Fin de semana”

print("Día de las semanas")
print("=" * 80)
dia = int(input("Cargue un día de la semana ("
                "\n 1-Domingo\n 2-Lunes\n 3-Martes\n "
                "4-Miércoles\n 5-Jueves"
                "\n 6-Viernes\n 7-Sábado"
                ": "))
print("=" * 80)


flag = False
dia_semana = 0
if 0 < dia < 8:
    if dia == 1:
        dia_semana = "Domingo"
        flag = True
    elif dia == 2:
        dia_semana = "Lunes"
    elif dia == 3:
        dia_semana = "Martes"
    elif dia == 4:
        dia_semana = "Miércoles"
    elif dia == 5:
        dia_semana = "Jueves"
    elif dia == 6:
        dia_semana = "Viernes"
    elif dia == 7:
        dia_semana = "Sábado"
        flag = True
    if flag == True:
        print("Es un fin de semana")
    else:
        print("Es un día de semana")
    print("Día de la semana:",dia_semana)
else:
    print("Error")

