def quick_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    pivot = input_list[len(input_list) // 2]
    left = [x for x in input_list if x < pivot]
    middle = [x for x in input_list if x == pivot]
    right = [x for x in input_list if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

my_input = [0, 3, 6, 1, 7, 4, 8, 2, 5, 9]
print(quick_sort(my_input))