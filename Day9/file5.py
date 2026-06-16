file = open("employee.txt" , "w")
file.write("Hello Python Programmers \n")
file.close()

file = open("employee.txt" , "a")
file.write("Hello fullstack Programmers \n")
file.close()

file = open("employee.txt" , "r")
data = file.read()
print(data)