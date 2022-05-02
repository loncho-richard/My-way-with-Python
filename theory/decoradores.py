def A(B):
    def C():
        print("**********")
        B()
        print("**********")
    return C

@A
def B():
    print("Hola mundo")

B()