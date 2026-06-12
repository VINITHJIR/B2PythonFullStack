menu = {"idly": 20, "dosa": 20, "vada": 15, "poori": 25, "chapati": 30}

print(menu["chapati"])

#add values in dict

menu["biriyani"] = 150

print(menu)
#update values in dict
menu["idly"] = 40
print(menu)

#delete values in dict
del menu["vada"]
print(menu)