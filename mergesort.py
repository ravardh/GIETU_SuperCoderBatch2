def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    
    # Compare elements of left and right subarrays and merge them
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    
    # Append remaining elements from left and right arrays (if any)
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    
    return result

# Example usage:
arr = [5, 3, 8, 2, 1, 7, 4]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # Output: [1, 2, 3, 4, 5, 7, 8]
