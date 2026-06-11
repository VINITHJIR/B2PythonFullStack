value1 = (1, 2, 3, 4, 5 ,"vini", 45.5)
print(value1)
print(type(value1))
print(value1[0])
temp = list(value1)
temp[0] = 10
value1 = tuple(temp)
print(value1)

value1 = value1 + (100,)
print(value1)

