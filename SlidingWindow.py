arr=[1,3,5,2,7,4,8,9,5,3,5,7,9,3,2,0]
i = 0
j = 0
sum = 0
maxi = 0
k = int(input("Enter the value of k: "))
while j < len(arr):
    sum += arr[j]
    if j - i + 1 == k:
        maxi = max(maxi, sum)
    elif j - i + 1 > k:
        while j - i + 1 > k:
            sum -= arr[i]
            i += 1

        if j - i + 1 == k:
            maxi = max(maxi, sum)
    j += 1

print(maxi)