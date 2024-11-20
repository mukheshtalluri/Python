"""
Recursion : Recursion is the Iterative approach to solve a problem using the stack implementation.
1. Recursive calls are maintained by the stack memory.
"""
def first_method():
    second_method()
    print("First method executed.")

def second_method():
    third_method()
    print("Second method executed.")

def third_method():
    fourth_method()
    print("Third method executed.")

def fourth_method():
    print("Fourth method executed.")

first_method()


# Print numbers upto the given number.
def numbers(n):
    if n == 1:
        print(n)
    else:
        numbers(n-1)
        print(n)

numbers(10)

# Find the factorial of the number.
def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

# Find the fibonacci series of upto n numbers.
def fibonacci_series(n):
    if n in [0, 1]:
        return n
    else:
        return fibonacci_series(n - 2) + fibonacci_series(n - 1)

for i in range(10):
    print(fibonacci_series(i), end = " ", sep = " ,")
print()

# Sum of digits in a number.
def count_number(n):
    if n <= 9:
        return n
    else:
        return n % 10 + count_number(n // 10)

print(count_number(123456789))






