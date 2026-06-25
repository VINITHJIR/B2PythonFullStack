def decorator(func):
    def wrapper():
        print("🔔 Before service")
        func()
        print("🍽️ After service")
    print("wrapper adrress : " ,wrapper )
    return wrapper


@decorator #greet = decorator(greet)
def greet():
    print("Welcome customer")

print("greet address " , greet)
greet()