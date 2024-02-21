def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

if __name__ == "__main__":
    try:
        user_list = list(map(int, input("Enter the elements : ").split()))
        print("\nOriginal list:", user_list)
        insertion_sort(user_list)
        print("Sorted list:", user_list)
    except ValueError:
        print("Invalid input! .")
