def south_indian():
    yield "idly"
    yield "chappti"

def northindian():
    yield "chappti spl"
    yield "butter non"

def menu():

    for i in south_indian():
        print(i)

    for i in northindian():
        print(i)

menu()
