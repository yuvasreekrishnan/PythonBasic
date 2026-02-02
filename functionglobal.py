a=20
b=30
print(a,b)

def accessvar():
    a=4
    b=6
    global accessvar
    print(a,b)
accessvar()
