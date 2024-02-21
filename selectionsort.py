# Selection sort in Python

def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            if array[i] < array[min_idx]:
                min_idx = i
         
        (array[step], array[min_idx]) = (array[min_idx], array[step])


'''data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)'''

arr=[]
n=int(input("Enter the no of array elements:"))
print("Enter the elements:")
for i in range(0,n):
	arr.append(int(input()))
print("unsorted array")
print(arr)
size = len(arr)
selectionSort(arr, size)
print('Sorted Array in Ascending Order:')
print(arr)