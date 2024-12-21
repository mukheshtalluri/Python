""" Linear search will go through all elements of an array and once it find the target value it will return the index.

"""
def linear_search(input_list, target_value):
    n = len(input_list)
    for i in range(n):
        if input_list[i] == target_value:
            return f"Value found at the index of {i}."
        return "Value not found."

my_input = [8, 5, 3, 1, 4, 7, 9]

print(linear_search(my_input, 7))