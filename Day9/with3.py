salary = {
 "Vinith":50000,
 "Rahul":45000
}

with open("salary.txt","w") as file:

    for name, amount in salary.items():
        file.write(f"{name}:{amount}\n")
