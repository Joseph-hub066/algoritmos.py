# Dos notas mas altas
nota1 = float(input("Introduce la primera calificación: "))
nota2 = float(input("Introduce la segunda calificación: "))
nota3 = float(input("Introduce la tercera calificación: "))

if nota1 <= nota2 and nota1 <= nota3:
    prom = (nota2 + nota3)/2
elif nota2 <= nota1 and nota2 <= nota3:
    prom = (nota1 + nota3)/2
else: 
    prom = (nota1 + nota2)
print("Tu calificacion teniendo en cuenta las dos notas mas altas es", prom)