# Calculator
queries = int(input("Enter the number of queries: "))
while (queries):
    x, y = map(int, input("Enter two numbers: ").split())
    operator = input("Enter the operator: ")
    match operator:
        case '+': print(x + y)
        case '-': print(x - y)
        case '*': print(x * y)
        case '/': print(x / y)
        case '%': print(x % y)
        case _: print("Invalid Operator!")
    queries -= 1

# Selection Sort
arr = list(map(int, input("Enter the array: ").split()))
for i in range(len(arr) - 1):
    min_idx = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print("Sorted Array:", arr)