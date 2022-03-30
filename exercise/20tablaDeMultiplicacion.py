'''
num1=int(input("Dijita un numero del 1 al 10: "))
num2=num1
if num1 > 0 and num1 <11:
    for multiplos in range(2,11):
       res=num1*multiplos
       print(f"Multiplo {res/num2}: {res}")
       multiplos+1
else:
    print("Tarado, te dije un numero entre 1 y 10")
'''

while True:
    numero=int(input("Ingresa un numero entre el 1 y el 10: "))
    if numero < 1 or numero > 10:
        print(f"tarado, el numero {numero} no esta en el 1 y el 10")
    else:
        break
for i in range(10):
    print(f"{(i+1)} * {numero} = {(i+1)*numero}")