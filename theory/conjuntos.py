#siempre se le establece como "set"
conjuntos=set()
conjuntos={1,2,3,"hola","como","estas"}
print(conjuntos)
#agrega un valor al conjunto
conjuntos.add(5)
print(conjuntos)
#corrobora si esta un valor especifico dentro del conjunto
print("3 in conjuntos:",3 in conjuntos)
#elimina un valor indicado
conjuntos.discard(1)
print("conjuntos.discard(1)=", conjuntos)