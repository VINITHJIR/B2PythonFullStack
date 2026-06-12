veg = {"idly" , "dosa" , "vada" , "poori" , "chapati"}
nonveg = {"chicken" , "mutton" , "fish" , "egg" , "prawn" , "idly" , "dosa" }

print(veg | nonveg) #union
print(veg & nonveg) #intersection
print(veg - nonveg) #difference
print(nonveg - veg) #difference
print(veg ^ nonveg) #symmetric difference
