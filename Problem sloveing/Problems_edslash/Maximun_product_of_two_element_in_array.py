def max_product(input_list):
    max1, max2 = 0, 0
    for i in input_list:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2:
            max2 = i
    return max1 * max2

my_list = [3, 7, 9, 2, 5]
print(max_product(my_list))
