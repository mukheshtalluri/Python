"""The Selection Sort algorithm finds the lowest value in an array and moves it to the front of the array.

How it works:
--> Go through the array to find the lowest value.
--> Move the lowest value to the front of the unsorted part of the array.
--> Go through the array again as many times as there are values in the array.

"""
def selection_sort(input_list):
    n = len(input_list)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if input_list[j] < input_list[min_index]:
                min_index = j
        input_list[i], input_list[min_index] = input_list[min_index], input_list[i]
    return input_list

my_input = [8, 5, 3, 1, 4, 7, 9]

print(selection_sort(my_input))