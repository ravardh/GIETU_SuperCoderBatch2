def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


if __name__ == "__main__":
    try:
        user_list = list(map(int, input("Enter the elements  ").split()))
        print("\nOriginal list:", user_list)
        bubble_sort(user_list)
        print("Sorted list:", user_list)
    except ValueError:
        print("Invalid input! ")
