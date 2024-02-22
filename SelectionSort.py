arr = [3, 4, 8, 1, 9, 2, 4]

for i in range(0, len(arr)):
    minIndex = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[minIndex]:
            minIndex = j

    arr[i], arr[minIndex] = arr[minIndex], arr[i]

print(arr)
