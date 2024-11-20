# How may days temperature above the average temperature.
def average_temperature():
    no_of_days = int(input("How many days temperature you want to enter : "))
    temp_list = []
    for i in range(1, no_of_days + 1):
        temp_data = int(input(f"Enter day {i} temperature: "))
        temp_list.append(temp_data)
    average_temp = int(sum(temp_list) / len(temp_list))
    days_above_normal_temp = 0
    for i in temp_list:
        if i > average_temp:
            days_above_normal_temp += 1

    print(f"The average temperature : {average_temp}")
    print(f"{days_above_normal_temp} day's are above normal temperature.")

# average_temperature() # --> Time complexity and Space complexity - O(n)

# Find missing number from the sequence of numbers.
def missing_number(input_list, n):
    num_sum = n * ((n + 1) / 2)
    list_sum = sum(input_list)
    miss_num = int(num_sum - list_sum)
    print(miss_num)

my_input = [1, 2, 3, 4, 5, 7, 8]
# missing_number(my_input, 8) # Time complexity - O(n) and Space complexity - O(1)

def pair_sum(input_list, target):
    for i in range(len(input_list)):
        for j in range(len(input_list)):
            if input_list[i] + input_list[j] == target:
                print(i, j)

# pair_sum(my_input, 9) # Time complexity - O(n) and Space complexity - O(1)

# Search a number in the given list
def find_num(input_list, target):
    for i in input_list:
        if i == target:
            return "Value found."
    return "Value not found."

# print(find_num(my_input, 6)) # Time complexity - O(n) and Space complexity - O(1)

# Find maximum product of two integers in the given list
def max_product(input_list):
    max1, max2 = 0, 0
    for i in input_list:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2:
            max2 = i
    print(max1 * max2)

# max_product(my_input) # Time complexity - O(n) and Space complexity - O(1)

# Remove first and last elements from the list
def middle_elements_from_list(input_list):
    print(input_list[1:-1])

# middle_elements_from_list(my_input) # Time complexity - O(n) and Space complexity - O(n)

# Calculating the diagonal sum of the 2D list
def diagonal_sum(input_list):
    total = 0
    for i in range(len(input_list)):
        total += input_list[i][i]
    print(total)

my_input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# diagonal_sum(my_input) # Time complexity - O(n) and Space complexity - O(1)

# Find the top two best scores from the list
def find_best_two(input_list):
    max1, max2 = 0, 0
    for i in input_list:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2 and i != max1:
            max2 = i
    print(max1, max2)

# find_best_two(my_input) # Time complexity - O(n) and Space complexity - O(1)

# Remove duplicates from the list.
def remove_duplicates(input_list):
    #print(list(set(input_list))) # We can do like this but this will miss order of list since set is un order type.
    print(list(dict.fromkeys(input_list))) # This method will help us to maintain order as well.

my_list = [1, 1, 3, 2, 2, 4, 5, 4, 5]
#remove_duplicates(my_list)  # Time complexity - O(n) and Space complexity - O(n)

# Pair sum to the target element.
def pairs_sum(input_list, target):
    pairs = {}
    all_pairs = []
    for i in range(len(input_list)):
        value = target - input_list[i]
        if value in pairs:
            all_pairs.append(f"{value} + {input_list[i]}")
        pairs[input_list[i]] = i
    print(all_pairs)

#pairs_sum(my_input, 7) # Time complexity - O(n) and Space complexity - O(n)

# List containing duplicates
def contain_duplicate(input_list):
    unique_elements = set()
    for i in input_list:
        if i not in unique_elements:
            unique_elements.add(i)
        else:
            return True
    return False

# print(contain_duplicate(my_list)) # Time complexity - O(n) and Space complexity - O(n)

# Rotate matrix by 90 degrees.
def rotate_matrix(input_list):
    n = len(input_list)
    for i in range(n):
        for j in range(i, n):
            input_list[i][j], input_list[j][i] = input_list[j][i], input_list[i][j]
    print(input_list)
    for row in input_list:
        row.reverse()
    print(input_list)
#rotate_matrix(my_input) # Time complexity - O(n) and Space complexity - O(1)



