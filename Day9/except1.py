try:
    data = int(input("Enter the value"))
    print(100/data)

except ValueError:
    print("Incorrect values are given ")

except ZeroDivisionError:
    print("there is no possiblity of number/0 = infinity ")

finally:
    print("operation completed ")