edad=int (input("Ingresa tu eded: "))

#if edad >= 0 and edad < 100:
if 0 <= edad < 100:
    if edad >= 18:
        print ("El humano es mayor de edad")
    else:
        print ("El humano es menor de edad")
else:
    print ("esa edad no existe")