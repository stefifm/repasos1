print("Venta de artículos")
print("=" * 80)

#datos
art1 = input("Nombre del artículo 1: ")
cant_art1 = int(input("Cantidades vendidas del artículo 1: "))
precio_uni1 = float(input("Precio unitario del artículo 1: "))

art2 = input("\nNombre del artículo 2: ")
cant_art2 = int(input("Cantidades vendidas del artículo 2: "))
precio_uni2 = float(input("Precio unitario del artículo 2: "))

art3 = input("\nNombre del artículo 3: ")
cant_art3 = int(input("Cantidades vendidas del artículo 3: "))
precio_uni3 = float(input("Precio unitario del artículo 3: "))
print("=" * 80)

#proceso
ing1 = cant_art1 * precio_uni1
ing2 = cant_art2 * precio_uni2
ing3 = cant_art3 * precio_uni3
ing_absoluto = ing1 + ing2 + ing3

if ing1 > ing2 and ing1 > ing3:
    may_ing = ing1
    may_nom = art1
else:
    if ing2 > ing3:
        may_ing = ing2
        may_nom = art2
    else:
        may_ing = ing3
        may_nom = art3

porcentaje = round((may_ing * 100) / ing_absoluto, 2)

#Resultados
print("El artículo de mayor aporte:",may_nom, "e hizo un aporte de:",may_ing)
print("Porcentaje del mayor aporte respecto al total:",porcentaje)
