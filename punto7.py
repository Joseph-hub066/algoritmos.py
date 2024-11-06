# Algoritmo que lea un registro
Nom = input("Escriba el nombre: ")
Edad = int(input("Digite su edad: "))
Sexo = input("Escriba su sexo (Hombre == M, Mujer == F): ").upper()
Est_Civil = input("Escriba su estado civil(casado/soltero): ").lower()

if (Sexo == "M" and Est_Civil == "casado" and Edad > 40):
    print("Nombre: ", Nom)
elif (Sexo == "F" and Est_Civil == "soltero" and Edad < 50):
    print("Nombre", Nom)
else: 
    print("La persona no cumple con los requisitos.")