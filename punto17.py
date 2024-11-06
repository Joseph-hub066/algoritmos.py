# Determinar un algoritmo que lea tres numeros y diga si uno es divisible del otro
N1 = int(input("Digite el primer numero: "))
N2 = int(input("Digite el segundo numero: "))
N3 = int(input("Digite el tercer numero: "))
if N1%N2 == 0:
    print(N1, "Es divisible entre", N2)
elif N1%N3 == 0:
    print(N1, "Es divisible entre", N3) 
elif  N2%N1 == 0:
    print(N2, "Es divisible entre", N1)
elif N2%N3 == 0:
    print(N2, "Es divisible entre", N3)
elif    N3%N1 == 0:
    print(N3, "Es divisible entre", N1)
elif    N3%N2 == 0:
    print(N3, "Es divisible", N2)    
else:
    print("No es divisible entre ningun numero dado")