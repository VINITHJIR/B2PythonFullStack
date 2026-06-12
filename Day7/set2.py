#add methods
set1 = {"idly" , "vada" , "dosa" , "poori" }
print("add an value to the set")
set1.add("biriyani")
print(set1)
print("add an more than one value to the set")
set1.update(["biriyani" , "fried rice" , "noodles"])
print(set1)

#remove methods
print("remove an value from the set")
set1.remove("vada")
print(set1)
print("remove an more than one value from the set")

set1.difference_update(["idly" , "poori"])
print(set1)

print("pop method")
set1.pop()
print(set1)
print("remove all set value from the set")
set1.clear()
print(set1)

numbers = {1, 2, 3, 4, 5}
numbers.discard(30)
print(numbers)