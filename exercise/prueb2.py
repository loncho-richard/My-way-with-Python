
"""
valido = False
email = input("Introduce tu email: ")

for i in range(len(email)):
    if email[i] == "@":
        valido = True

if valido == True:
    print("Email correcto")
else:
    print("Email incorrecto")
    """

email= input("ingrese un email:")
com1 = False
com2 = False

for i in range(len(email)):
    if email[i]== "@":
        com1 = True
    if email[i]== ".":
        com2= True

if com1 and com2 == True:
    print("EMAIL CORRECTO")
elif com1 == True and com2 == False:
    print("te falta asignar el dominio del email")
elif com1 == False and com2 == True:
    print("te falta un arroba")
else:
    print("no pusiste un email")

