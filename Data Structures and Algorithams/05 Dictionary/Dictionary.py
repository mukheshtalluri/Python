"""
Dictionary : Dictionary will consist the elements in the key, value pair.in which no key is duplicate.
1.
"""
my_dict = {1 : "a", 2 : "b", 3 : "c", 4 : "d"}

# Print all values from the dictionary.
for i, val in my_dict.items():
    print(f"{i} : {val}")

# Access the value from dictionary using key.
print(my_dict[2])

# Print all keys from the dictionary.
print(my_dict.keys())

# Print all values from the dictionary.
print(my_dict.values())

# Access the value of dictionary using key and get method.
print(my_dict.get(1))

# Remove the value from the dictionary using key.
my_dict.pop(4)
print(my_dict)

# Remove an element from the end of dictionary.
my_dict.popitem()
print(my_dict)

# Update dictionary with the anthor dictionary.
my_dict_1 = {3 : "c", 4 : "d", 5 : "e"}
my_dict.update(my_dict_1)
print(my_dict)