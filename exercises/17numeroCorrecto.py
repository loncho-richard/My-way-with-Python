divisor=float(input("Ingresa el divisor"))
dividendo=float(input("Ingresa el dividendo"))
while dividendo<=0:
    print(f"El dividendo {dividendo} debe ser mayor a 0")
    dividendo=float(input("Ingresa el dividendo"))

divicion=divisor/dividendo
print(f"El resultado de tu divicion es {divicion}")