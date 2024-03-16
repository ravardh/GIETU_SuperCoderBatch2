
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[i + j] = left_half[i]
                i += 1
            else:
                arr[i + j] = right_half[j]
                j += 1
        while i < len(left_half):
            arr[i + j] = left_half[i]
            i += 1
        while j < len(right_half):
            arr[i + j] = right_half[j]
            j += 1
my_list = [38, 27, 43, 3, 9, 82, 10]
merge_sort(my_list)
print("Sorted list:", my_list)

