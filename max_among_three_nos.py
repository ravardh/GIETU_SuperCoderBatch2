def find_max_sum_triplet(arr):
    n = len(arr)
    max_sum = float('-inf')
    max_triplet = []
    for i in range(n - 2):
        current_sum = arr[i] + arr[i + 1] + arr[i + 2]
        if current_sum > max_sum:
            max_sum = current_sum
            max_triplet = [arr[i], arr[i + 1], arr[i + 2]] 
    return max_triplet
try:
    arr = list(map(int, input("Enter space-separated numbers: ").split()))
result = find_max_sum_triplet(arr)
if result:
    print("Three consecutive numbers with maximum summation value:", result)
else:
    print("Array should have at least three elements.")
