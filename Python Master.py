"""
# Here we will discuss the theory part.

What is Programing: Programing is the only way to interact with the computers. Computers are dumb machines they do what
we tell us do. For any complex problems we can use computers to get quicker solutions.

Why Python: Python is very simple syntax used programing language. We can use python in various fields such as
Web development, Gaming, Data science, Machine learning, Desktop application.Python is high level programing language and
dynamically typed langauge, Python is Interpreted programing language since debugging very easy.Python having huge library
support which can makes our work easier.

Dynamically typed: No need to define syntax, It will understand type of variable while running the code.
High level language: Human readable code, Computers only understand 0 and 1 only in case high level programing languages
we can see the exact code.
Interpreted programing languages: Execution happen line by line. Python primary know as the interpreted programing language
after run the code by python compiler it will convert into the byte code and python virtual machine execute the byte code.

What is REPL: After installation of python it will come with the Python IDLE, Python Idle works on the principle of REPL
R - Read, E - Execution, P - Print, L - Loop These are the 4 operations executing continuously.

Modules and Pip : Modules are some set of functions which were define in that python file. when we want to use those functions
we need to import that python file as package.There are 2 types of modules in python External modules and internal modules.
Internal modules we can use directly by using of import key word. When we want to use external modules we need to install them
through package installer after installation we use them as the internal modules. Pip is the package installer it will help us
to install external packages.
Usage of internal module: import math --> Math is the one of internal module we can use like this
Usage of external module: pip install pandas --> It will install pandas then,  import pandas --> Then we can use this module.

Print function: When we want to print something to the console will use the print function, It will consist of several arguments
which will discuss one by one
sep: sep will be one key word which can use to separate variables with defined character. by default, it will be space.
end: end will useful when want to print things in the same line. by default, it will \n.
file: print something directly to file.
flush: flush will help us to print something forcefully without buffering. by default, it will false.

Comments: Comments will help us to skip the commented information not executed by the compiler. Basically we will use comments
for any information required about the program like how it will work. There are two types of comments we can use single line
comment and multiline comments.

Escape character (Backslash): Some symbols having special meaning for their occurrence in python. want escape that
special meaning we can use the escape character.

Variable: Variables are used to hold the data. It can store any kind of data. Variables are case-sensitive and it can be replaceable.
In python, we have special keywords are there don't use them for the variables.

Data types: Data types are the classification of data and operations can be performed on that data.We will use the different data types
Numeric data: The data which associated with the numbers. In which we have Integers, Float, Complex.
Text data: The data which is in the form of Text. Strings
Boolean data: The data associated with the True or False.
Sequence data: The data which is associated with the multiple values in the same sequence. In which we have List, Tuple
Mapped data: The data associated with the key, values. Dictionary.
We can check data type by using type function.

Arithmetic operators: When we want to perform any mathematical action such as addition, subtraction, multiplication,
division, floor division, modulo, exponent. will use the mathematical operators.

Comparison operators: Comparison operators help us to evaluate two numbers.Comparison operators are Equal, Less than,
Greater than, Not equal, Less than or equal,Greater than or equal. These are the comparison operators.

Assignment operators: When we want to assign something to variable we will use the assignment operators.

Logical operators: Logical operations are used to evaluate the multiple expressions. And operator used to return True when
both the expressions are True. Or will return True when any one of expression is True. Not is used evaluate the until empty kind condition.

Bitwise operators: Bitwise operators will perform on binary numbers. Initially it will convert decimal number to binary number
then it will perform the bit wise operation. we have few bitwise operations such as the and, or, XOR, not, Left shift, Right shift.

Membership operators: Membership operator will help us find the value present in the target or not.

Identity operators: Identity operator is used to compare the two variable memory address.

Type casting: Conversion of one data type to other data type is know as the type casting. There are two types of type casting
explicit type conversion: The conversion of one data type to other data type explicitly by the programmer.
implicit type conversion: While performing any operations data type will change automatically this is implicit type casting.

User input: User input is something we need to take from the user as the input. if you provide int, float any data type
by default it will be string we need to do type casting based on the requirement. for the user input will use input function.

String and string methods: String is series of characters which are arranged in sequential manner. Since string is series of
characters it will support for the indexing. String is an immutable data type.
Indexing: The items are arranged in the sequential order and number to that particular order. index always start from 0.
Immutable: Once data type is created it cont be changeable.


"""
# Using internal module
import math
print(math.sqrt(9))

