
#Que es la asignacion simultanea
#a=5
#b=10
#c=15
a,b,c=10,15,20
print(f"a={a} b={b} y c={c}")

print("---------------")

#funciones que retornan valores simultaneos

def retornaValoresSimultaneos(a,b,c):
    return a+b,c
d,f=retornaValoresSimultaneos(4,5,6)
print(f"d={d} y f={f}")

print("---------------")

t=retornaValoresSimultaneos(4,5,6)
print(t)
print(f"t[0]={t[0]},t[1]={t[1]}")

print("---------------")

#Funciones que aceptan indeterminadas cantidad de valores

def indeterminadaParametros(*args):
    suma=0
    for i in args:
        print(f"{i}", end="+")
        suma=suma+i
    print(f"\nSuma={suma}")
indeterminadaParametros(4,5,6,7,8,9)