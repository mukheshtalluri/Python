def squares_of_sorted_array(input_list):
    for i in range(len(input_list)):
        input_list[i] = input_list[i] ** 2
    input_list.sort()
    return input_list

my_input = [-3, 6, -5, 1, 7]
print(squares_of_sorted_array(my_input))