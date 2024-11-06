# Algoritmo que compare dos números y diga cual es el número mayor
Num1 = int(input("Digita el primer numero a comparar: "))
Num2 = int(input("Digita el segundo numero a comparar: "))

if Num1 > Num2: # Los ":" significa "entonces"
    print("El numero mayor es", Num1)
else:
    print("El numero mayor es", Num2)