def insertion_sort(ary):
    for i in range(1, len(ary)):
        key = ary[i]
        j = i - 1
        while j >= 0 and key < ary[j]:
            ary[j + 1] = ary[j]
            j -= 1
        ary[j + 1] = key

ary = [8, 1, 31, 12, 45]
insertion_sort(ary)
print("Sorted array is:", ary)
