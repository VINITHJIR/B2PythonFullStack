menu = {"idly": 20, "dosa": 20, "vada": 15, "poori": 25, "chapati": 30}

print(menu.get("idly" , "Not available"))
print(menu.get("octobus fry" , "Not available"))
print(menu["idly"])
print(menu["octobus fry"])