niños = 0
jovenes = 0
adultos = 0
mayores = 0
pesoTotalNiño = 0
pesoTotalJoven = 0
pesoTotalAdult = 0
pesoTotalMayores = 0
promNiño = 0
promJoven = 0
promAdult = 0
promMayores = 0

for i in range(50):
    edad = int(input("Ingresa tu edad: "))
    
    if edad >= 0 and edad <= 12:
        niños = niños + 1
        pesoNiño = float(input("Ingresa tu peso: "))
        pesoTotalNiño = pesoTotalNiño + pesoNiño
        promNiño = (pesoTotalNiño / niños)
    
    elif edad >= 13 and edad <= 29:
        jovenes = jovenes + 1
        pesoJoven = float(input("Ingresa tu peso: "))
        pesoTotalJoven = pesoTotalJoven + pesoJoven
        promJoven = (pesoTotalJoven / jovenes)

    elif edad >= 30 and edad <= 59:
        adultos = adultos + 1
        pesoAdulto = float(input("Ingresa tu peso: "))
        pesoTotalAdult = pesoTotalAdult + pesoAdulto
        promAdult = (pesoTotalAdult / adultos)

    elif edad >= 60:
        mayores = mayores + 1
        pesoMayores = float(input("Ingresa tu peso: "))
        pesoTotalMayores = pesoTotalMayores + pesoMayores
        promMayores = (pesoTotalMayores / mayores)

print ("El promedio del peso de los niños es de: ", promNiño, "kg")
print ("El promedio del peso de los Jovenes es de: ", promJoven, "kg")
print ("El promedio del peso de los Adultos es de: ", promAdult, "kg")
print ("El promedio del peso de los Mayores es de: ", promMayores, "kg")