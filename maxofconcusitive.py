a = [1, 2, 3, 1, 4, 5, 6, 8, 9, 6, 4, 6, 0, 4]
k = int(input('Enter the number of consecutive numbers: '))

if  k > len(a):
    print("invalid input.")
else:
    sum1 = []

    for i in range(len(a) - (k - 1)):
        current_sum = sum(a[i:i + k])
        sum1.append(current_sum)

    max_sum = max(sum1)
    max_index = sum1.index(max_sum)

    print("Maximum sum:", max_sum)
    print("Consecutive numbers:", a[max_index:max_index + k])
