def bubble_sort(input_list):
    for i in range(len(input_list) -1):
        for j in range(len(input_list) -i -1):
            if input_list[j] > input_list[j + 1]:
                input_list[j + 1], input_list[j] = input_list[j], input_list[j + 1]
    return input_list

my_input = [0, 3, 6, 1, 7, 4, 8, 2, 5, 9]
print(bubble_sort(my_input))