def binary_search(input_list, target_value):
    n = len(input_list)
    l = 0
    r = n - 1
    while l <= r:
        m =  (l + r) // 2
        if input_list[m] < target_value:
            l = m + 1
        elif input_list[m] > target_value:
            r = m - 1
        else:
            return f"Value found at the index of {m}"
    return "Value not found."


my_input = [8, 5, 3, 1, 4, 7, 9]

print(binary_search(my_input, 7))