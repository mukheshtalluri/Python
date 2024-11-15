from array import array
"""
Array : Array is collection of similar data types. 
"""
my_array = array("i", [1, 2, 3, 4, 5, 6, 7]) # Based on the type code we can initialise the values.
print(my_array)

# Print all the values in an array - T.C : O(n)
for i in my_array:
    print(i)

# Append value to array - T.C : O(1)
my_array.append(8)
print(my_array)

# Insert value to array - T.C : O(n)
my_array.insert(0, 0)
print(my_array)

# Pop value from the array - T.C : O(n) / O(1)
my_array.pop() # If you pass any index value in pop as the argument it will remove that value otherwise it will remove last value.
print(my_array)

# Adding some array of elements to original array - T.C : O(len(second_array))
my_array_1 = array("i", [8, 9, 10, 11, 12])
my_array.extend(my_array_1)
print(my_array)

# Adding list elements to the array - T.C : O(len(list))
my_list = [13, 14, 15]
my_array.fromlist(my_list)
print(my_array)

# Buffer info method will show the buffer information about the array and no.of elements.
print(my_array.buffer_info())

# Count method will count the no.of elements in the array - T.C : O(n)
print(my_array.count(1))

# Index method will give us the index of element - T.C : O(n)
print(my_array.index(5))

# Remove method will remove element from the array - T.C : O(n)
my_array.remove(15) # If any element which is not present in the array it will show the ValueError.
print(my_array)

# Reverse method is used to reverse the elements in an array - T.C : O(n)
my_array.reverse()
print(my_array)

# Array supports for the slicing as well we can do as per the requirement.


