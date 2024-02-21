def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1  
        
       
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  
        
    return arr

arr = [24, 36, 65, 42, 12, 10, 9]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)
