cant_alumnos = int(input("Ingresa la cantidad de alumnos que tiene el curso: "))
mayor_nota = 0
cont = 0
total_estu = 0
for i in range(cant_alumnos):
    trab_integrador = float(input(f"Ingresa la nota del trabajo integrador del alumno {i+1}: "))
    exposicion = float(input(f"Ingresa la nota de la exposicion del alumno {i+1}: "))
    parcial = float(input(f"Ingresa la nota del parcial del alumnos {i+1}: "))
    nota_final = (trab_integrador * 0.35) + (exposicion * 0.25) + (parcial * 0.40)
    if nota_final >= 6.5:
        print(f"El alumno {i+1} esta aprodabo")
    else:
        print(f"El alumnos {i+1} esta desaprobado")
    if trab_integrador >= 7.5:
        cont += 1
    if exposicion > mayor_nota:
        mayor_nota = exposicion
    if parcial > 4.0 and parcial < 7.5:
        total_estu += 1
porcentaje_alumnos = (cont / cant_alumnos) * 100
print(f"El {porcentaje_alumnos}% aprobo con mas del 7.5 en el traba integrador")
print(f"La nota mas alta de las exposiciones es {mayor_nota}")
print(f"El total de los estudiantes que tuvieron su nota entre 4 y 7.5 es {total_estu}")