# Using external module
#import matplotlib #It will give error since it was installed in machine, first we need to install using pip then we use library.

# Print function
print("Type something here..")

a, b = 5, 7
print(a, b, sep = " - ")
print(a, end = " ")
print(b)
print()

# Comments
# Hash symbol will use to comment the information. This is the single line comment
"""
When we want do multi lines as the comment we can define like that.
This is will won't recognised by the compiler and this portion will skip from the execution.
"""

# Escape character
# I want to print something to console like this --> I'm very versatile programing language.
print('I\'m very versatile programing language.') # By using of escape character we skip the special meaning of single quote.

# Variables
a, A = 7, 16 # we can store different values in upper case and lower case this is called case-sensitive.
print("The value of a : ",a)
print("The value of A : ",A)
a = 25
print("This value after replacement : ",a)

# data types:

# Numeric data types
num_int = 5 # Which is associated with the whole numbers.
print("The '5' data type is: ", type(num_int))
num_float = 6.5 # Which is associated with the decimal values.
print("The '6.5' data type is: ", type(num_float))
num_complex = 6 + 2j # Which is associated with the complex numbers.
print("The '6 + 2j' data type is: ", type(num_complex))

# Text data types
city = "Bangalore" # Which is associated with the series of characters.
print("The 'Bangalore' data type is: ", type(city))

# Sequenced data types # Series of numbers can be changeable after defining.
scores = [22, 12, 23, 19, 18] # Series of numbers can be changeable after defining.
print("The 'scores' data type is: ", type(scores))
marks = (22, 12, 23, 19, 18) # Series of numbers can be not changeable after defining.
print("The 'marks' data type is: ", type(marks))

# Mapped data type store in the form of key and value.
person_info = {"name":"Alex", "age": 25, "phone_no":12345678}
print("The 'person_info' data type is: ", type(person_info))


# Mathematical operators
# Addition : addition of the two numbers
a, b = 5, 6
print("The addition of two numbers will be :",a + b)

# Subtraction : Subtraction of the two numbers
a, b = 5, 6
print("The subtraction of two numbers will be :",a - b)

# Multiplication : Multiplication of the two numbers
a, b = 5, 6
print("The multiplication of two numbers will be :",a * b)

# Division : Division of the two numbers
a, b = 5, 6
print("The division of two numbers will be :",a / b)

