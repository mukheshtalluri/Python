def heapify(input_list, n, i):
    small = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and input_list[l] < input_list[small]:
        small = l
    if r < n and input_list[r] < input_list[small]:
        small = r

    if small != i:
        input_list[i], input_list[small] = input_list[small], input_list[i]
        heapify(input_list, n, small)

def heap_sort(input_list):
    n = len(input_list)
    for i in range(int(n/2) -1, -1, -1):
        heapify(input_list, n, i)

    for i in range(n-1, 0, -1):
        input_list[i], input_list[0] = input_list[0], input_list[i]
        heapify(input_list, i, 0)
    input_list.reverse()


my_input = [0, 3, 6, 1, 7, 4, 8, 2, 5, 9]
heap_sort(my_input)
print(my_input)
