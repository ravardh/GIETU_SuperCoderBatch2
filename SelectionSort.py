def Selection_Sort(arr,n):
    for i in range(0,n):
        min=i
       
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
        (arr[i],arr[min])=(arr[min],arr[i])
        
arr=[2,1,5,7,34,21,11,10]
n=len(arr)
Selection_Sort(arr,n)

print("The sorted array is :")
print(arr)

                