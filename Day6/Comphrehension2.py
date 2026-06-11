values = [i for i in range(10) if i %2 ==0]
print(values)


listvalue = ["vini", "anushka", "thamana", "sneha", "sneha", "anushka"]
length = len(listvalue)
values = [listvalue[i].upper() for i in range(length) if listvalue[i].strip()]
print(values)


listvalue = ["vini", "anushka", "thamana", "sneha", "sneha", "anushka"]
length = len(listvalue)
values = [listvalue[i].upper() for i in range(length) if listvalue[i].strip()=="sneha"]
print(values)