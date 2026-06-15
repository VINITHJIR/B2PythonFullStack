
def square(value):
    return value ** 2

listvalue = [10, 20, 30, 40]
totalvalues = map(square, listvalue)
print(list(totalvalues))


listvalue2 = [10 , 20 , 30 , 40]
totalvalues = map(lambda x :x*1.18 ,listvalue2)
print(list(totalvalues))