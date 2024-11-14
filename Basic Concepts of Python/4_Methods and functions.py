"""
Functions : Function is reusable block of code designed to perform specific task.
Method : If the function is subjected to any class then it will be method.
"""
# Function : We can create custom functions based on the requirement.
# Function with no input.
def sample():
    print("Welcome to functions.")
sample()

# Function with some input.
def greet(name):
    print(f"Hello {name}. How are you ?")
greet("Bob")

# Function with the multiple inputs
def addition(num_1, num_2):
    result = num_1 + num_2
    print(f"The sum of {num_1} and {num_2} is : {result}")
addition(5, 6)

# Functions with key word arguments and Positional arguments.
# Function with positional arguments
def subtraction(num_1, num_2):
    result = num_1 - num_2
    print(f"The subtraction of {num_1} and {num_2} is : {result}")
subtraction(6, 3) # It will take default positions as mention in function.

# Function with keyword arguments
def division(num_1, num_2):
    result = num_1 / num_2
    print(f"The division of {num_1} and {num_2} is : {result}")
division(num_2 = 6, num_1 = 3) # It won't take based on the position reference which provided by us.
