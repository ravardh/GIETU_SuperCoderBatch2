def bubble_sort(ary):
    n = len(ary)
    for i in range(n):
        for j in range(0, n-i-1):
            if ary[j] > ary[j+1]:
                ary[j], ary[j+1] = ary[j+1], ary[j]

ary = [25, 78, 13, 9, 40, 1]
bubble_sort(ary)
print("Sorted array is:", ary)
