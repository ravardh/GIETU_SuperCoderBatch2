# Bubble sort in Python

def bubbleSort(array):
    
  for i in range(len(array)):

    for j in range(0, len(array) - i - 1):

      if array[j] > array[j + 1]:

        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


'''data = [-2, 45, 0, 11, -9]
bubbleSort(data)
print('Sorted Array in Ascending Order:')
print(data)'''

arr=[]
n=int(input("Enter the no of array elements:"))
print("Enter the elements:")
for i in range(0,n):
	arr.append(int(input()))
print("unsorted array")
print(arr)
bubbleSort(arr)
print('Sorted Array in Ascending Order:')
print(arr)