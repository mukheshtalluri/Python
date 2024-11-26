def fibonacci_series(num):
    fibo_series = [0, 1]
    for i in range(2, num):
        fibo_series.append(fibo_series[i - 1] + fibo_series[i - 2])
    print(fibo_series)

def fibonacci_series_1(num):
    a, b = 0, 1
    for i in range(num):
        print(a, end = " ")
        c = a + b
        a = b
        b = c

def fibonacci_series_2(num):
    if num in [0, 1]:
        return num
    return fibonacci_series_2(num - 1) + fibonacci_series_2(num - 2)

for i in range(11):
    print(fibonacci_series_2(i), end = " ")

