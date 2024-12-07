# Two sum - Leet code 1
def two_sum(input_list, target):
    visited = {}
    for i, val in enumerate(input_list):
        value = target - val
        if value in visited:
            return i, visited[value]
        visited[val] = i

# my_list = [2,7,11,15]
# print(two_sum(my_list, 9))

# Best Time to Buy and Sell Stock - Leet code 121
def best_time_to_buy_or_sell_stocks(input_list):
    min_value = float('-inf')
    max_profit = 0
    for i in input_list:
        if i < min_value:
            min_value = i
        profit = i - min_value
        if profit > max_profit:
                max_profit = profit
    return max_profit

# my_list = [7,6,4,3,1]
# print(best_time_to_buy_or_sell_stocks(my_list))

# Contains Duplicate - Leet code 217
def contain_duplicate(input_list):
    unique = set()
    for i in input_list:
        if i not in unique:
            unique.add(i)
        else:
            return True
    return False

# my_list = [1,2,3,4]
# print(contain_duplicate(my_list))

# Contains Duplicate II - Leet code 219
def contain_duplicate_2(input_list, k):
    visited = {}
    for i, val in enumerate(input_list):
        if input_list[i] in visited:
            target = i - visited[val]
            if target <= k:
                return True
        visited[val] = i
    return False

# my_list = [1,2,3,1,2,3]
# print(contain_duplicate_2(my_list, 2))

# Product of Array Except Self - Leet code 238
def product_of_array_expect_self(input_list):
    n = len(input_list)
    l_index = 1
    r_index = 1
    l_array = [0] * n
    r_array = [0] * n
    for i in range(n):
        j = -i - 1
        l_array[i] = l_index
        r_array[j] = r_index
        l_index *= input_list[i]
        r_index *= input_list[j]
    return [l * r for l, r in zip(l_array, r_array)]

# my_input = [1, 2, 3, 4]
# print(product_of_array_expect_self(my_input))

# Maximum Subarray - Leet code 53
def max_sum_subarray(input_list):
    max_sum = float('-inf')
    current_sum = 0
    for i in range(len(input_list)):
        current_sum += input_list[i]
        max_sum = max(current_sum, max_sum)
        if current_sum < 0:
            current_sum = 0
    return max_sum

# my_array = [-2]
# print(max_sum_subarray(my_array))

# Maximum Product Subarray - Leet code 152
def max_product_subarray(input_list):
    max_prod = max(input_list)
    cur_max, cur_min = 1, 1
    for i in input_list:
        temp = cur_max * i
        cur_max = max(i * cur_max, i * cur_min , i)
        cur_min = min(temp, i * cur_min , i)
        max_prod = max(cur_max, max_prod)
    return max_prod

def maxProduct(A):
    B = A[::-1]
    for i in range(1, len(A)):
        A[i] *= A[i - 1] or 1
        B[i] *= B[i - 1] or 1
    return max(A + B)

# my_input = [1, 3, -3, 1]
# print(maxProduct(my_input))

# Find Minimum in Rotated Sorted Array - Leet code 153
def find_min_in_rotated_sorted_array(input_list):
    n = len(input_list)
    l = 0
    r = n - 1
    while l < r:
        m = (l + r) // 2
        if input_list[m] > input_list[r]:
            l = m + 1
        else:
            r = m
    return input_list[l]

# my_input = [3, 4, 5, 0, 1, 2]
# print(find_min_in_rotated_sorted_array(my_input))

# Search in Rotated Sorted Array - Leet code 33
def search_in_rotated_sorted_array(input_list, target):
    n = len(input_list)
    l = 0
    r = n - 1
    while l < r:
        m = (l + r) // 2
        if input_list[m] > input_list[r]:
            l = m + 1
        else:
            r = m
    min_index = l
    if target > input_list[l]:
        s, e = 0, min_index
    else:
        s, e = min_index, r

    while s <= e:
        m = (s + e) // 2
        if input_list[m] > target:
            r = m - 1
        elif input_list[m] < target:
            l = m + 1
        else:
            return m
    return "element not found"

# my_input = [3, 4, 5, 6, 7, 8, 0, 1, 2]
# print(search_in_rotated_sorted_array(my_input, 6))

# Two Sum II - Input Array Is Sorted - Leet code 167
def two_sum_2(input_list, target):
    visited = {}
    for i, val in enumerate(input_list):
        value = target - val
        if value in visited:
            return list((visited[value] + 1, i + 1))
        visited[val] = i

# my_input = [2,7,11,15]
# print(two_sum_2(my_input, 9))


# Three Sum - Leet code 15
def three_sum(input_list):
    h = {}
    n = len(input_list)
    s = set()
    for i, val in enumerate(input_list):
        h[val] = i
    for i in range(n):
        for j in range(i + 1, n):
            desired = -input_list[i] -input_list[j]
            if desired in h and h[desired] != i and h[desired] != j:
                s.add(tuple(sorted((desired, input_list[i], input_list[j]))))
    return s

# my_input = [-1,0,1,2,-1,-4]
# print(three_sum(my_input))

# Container With Most Water - Leet code 11
def container_with_most_water(input_list):
    max_area = 0
    n = len(input_list)
    i = 0
    j = len(input_list) - 1
    for k in range(n):
        if input_list[i] > input_list[j]:
            area = input_list[j] * (j - i)
            j -= 1
        else:
            area = input_list[i] * (j - i)
            i += 1
        if area > max_area:
            max_area = area
    return max_area

my_input = [8, 7, 2, 1]
print(container_with_most_water(my_input))

# Verifying an Alien Dictionary - Leet code 953
def verify_alien_dictionary(words, order):
    order_dict = {}
    for i, val in enumerate(order):
        order_dict[val] = i
    for word in words:
        word_count = [[dict[x] for x in word]]

word = ["hello","leetcode"]
rder = "hlabcdefgijkmnopqrstuvwxyz"
print(verify_alien_dictionary(word, rder))
# Next Permutation - Leet code 31
# Remove Duplicates from Sorted Array - Leet code 26
# Find First and Last Position of Element in Sorted Array - Leet code - 34
# Trapping Rain Water - Leet code 42
# Median of Two Sorted Arrays - Leet code 4