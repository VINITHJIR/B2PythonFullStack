def idly():
    print("Serving idly")

def dosa():
    print("Serving dosa")

menu = {
    "idly": idly,
    "dosa": dosa
}

order = "idly"

menu["dosa"]()