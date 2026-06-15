def south_indian():
    yield "idly"
    yield "chappti"

def northindian():
    yield "chappti spl"
    yield "butter non"

def menu():

    yield from south_indian()
    yield from northindian()
menu()
