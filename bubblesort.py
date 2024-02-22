def bubble_sort(arr):
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j]>arr[j+1]:
                swapped= True
                arr[j], arr[j+1]=arr[j+1], arr[j]

        if not swapped:
            return
arr=[1,34,23,8,6]

bubble_sort(arr)
print("the sorted arr is: ")
for i in range(len(arr)):

  print("%d"% arr[i] , end=" ")
