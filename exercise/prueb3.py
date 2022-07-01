'''
n1 = int(input("Ingresa la primera nota: "))
n2 = int(input("Ingresa la segunda nota: "))
n3 = int(input("Ingresa la tercera nota: "))

promedio = (n1 + n2 + n3) / 3

if promedio >= 6:
    print (f"Esta aprobado con {promedio}")
else:
    print(f"No esta aprobado con {promedio}")
'''

cant_alumns = int(input("Ingresa la cantidad de alumnos: "))

for i in range(cant_alumns):
    promedio = 0
    n1 = int(input("Ingresa la primera nota: "))
    n2 = int(input("Ingresa la segunda nota: "))
    n3 = int(input("Ingresa la tercera nota: "))

    promedio = (n1 + n2 + n3) / 3

    if promedio >= 6:
        print (f"El alumno {i+1} esta aprobado con {promedio}")
    else:
        print(f"El alumno {i+1} NO esta aprobado con {promedio}")