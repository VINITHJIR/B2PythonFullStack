values =[]

for i in range(5):
    value = int(input("Enter a value: "))
    if value % 2 ==0:
     values.append(value)

print("The values you entered are:" , values)