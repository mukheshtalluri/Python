"""Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value.

How it works:
--> Go through the array, one value at a time.
--> For each value, compare the value with the next value.
--> If the value is higher than the next one, swap the values so that the highest value comes last.
--> Go through the array as many times as there are values in the array.

"""

def bubble_sort(input_list):
    n = len(input_list)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
    return input_list

my_input = [8, 5, 3, 1, 4, 7, 9]

print(bubble_sort(my_input))