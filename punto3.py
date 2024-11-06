#Algoritmo para aumento del 15% del sueldo si es inferior a 300,000
Sueldo = int(input("Sueldo del trabajador: "))
if Sueldo <= 300000:
    Sueldo = Sueldo + (Sueldo * 0.15)
    print("AUMENTO ACEPTADO.")
    print("El nuevo sueldo del trabajador es", Sueldo)
else:
    print("AUMENTO DENEGADO.")

