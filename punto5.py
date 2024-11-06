#3 numeros de mayor a menor
num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))
num3 = int(input("Digite el tercer numero: "))

mayor = max(num1, num2, num3)
menor = min(num1, num2, num3)

if num1 == num2 == num3:
    print("Los tres numeros son iguales.")
elif num1 == num2 or num1 == num2 or num2 == num3:
    print("Hay dos numeros iguales")
else:
    print("Los tres numeros son diferentes.")
print("El numero mayor es", mayor)
print("El numero menor es", menor)