x=float(input("Ingresa el valor de x"))
y=float(input("ingrese el valor de y"))
dividendo=(y**2)-1
if dividendo!=0:
    res= ( x**(1/2) ) / dividendo
    print(f"Aqui esta tu resultado{res}")
else:
    print(f"El valor de Y no puede ser {y}")