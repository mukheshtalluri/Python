def linear_search(input_list, value):
    for i in range(len(input_list)):
        if input_list[i] == value:
            return f"Value found at the index of {i}."
    else:
        return "Value not found."

my_input = [1, 6, 2, 8, 7, 3, 5, 4, 0, 9]
print(linear_search(my_input, 7))
