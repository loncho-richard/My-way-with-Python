a={1,2,3,4}
b={4,5,6,7}
d={1,2,3,4,5,6}
e={11,12,13,14,15,16}
print("a==b:", a==b)
#la suma de dos conjuntos 
c=a|b
print("c=a|b:", c)
#la resta de dos conjuntos
c=a-b
print("c=a-b:", c)
#la interseccion de dos conjuntos
c=a&b
print("c=a&b:", c)
#la diferencia simetrica de dos conjuntos
c=a^b
print("c=a^b:", c)
#sub conjuntos
print("a.issubset(d):", a.issubset(d))
print("d.issubset(a):", d.issubset(a))
#super conjunto
print("d.issubset(a):", d.issuperset(a))
#disconexos
print("a.isdisjoint(e)", a.isdisjoint(e))
#conjuntos inmutables
f=frozenset({1,2,3})
##f.add(2) "no se puede"