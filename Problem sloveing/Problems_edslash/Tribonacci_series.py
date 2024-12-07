def tribonacci_series(num):
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    dp = [0, 1, 1]
    for i in range(3, num + 1):
        dp.append(dp[i - 3] + dp[i - 2] + dp[i - 1])
    return dp[num]

print(tribonacci_series(4))
