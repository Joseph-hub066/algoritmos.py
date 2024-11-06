# Organizar de mayor a menor con 3 numeros enteros unicos
num1 = int(input("Digite un numero: "))
num2= int(input("Digite un numero: "))
num3 = int(input("Digite un numero: "))

if num1 > num2 > num3:
    orden = (num1, num2, num3)
elif num1 > num3 > num2:
    orden = (num1, num3, num2)
elif num2 > num1 > num3:
    orden = (num2, num1, num3)
elif num2 > num3 > num1:
    orden = (num2, num3, num1)
elif num3 > num1 > num2:
    orden = (num3, num1, num2)
else: 
    orden = (num3, num2, num1)

print("Numero ordenados de mayor a menor", orden)