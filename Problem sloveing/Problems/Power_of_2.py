def power_of_two(num):
    if num == 1 or num == 2:
        return True
    else:
        while num > 2:
            num = num / 2
            if num == 2:
                return True
        return False

import math
def power_of_two_1(num):
    if num == 0 or num < 1:
        return False
    return math.ceil(math.log2(num)) == math.floor(math.log2(num))

def power_of_two_2(num):
    if num <= 0:
        return False
    return (num & (num - 1)) == 0

print(power_of_two_2(256))
