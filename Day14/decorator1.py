def greet():
    print("Welcome customer")


def decorator(func):
    def wrapper():
        print("🔔 Before service")
        func()
        print("🍽️ After service")
    return wrapper

greet = decorator(greet)
greet()

