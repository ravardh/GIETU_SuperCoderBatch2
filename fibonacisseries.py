n = int(input('Enter the length of Fibonacci series: '))

fib_series = [0, 1]

while len(fib_series) < n:
    next_num = fib_series[-1] + fib_series[-2]
    fib_series.append(next_num)

print(fib_series)