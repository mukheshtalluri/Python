def merge_sort(input_list):
    if len(input_list) > 1:
        left_part = input_list[:len(input_list) // 2]
        right_part = input_list[len(input_list) // 2:]

        # Recursion
        merge_sort(left_part)
        merge_sort(right_part)

        # Merge
        i = 0
        j = 0
        k = 0
        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                input_list[k] = left_part[i]
                i += 1
            else:
                input_list[k] = right_part[j]
                j += 1
            k += 1

        while i < len(left_part):
            input_list[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            input_list[k] = right_part[j]
            j += 1
            k += 1

my_input = [8, 5, 3, 1, 4, 7, 9]
merge_sort(my_input)
print(my_input)


