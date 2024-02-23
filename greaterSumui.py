nums = list(map(int, input("Enter numbers separated by space: ").split()))
n = int(input("Enter nnumber of elements to add: "))

if n > len(nums):
    print("Invalid input: n is greater than the length of the list")
else:
    maxSum = sum(nums[:n])
    for i in range(len(nums) - n + 1):
        curSum = sum(nums[i:i+n])
        maxSum = max(maxSum, curSum)

    print(maxSum)
