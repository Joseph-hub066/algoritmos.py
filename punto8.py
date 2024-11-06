#capturar el numero medio
9
num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))
num3 = int(input("Digite el tercer numero: "))

if (num1 > num2 and num1 < num3) or (num1 < num3 and num1 > num3):
    medio = num1
elif (num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3):
    medio = num2
else: 
    medio = num3
print("El numero medio es", medio)

