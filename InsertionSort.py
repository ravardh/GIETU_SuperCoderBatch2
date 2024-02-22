arr = [3, 4, 8, 1, 9, 2, 4]

for i in range(1,len(arr)):
    index=i
    for j in range(index,0,-1):
        if(arr[j]<arr[j-1]):
            arr[j-1],arr[j]=arr[j],arr[j-1]
        else:
            break

print(arr)

