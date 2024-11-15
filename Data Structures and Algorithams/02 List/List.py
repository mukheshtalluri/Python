"""
List : List is an ordered mutable data structure. List will allow duplicates and supports for the slicing.
1. In the list data structure we can store different data types.
2. List will support various in built operations.
"""
my_list = ["apple", "bat", "cat", "dog", "elephant", "fox"]
print(my_list)

# Print all the values in a list
for item in my_list:
    print(item)

# Append value to the list
my_list.append("goat")
print(my_list)

# Pop value from the list with index or without index
my_list.pop()
print(my_list)

# Insert value to the list
my_list.insert(6, "goat") # If you provide the value which has the index more than inside a list then it will append.
print(my_list)

# Remove value based on the element name
my_list.remove("goat")
print(my_list)

# Index method will find the index position of element
print(my_list.index("bat")) # If value not there in the list it will raise ValueError

# Count method will count no.of times that element repeated.
print(my_list.count("apple"))

# Extend method will add anthor list to the original list.
my_list_1 = ["goat", "horse", "ice-cream"]
my_list.extend(my_list_1)
print(my_list)

# Reverse method will reverse the elements in a list.
my_list.reverse()
print(my_list)

# Sort method will arrange the elements in the either ascending or descending order.
my_list.sort(reverse=False) # For True it will come in the descending order, False it will come as the ascending order.
print(my_list)

# Clear method will remove all elements from the list.
#my_list.clear()
print(my_list)

# List slicing : Slicing is the concept where we can trim the list as per requirement.
# In slicing maily we have 3 things initial index, final index, step definition
print(my_list[1:8:2])

# Using negative index --> It will print the list in reverse order.
print(my_list[::-1])

# List comprehension : It is the concept where we can make list using some condition.
numbers = [x for x  in range(21)] # Here also we can use initial index, final index, step definition.
print(numbers)

squares = [x ** 2 for x in range(1, 11)]
print(squares)

even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)

# List flatten : If we have a 2D array we want to make it 1d array.
two_d_list = [[1, 2, 3], [4, 5, 6]]
one_d_list = []
for i in range(len(two_d_list)):
    for j in range(len(two_d_list[i])):
        one_d_list.append(two_d_list[i][j])

print(one_d_list)

# ternary operator
even_or_odd = ["even number" if x % 2 == 0 else "odd number" for x in range(1, 21)]
print(even_or_odd)
