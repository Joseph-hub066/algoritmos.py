#Hallar la nota total de una materia en el SENA y determinar si ganó o perdió

N1 = float(input("Digite la primera nota: "))
N2 = float(input("Digite la segunda nota: "))
N3 = float(input("Digite la tercera nota: "))
NT = N1 + N2 + N3
print("La nota total es", NT)
if NT > 60:
    print("Ganó la materia.")
else: 
    print("Perdió la materia.")