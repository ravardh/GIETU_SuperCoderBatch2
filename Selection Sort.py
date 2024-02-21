def selection_sort(arr, n):
	for i in range(n):
		min = i
		for j in range(i+1, n):
			if arr[j] < arr[min]:
				min = j

		arr[i], arr[min] = arr[min], arr[i]


arr=eval(input("Enter the array :"))
size=len(arr)

selection_sort(arr, size)
print("Sorted array is:",end=" ")
for i in range(size):
	print(arr[i],end=" ")