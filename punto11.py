long = float(input("Longitud de la varilla: "))
diam = float(input("Diametro de la varilla: "))
dense = 3.5
masa = (diam * long)/dense


if long < 7.5 or long > 9:
    print("La longitud no es aceptable.")
elif diam < 0.5 or diam > 1.3:
    print("EL diametro no es aceptable.")
elif masa > 5.8:
    print("La masa no es aceptable.")
else:
    print("La empresa ha aceptado tu trabajo.")





