# Map : Map function is used to connect with the function and iterable.
def even_or_odd(num):
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

numbers = [18, 25, 39, 43, 56, 61, 73, 89, 94]
list(map(even_or_odd, numbers))

# Map function with the lambda
print(list(map(lambda x : "Even number" if x % 2 == 0 else "Odd number", numbers)))

# Map function with the multiple iterables.
list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9, 10]
list_3 = [11, 12, 13, 14, 15]
print(list(map(lambda x, y, z : x + y + z, list_1, list_2, list_3)))

# Reduce function : Reduce function need min 2 inputs to max no.of inputs.
from functools import reduce
list_1 = [1, 2, 3, 4, 5]
print(reduce(lambda x, y : x + y, list_1)) # Sum of the list using the reduce function
print(reduce(lambda x, y: x if x > y else y, list_1)) # Find the maximum number from the list.

# Filter function : Filter function is used to filter some of the values based on function.
def even_numbers(num):
    if num % 2 == 0:
        return num

num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(even_numbers, num_list)))




