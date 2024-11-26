def palindrome(num):
    num_str = str(num)
    l, r = 0, len(num_str) - 1
    while l < r:
        if num_str[l] == num_str[r]:
            l += 1
            r -= 1
        else:
            return False
    return True

def palindrome_1(num):
    if num < 0:
        return False
    reverse = 0
    num_copy = num
    while num > 0:
        reverse = (reverse * 10) + (num % 10)
        num //= 10
    return reverse == num_copy

number = int(input("Enter the number for palindrome check: "))
print(palindrome_1(number))
