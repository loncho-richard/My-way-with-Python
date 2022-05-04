def closureValidador(a,b):
    def validar():
        if a>0 and b>0:
            return True
        else:
            return False
    return validar

validado=closureValidador(4,1)
print(validado())