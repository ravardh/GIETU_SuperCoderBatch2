def selection_sort(ary):
    n = len(ary)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if ary[j] < ary[min_index]:
                min_index = j
        ary[i], ary[min_index] = ary[min_index], ary[i]
    return ary

ary = [36, 8, 87, 19, 7]
res = selection_sort(ary)
print("Sorted array is:", res)
