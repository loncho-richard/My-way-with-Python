def functionOne():
    myVariable="Hello from functionOne"
    print(myVariable)

def functionTwo():
    myVariable="Hello from functionTwo"
    print(myVariable)
myVariable="Hello from outsite"
functionOne()
functionTwo()
print(myVariable)