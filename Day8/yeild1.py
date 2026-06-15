def func():
    yield 1
    yield 2
    yield 3

g = func()

print(next(g))
print(next(g))
print(next(g))
print(next(g))