'''
En este ejercicio vamos a acceder a una lista de alumnos que tengan:
nombre
edad
calificación
Además un diccionario que tenga alumnos y maestros donde:
Los alumnos tendrán:
nombre
edad
calificación
Y los maestros tendrán:
nombre
grado
'''

'''
alumnos=[
    {"nombre":"Santino","edad":17,"calificacion":8},
    {"nombre":"Valentin","edad":17,"calificacion":9},
    {"nombre":"Alejo","edad":17,"calificacion":7},
    {"nombre":"Mariano","edad":16,"calificacion":10},
]
'''

#for alumno in alumnos:
 #   print(f"Nombre:{alumno['nombre']} Edad:{alumno['edad']} Calificacion:{alumno['calificacion']}")

escuela={
    "alumnos":[
        {"nombre":"Santino","edad":17,"calificacion":8},
        {"nombre":"Valentin","edad":17,"calificacion":9},
        {"nombre":"Alejo","edad":17,"calificacion":7},
        {"nombre":"Mariano","edad":16,"calificacion":10},
    ],
    "maestros":[
        {"nombre":"Carlos","grado":"Licenciatura"},
        {"nombre":"Maria Eugenia","grado":"Maestria"},
        {"nombre":"Pichi","grado":"Doctorado"},
    ]
}

print("ALUMNOS")
for alumno in escuela["alumnos"]:
    print(f"Nombre: {alumno['nombre']} Edad: {alumno['edad']} Calificaion: {alumno['calificacion']}")
print("\nMAESTROS")
for maestro in escuela["maestros"]:
    print(f"Nombre: {maestro['nombre']} Grado: {maestro['grado']}")

#print(escuela)