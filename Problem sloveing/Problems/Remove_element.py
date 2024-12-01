def remove_element(nums, val):
    i = 0
    n = len(nums)

    while i < n:
        if nums[i] == val:
            nums[i] = nums[n - 1]
            n -= 1
        else:
            i += 1
    return n

def remove_element_1(nums, val):
    if len(nums) == 0:
        return 0
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

my_input = [3, 2, 2, 3]
print(remove_element_1(my_input, 3))