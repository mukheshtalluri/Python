def swap(input_list, index1, index2):
    input_list[index1], input_list[index2] = input_list[index2], input_list[index1]

def pivot(input_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if input_list[i] < input_list[pivot_index]:
            swap_index += 1
            swap(input_list, swap_index, i)
    swap(input_list, pivot_index, swap_index)
    return swap_index

def quick_sort_helper(input_list, left, right):
    if left < right:
        pivot_index = pivot(input_list, left, right)
        quick_sort_helper(input_list, left, pivot_index -1)
        quick_sort_helper(input_list, pivot_index + 1, right)
    return input_list

def quick_sort(input_list):
    return quick_sort_helper(input_list, 0, len(input_list) -1)

my_input = [0, 3, 6, 1, 7, 4, 8, 2, 5, 9]
print(quick_sort(my_input))