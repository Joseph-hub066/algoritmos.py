# Desarrolle un algoritmo que determine si un numero es par o impar
N = int(input("Ingrese un numero: "))
res = N%2 
if res == N%2 == 0:
    print(N, "Es un numero par")
else:
    print(N, "Es un numero impar")