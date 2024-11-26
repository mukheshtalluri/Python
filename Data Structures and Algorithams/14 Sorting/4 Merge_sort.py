def merge(input_list, low, mid, right):
    n1 = mid - low + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = input_list[low + i]

    for j in range(n2):
        R[j] = input_list[mid + j + 1]

    i = 0
    j = 0
    k = low
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            input_list[k] = L[i]
            i += 1
        else:
            input_list[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        input_list[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        input_list[k] = R[j]
        j += 1
        k += 1


def merge_sort(input_list, low, high):
    if low < high:
        mid = (low + (high - 1)) // 2
        merge_sort(input_list, low, mid)
        merge_sort(input_list, mid + 1, high)
        merge(input_list, low, mid, high)
    return input_list

my_input = [0, 3, 6, 1, 7, 4, 8, 2, 5, 9]
print(merge_sort(my_input, 0, 9))


