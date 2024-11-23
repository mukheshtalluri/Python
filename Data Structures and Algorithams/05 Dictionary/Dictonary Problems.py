def word_frequency(input_list):
    word_count = {}
    for i in input_list:
        if i not in word_count:
            word_count[i] = 1
        else:
            word_count[i] += 1
    print(word_count)

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
#word_frequency(words) # Time complexity - O(n) and Space complexity - O(m)

def common_keys(dict1, dict2):
    for i, val in dict2.items():
        if i not in dict1:
            dict1[i] = val
        else:
            dict1[i] += val
    print(dict1)

a = {'a': 1, 'b': 2, 'c': 3}
b = {'b': 3, 'c': 4, 'd': 5}
#common_keys(a, b) # Time complexity - O(n) and Space complexity - O(1)

def key_with_highest_value(dict):
    max_value = 0
    key = None
    for i in dict:
        if dict[i] > max_value:
            max_value = dict[i]
            key = i
    print(key)

keys = {'a': 1, 'b': 9, 'c': 3}
#key_with_highest_value(keys) # Time complexity - O(n) and Space complexity - O(1)

def reverse_key_value_pairs(dict):
    new_dict = {}
    for i, val in dict.items():
        new_dict[val] = i
    #print(new_dict)
    print({v: k for k, v in dict.items()})

dict_key_values = {'a': 1, 'b': 9, 'c': 3}
#reverse_key_value_pairs(dict_key_values) # Time complexity - O(n) and Space complexity - O(n)

def filtered_data(dict):
    print({i : val} for i, val in dict.items() if val % 2 == 0)

dict_1 = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7}
filtered_data(dict_1)