# Floor division : Floor division of the two numbers it will integer as return value.
a, b = 5, 6
print("The floor division of two numbers will be :",a // b)

# Modulo : Remainder of two values.
a, b = 5, 6
print("The modulo of two numbers will be :",a % b)

# Exponent : Power of one number with the other one.
a, b = 5, 6
print("The exponent of two numbers will be :",a ** b)


# Comparison operators
# Equal : If both values are equal it will return True else False.
a, b = 5, 6
print("Both values are equal :",a == b)

# Not equal : If values are not equal then it will return True
a, b = 5, 6
print("Both values are not equal:", a != b)

# Less than : If value is less then the compared value return True.
a, b = 5, 6
print("The value of a is less than b:", a < b)

# Greater than : If value is greater than the compared value return True.
a, b = 5, 6
print("The value of a is greater than b:", a > b)

# Less than or equal : If the value is less or equal to the compared value it will return True.
a, b = 5, 6
print("The value of a is less than or equal to b:",a <= b)

# greater than or equal : If the value is greater or equal to the compared value it will return True.
a, b = 5, 6
print("The value of a is greater than or equal to b:",a >= b)


# Assignment operators
# Equal : Used to assign value to variable
a = 5

# Add and assign : Adding value and assign to the variable
a += 5

# Subtract and assign : Subtract value and assign to the value
a -= 5

# Multiply and assign : Multiply value and assign to the value
a *= 5

# Division and assign : Division value and assign to the value
a /= 5

# Floor division and assign : Floor division value and assign to the value
a //= 5

# Modulo and assign : Modulus value and assign to the value
a %= 5

# exponent and assign : Exponent value and assign to the value
a **= 5


# Logical operations
# and operator : If both expressions are True then True else False
a, b = 7, 3
print("Both the expressions are True :", a > 5 and b < 5)

# or operator : If any one of expression is True it will be True else False.
a, b = 7, 3
print("Any one expressions is True :", a > 5 or b > 5)

# not operator : it is used evaluate negative condition.
# while stack is not empty() --> These kind of scenarios will use not.


# Bitwise operations
# Bitwise and operator : Both the values are True then return True
a, b = 5, 3 # 0101 & 0011 -> 0001
print("The bitwise and for the a and b :", a & b)

# Bitwise or operator : Any one of the values is True then return True
a, b = 5, 3 # 0101 | 0011 -> 0111
print("The bitwise or for the a and b :", a | b)

# Bitwise XOR :
a, b = 5, 3 # 0101 | 0011 -> 0110
print("The bitwise XOR for the a and b :", a ^ b)

# Bitwise not operator : This performs operation on the single variable.
a = 5 # 0101 - -1010
result = ~a
print("The bitwise not for the a:", result)

# Bitwise left shift : This performs operation on the single variable.
a = 5 # 0101 - 1010
result = a << 1
print("The bitwise left shift for the a:", result)

# Bitwise right shift : This performs operation on the single variable.
a = 5 # 0101 - 0010
result = a >> 1
print("The bitwise right shift for the a:", result)

# Membership operator
# in operator: If value in the target it will return True else False
num = [1, 2, 3, 4, 5, 6, 7]
print("The value 7 in num :", 7 in num)

# not in operator : If value not in the target it will return True else False
print("The value 16 in num :", 16 not in num)

# Identity operator
# is operator: It will compare the memory address of the values
a, b = 5, 5
print("The value a is b :", a is b)

# is not operator: It will compare the memory address of values if memory address is not same it will return True
a, b = 5, 6
print("The value a is not  b :", a is not b)


# Type casting
# Explicit type casting:
num = input("Enter the num: ")
print("Before explicit type casting :",type(num))
num = int(num)
print("After explicit type casting :",type(num))

# Implicit type casting:
num = 5
print("Before implicit type casting :", type(num))
num += 6.0
print("After implicit type casting :", type(num))

# User input
name = input("Enter your name :")
print("The user input value is :",name)

# Strings
name = "Bangalore"
print(name)

# Multiline string
poem = """The red fence
takes the cold trail
north; no meat
on its ribs
but neither has it
much to carry."""
print(a)

# Memory address of the name
print(id(name))

# Indexing of String
print(name[0])

# Loop through string
for i in name:
    print(i)

# String slicing : Slicing is the process of cut string into pieces with the specified notations
print(name[0:5:2]) # 0 - lower index, 5 - upper index, 2 - step definition
print(name[1: -1]) # -1 will be the upper index of string, we make the string with the negative index as well.
print(name[0: 7: -1]) # negative step index will print string in the reverse order.

# String methods
# upper - It will convert all characters to upper case
print(name.upper())

# lower - It will convert all characters to lower case
print(name.lower())

# strip - It will trim empty spaces from the starting and trailing places.
test = "       Test          "
print(test.strip())

# rstrip - It will remove trailing characters with the specific argument
test_1 = "Name.....!!!"
print(test_1.rstrip("!"))

# replace - It replace the character with other character.
print(name.replace("B", "M"))

# split - Split method is used to divide the given staring into pieces based on argument given, and it will return list object.
print(name.split("a"))

# capitalize - It will return in the given string first character will be upper case remaining all are the lower case.
name = name.lower()
print(name.capitalize())

# center - Center method is used to move the string to words center.
print(name.center(25, "."))

# count - Count method is used to count the characters of given argument.
print(name.count("a"))

# endswith - String end with the particular character which we provided as argument then it will return True.
print(name.endswith("e"))

# find - Find is used to find something in the string.
print(name.find("ban"))

# index - Index is used to get index position of search in the string.
print(name.index("a"))

# isalnum - If string only contain A-Z, a-z, 0-9 Then it will return True
print(name.isalnum())

# isalpha - If string only contain A-Z, a-z Then it will return True
print(name.isalpha())

# islower

# isprintable

# isspace

# istitle

# isupper

# startswith

# swapcase

# title
















