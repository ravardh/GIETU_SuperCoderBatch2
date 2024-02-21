def selectionSort(array, size):
   for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])
         
data =eval(input("enter the numbers"))
size = len(data)
selectionSort(data, size)
print('Sorted Array using selection sort:')
print(data)
