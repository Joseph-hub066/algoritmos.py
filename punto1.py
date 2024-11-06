#Algoritmo de un numero que en caso de ser negativo lo imprima con su positivo.
num = int(input("Digite el numero: "))
if num < 0:
    num = num * -1
    print("El positivo es:", num)
else: 
    print("El numero positivo es", num)