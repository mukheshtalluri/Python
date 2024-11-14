"""
Generators : Generators are a special type of iterator in Python that allow you to iterate over a sequence of values lazily.
"""
def fibonacci(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        a, b = b, a+b

for i in fibonacci(10):
    print(i, end = " ")

def factorial(num):
    result = 1
    for i in range(1, num):
        result *= i
        yield result

for i in factorial(5):
    print(i, end = " ")

