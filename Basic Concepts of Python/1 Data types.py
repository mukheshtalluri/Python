# Numbers --> Integers, Floating values
# Integers : Integers are nothing but whole numbers. Ex: -5, 3
# Floats : Numbers which consist of decimal values. Ex: 10.3, 5.6
# Variables : Variables are containers which can be used to store the data of any data type.

num_1 = 5  # Integer
num_2 = 10.5 # Floating value

# We can check the data type of variable using the type function.
print(type(num_1))
print(type(num_2))

# mathematical operations

# Addition
addition = num_1 + num_2
print(addition)

# Subtraction
subtraction = num_2 - num_1
print(subtraction)

# Multiplication
multiplication = num_1 * num_2
print(multiplication)

# Division
division = num_2 / num_1
print(division)

# Floor division
floor_division = num_2 // num_1
print(floor_division)

# Modulo
modulo = num_2 % num_1
print(modulo)

# Exponent
exponent = num_1 ** 2
print(exponent)

# Multiple operations --> It will work on the principle of BODMAS rule.
print( num_1 * num_2 + num_1 / num_2)

# Rounding the value
print(round(num_1 * num_2 + num_1 / num_2, 2))

"""
Some basic rules to define variables
1. Variable names are always start with alphabets or underscore.
2. No spaces and special characters are allowed in variable names.
3. Numeric values can be used in middle or end of variable not at the beginning.
4. Variables are used to define with the snake_case, PascalCase or camelCase for the good practice.
5. Aviod python built in key words while defining the variables.
6. Try to use good naming convention to let other understand.
"""

# Strings : String is a sequence of characters. It is immutable data type which means value assignment can not be possible.
my_city = "Bangalore" # There are many methods are there for the string will discuss in other module.

# Find the length of string.
print(len(my_city))

# String indexing
print(my_city[0])

# String slicing --> slicing consist of 3 arguments 1 - Starting index, 2 - Ending index, 3 - Step definition
print(my_city[1:])
print(my_city[5:])
print(my_city[1:7:2])
print(my_city[-5:-1:2])

# Convert string to upper case
print(my_city.upper())

# Convert string to lower case
print(my_city.lower())

# Convert string to title case --> In the string each and every word first letter is upper case
print(my_city.title())

# Convert string to capitalize case --> In the string first word, first letter only upper case.
print(my_city.capitalize())

# String formating : We can format string in 3 different methods. Some time as a part of project we need to check older code as well in that condition it will help us.
"""
String formating : In some situation we need to print integers along with the strings it will raise an exception
to aviod that we need to use string formating.
"""
# Normal conventional way of printing without formating.
kingdom = "Vijaya nagara"
age = 500
print(kingdom + " kingdom is one of the ancient kingdom with " + str(age) + " years old.")

# By using of the string formating.
print(f"{kingdom} kingdom is one of the ancient kingdom with {age} years old.")

# Different ways of string formating.
# Method 1 : Formating with a placeholders.
# String formating
# %s --> It will represent the string objects. str()
# %r --> It will represent the string format of an object with quotes everything. repr()
# %d --> It will represent integer value. In case any floating will be there it will convert as the integer.
# %f --> It will represent float value with the precession.
print("I am going to buy %s of 1 kg." %"apples")
print("I am here to develop %s and %s applications." %("web", "mobile"))

print("I am going to buy %s of 1 kg." %"\t apples")
print("I am going to buy %r of 1 kg." %"\t apples")

print("I am going to buy %d kg's of apples." % 4.5)

print("My weight is : %5.2f. And age is : 25." % 68.578)
print("My weight is : %25.2f. And age is : 25." % 68.578) # 25 will represent the total length of the number and 2 will represent the precession.

# Method 2 : Formating with a .format method.
print("I am going to buy {} of 1 kg.".format("apple"))
print("I am going to buy {} kg's of {}.".format(4.5, "apples"))

print("I am going to buy {1} kg's of {0}.".format("apples", 4.5)) # Using index positions.

print("I am going to buy {a} kg's of {b}.".format(b = "apples", a = 4.5)) # Using keywords.

print("I am going to buy {a} kg's of {b} and {a} kg's of orange.".format(b = "apples", a = 4.5)) # We can aviod duplicates.

print('{0:8} | {1:9}'.format('Fruit', 'Quantity')) # We can do alignment padding.
print('{0:8} | {1:9}'.format('Apples', 3.))
print('{0:8} | {1:9}'.format('Oranges', 10))

print('{0:<8} | {1:^8} | {2:>8}'.format('Left','Center','Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11,22,33))

print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left','Center','Right'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11,22,33))

print("My weight is : {0:5.2f}. And age is : 25.".format(65.578))

# Method 3 : Formating with f-string method.
print(f"My weight is : {65.578}. And age is : 25.") # It will be applicable to all types.

# Boolean : It will consist of the 2 statements True and False.
statement_true = True
print(type(statement_true))

statement_false = False
print(type(statement_false))





















