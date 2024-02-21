# Insertion sort in Python
def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
               
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        array[j + 1] = key


'''data = [9, 5, 1, 4, 3]
print("Unsorted Array:")
print(data)
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)'''

arr=[]
n=int(input("Enter the no of array elements:"))
print("Enter the elements:")
for i in range(0,n):
	arr.append(int(input()))
print("unsorted array")
print(arr)
insertionSort(arr)
print('Sorted Array in Ascending Order:')
print(arr)