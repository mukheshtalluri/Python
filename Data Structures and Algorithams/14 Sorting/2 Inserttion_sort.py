def insertion_sort(input_list):
    for i in range(1, len(input_list)):
        key = input_list[i]
        j = i - 1
        while j >= 0 and key < input_list[j]:
            input_list[j + 1] = input_list[j]
            j -= 1
        input_list[j + 1] = key
    return input_list

my_input = [0, 3, 6, 1, 7, 4, 8, 2, 5, 9]
print(insertion_sort(my_input))
