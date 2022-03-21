'''
S o s: Suma.
R o r: Resta.
M o m: Multiplicación.
D o d: División.
'''
print("Ingresa dos numeros")
num1=int(input("Numero 1:"))
num2=int(input("Numero 2:"))
opcion=input("Selecciona lo que quieres hacer con eses dos numeros\n\
S s=Suma\n\
R r=Resta\n\
M m=Multiplicacion\n\
D d=Divicion\n"
)
opcion=opcion.lower()
res=0

if opcion=='s':
    res=num1+num2
    print(f"El resultado de tu suma es {res}")
    quit()
if opcion=='r':
    res=num1-num2
    print(f"El resultado de tu resta es {res}")
    quit()
if opcion=='m':
    res=num1*num2
    print(f"El resultado de tu multiplicacion es {res}")
    quit()
if opcion=='d':
    res=num1/num2
    print(f"El resultado de tu divicion es {res}")
    quit()
else:
    print("Error")