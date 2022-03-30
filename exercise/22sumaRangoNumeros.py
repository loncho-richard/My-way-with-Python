'''
Programa que pida numero enteros y los vaya sumando.
Si el número introducido esta dentro de 100 y 200 o es 0 cerrar el programa.
'''
suma=0
while True:
    numero=int(input("Ingresa un numero entre el 100 y el 200 para ser sumado, si precionas 0 se cierra el programa: "))
    if numero>=100 and numero<=200:
        suma=suma+numero
        print(f"Aqui esta tu resultado: {suma}")
    else:
        print(f"tu numero {numero} no esta dentro del 100 y el 200")
    if numero==0:
        break