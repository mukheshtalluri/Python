"""
Control flow statements : While coding we will face some situation if condition is true execute this block of code else execute other code block.
In python, we have if, elif and else blocks are there we will use their use cases in this module.
"""
# Check the number is even or odd.
num = -5
if num == 0:
    print(f"{num} is not even or odd number.")
elif num % 2 == 0:
    print(f"{num} is a even number.")
else:
    print(f"{num} is a odd number.")

# Nested control statements
num = -5
if num == 0:
    print(f"{num} is not even or odd number.")
elif num % 2 == 0:
    print(f"{num} is a even number.")
    if num < 0:
        print(f"{num} is a negative number.")
    else:
        print(f"{num} is a positive number.")
else:
    print(f"{num} is a odd number.")
    if num < 0:
        print(f"{num} is a negative number.")
    else:
        print(f"{num} is a positive number.")


"""
Loops : If want to execute same line of code multiple times we will use loops. There are 2 types of loops are there for loop and while loop.
Why loops : we want write same line of code multiple times for large no.of times we will use loops. Code duplication is not good practice.

For loops : It will work based on the length of iterable.
while loops : It will work on based on the condition, If condition not provided properly it will leads to infinite loop.
"""
list_of_fruits = ["apple", "banana", "cherry", "orange", "grape"]

for i in list_of_fruits:
    print(i)

num = 1
while num <= 10:
    print(num)
    num += 1      # In this step we provided the increment if we miss to provide increment it will lead to infinite loop.


# Some useful functions.
# Range --> Range function is used to generate values with in the range.
for i in range(10): # lower bound will be always zero, and value will be generated less than the upper bound.
    print(i)

# Enumerate --> Enumerate function will generate the sequence values along with the values.
list_of_fruits = ["apple", "banana", "cherry", "orange", "grape"]

for i, val in enumerate(list_of_fruits):
    print(f"{i} : {val}")

# Zip --> Zip function used to pack the lists and return the tuple.
list_of_index = [0, 1, 2, 3, 4]
list_of_fruits = ["apple", "banana", "cherry", "orange", "grape"]

for i in zip(list_of_index, list_of_fruits):
    print(i)

# In function
print("apple" in list_of_fruits)

# not in function
print("apple" not in list_of_fruits)

# Min and Max function
list_of_prices = [26, 78, 45, 34, 98, 31]
print(min(list_of_prices))
print(max(list_of_prices))

# Random --> Random function used to generate the random things.
import random
print(random.randint(1, 100)) # It will generate random value between the given range.

print(random.random()) # It will generate the value random floating value in between 0 to 1.

print(random.choice(list_of_prices)) # It will pick a random value from list.

print(list_of_prices)
random.shuffle(list_of_prices)
print(list_of_prices)





