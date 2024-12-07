def add_to_array_from_integer(input_list, k):
    input_num = 0
    for i in input_list:
        input_num = input_num * 10 + i
    to_list_num = input_num + k
    final_list = [] # 1234
    while to_list_num > 0:
        final_list.append(to_list_num % 10)
        to_list_num = to_list_num // 10
    final_list.reverse()
    return final_list

print(add_to_array_from_integer([1, 2, 0, 0], 34))

