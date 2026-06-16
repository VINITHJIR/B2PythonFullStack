employees = ["Vinith","Rahul","Arun"]

with open("employees.txt","w") as file:

    for emp in employees:
        file.write(emp + "\n")
