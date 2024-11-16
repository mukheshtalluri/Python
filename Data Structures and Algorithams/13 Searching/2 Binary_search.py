def binary_search(input_list, value):
    n = len(input_list)
    l = 0
    r = n - 1
    while l <= r:
        m = (l + r) // 2
        if input_list[m] > value:
            r = m - 1
        elif input_list[m] < value:
            l = m + 1
        else:
            return f"Value found at the index of {m}."
    return "Value not found."

my_input = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(my_input, 21))