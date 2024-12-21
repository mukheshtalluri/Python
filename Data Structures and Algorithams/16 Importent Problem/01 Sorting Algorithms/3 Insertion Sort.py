"""The Insertion Sort algorithm uses one part of the array to hold the sorted values, and the other part of the array to
hold values that are not sorted yet.

How it works:

--> Take the first value from the unsorted part of the array.
--> Move the value into the correct place in the sorted part of the array.
--> Go through the unsorted part of the array again as many times as there are values.

"""
def insertion_sort(input_list):
    n = len(input_list)
    for i in range(1, n):
        key = input_list[i]
        j = i - 1
        while j >= 0 and key < input_list[j]:
            input_list[j + 1] = input_list[j]
            j -= 1
        input_list[j + 1] = key
    return input_list

my_input = [8, 5, 3, 1, 4, 7, 9]

print(insertion_sort(my_input))

