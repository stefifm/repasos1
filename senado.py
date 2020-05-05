print("Votación en el senado")

print("=" * 80)

#Datos
favor = int(input("Votos a favor: "))
contra = int(input("Votos en contra: "))
abstenciones = int(input("Abstenciones: "))
total_votos = favor + contra + abstenciones

print("=" * 80)

#Resultado de la votación

if favor > contra and favor > abstenciones:
    ley = "La ley fue aprobada"
    p_favor = (favor * 100) / total_votos
    if p_favor > 50:
        ley = "Mayoria absoluta"
    else:
        ley = "Mayoria simple"
elif contra > abstenciones:
    ley = "La ley no fue aprobada"
else:
    ley = "La ley deberá volver a Diputados"

#Determinar ausentes
senadores = 72
ausentes = senadores - total_votos

#Resultados
print("Resultado de la votación:",ley)
print("Cantidad de ausentes:",ausentes)





