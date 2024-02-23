n = int(input("Enter the number of elements: "))
k = int(input("Enter the K value: "))
max_sum, rank = 0, 0

if n > k:
    a = []
    for i in range(0, n):
        a.append(int(input()))

    for i in range(0, k):
        max_sum += a[i]

    window_sum = max_sum

    for i in range(0, n - k + 1):
        if max_sum < window_sum:
            max_sum = window_sum
            rank = i

        if i + k < n:
            window_sum = window_sum + a[i + k] - a[i]

    print("The Grade is:", max_sum)
    print("The Rank is:", a[rank:rank + k])
else:
    print("Invalid input")
