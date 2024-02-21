def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == "__main__":
    try:
        size = int(input("Enter the size of the list: "))
        if size <= 0:
            print("Please enter a positive integer.")
        else:
            user_list = []
            for i in range(size):
                user_list.append(int(input(f"Enter element {i+1}: ")))
            
            print("\nOriginal list:", user_list)
            selection_sort(user_list)
            print("Sorted list:", user_list)
    except ValueError:
        print("Invalid input!.")
