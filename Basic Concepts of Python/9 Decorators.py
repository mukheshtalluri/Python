"""
Decorators : Decorators are the functions which will change the behavior of the anthor function while run time without changing the existing code.
Usage of decorators : If we don't have access for the existing function still we want to change behavior of the function while run time we will use decorators.
"""
def division(a, b):
    return a / b
print(division(2, 4)) # 0.5 is the expected output.but i want to get value always higher than 1.

# Method 1 : Without using decorators.
def division_1(a, b):
    if a < b:
        a, b = b, a
    return a / b
print(division_1(2, 4))

# Method 2 : Using Decorators : I don't want to change anything in the function but i want to change some of the things while run time.
def my_decorator(func):
    def wrapper(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return wrapper

@my_decorator
def division_2(a, b):
    return a / b

print(division_2(2, 4))


def decorator(func):
    def wrapper(value):
        if type(value) == int:
            value = float(value)
        elif type(value) == float:
            value = int(value)
        return func(value)
    return wrapper


@decorator
def float_to_int(num):
    return num

print(type(float_to_int(5.8)))




