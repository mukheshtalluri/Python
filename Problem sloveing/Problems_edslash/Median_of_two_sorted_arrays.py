def median_of_sorted_arrays(list1, list2):
    merged_list = list1 + list2
    merged_list.sort()
    n = len(merged_list)
    if n % 2 == 0:
        return (merged_list[(n // 2) - 1] + merged_list[(n // 2)]) / 2
    else:
        return merged_list[(n // 2)]


l1 = [2, 4, 6, 8, 10]
l2 = [3, 7, 9, 12, 15]
print(median_of_sorted_arrays(l1, l2))