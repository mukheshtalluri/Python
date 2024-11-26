import math
def bucket_sort(input_list):
    no_of_buckets = round(math.sqrt(len(input_list)))
    max_value = max(input_list)
    arr = []

    for i in range(no_of_buckets):
        arr.append([])

    for j in input_list:
        index_b = math.ceil(j * no_of_buckets / max_value)
        arr[index_b - 1].append(j)

    for i in range(no_of_buckets):
        arr[i] = sorted(arr[i])

    k = 0
    for i in range(no_of_buckets):
        for j in range(len(arr[i])):
            input_list[k] = arr[i][j]
            k += 1
    return input_list

my_input = [0, 3, 6, 1, 7, 4, 8, 2, 5, 9]
print(bucket_sort(my_input))