lista=[1,1,1,2,3,3,8,4,5,6,6,7]
print(lista)
'''
conjunto=set()
conjunto=set(lista)
print(conjunto)
lista=list(conjunto)
lista.sort()
print(lista)
'''

lista=list(set(lista))
lista.sort()
print(lista)