#Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = input("Enter elements of the list separated by space: ").split()
arr = [int(x) for x in arr]

bubble_sort(arr)

print("Bubble sorted array is:", *arr)
