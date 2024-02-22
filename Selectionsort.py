def selection_Sort(array, n):
    for i in range(n):
        min_ind = i
        for j in range(i + 1, n):
            if array[j] < array[min_ind]:
                min_ind = j
        (array[i], array[min_ind]) = (array[min_ind], array[i])
array = [-2, 4, -89, 56, 9]
n = len(array)
selection_Sort(array, n)
print('The sorted array is:')
print(array)

