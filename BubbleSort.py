arr=[5,3,4,2,7,1]

for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]>arr[j]):
            arr[j],arr[i]=arr[i],arr[j]

print(arr)