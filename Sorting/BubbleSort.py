#Bubble Sort
n=int(input("enter the no of element:-"))
arr=[]
for i in range (0,n):
    arr.append(int(input()))
print("Before sorting:",arr)
for i in range(0,n):
    for j in range (i+1,n):
        if(arr[i]>arr[j]):
            arr[i],arr[j]=arr[j],arr[i]
print("After Sorting",arr)