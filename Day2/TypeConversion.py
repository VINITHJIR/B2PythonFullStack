#int -> float
#int -> bool
#int -> string

value = 10

print("value is " , value , " and DataType is " , type(value) , "and Coverted datatype is "  , type(value))

value1 = 10
value2 = float(value1)

print("value is " , value1 , " and DataType is " , type(value1) , "and Coverted datatype is "  , type(value2) , "value is " , value2)


value1 = 10
value2 = bool(value1)

print(f"value is {value1} and DataType is  {type(value1)} and Coverted datatype is {type(value2)} value is  {value2}")

value1 = 10
value2 = str(value1)

print(f"value is {value1} and DataType is  {type(value1)} and Coverted datatype is {type(value2)} value is  {value2 + '25'}")

value1 = str(5)
print('5' + value1)

