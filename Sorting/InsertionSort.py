#Insertion Sort
n=int(input("enter the no of element:-"))
arr=[]
for i in range (0,n):
    arr.append(int(input()))
print("Before sorting:",arr)
for i in range(0,n):
    pos=i
    min=arr[i]
    for j in range (i,n):
        if (min>arr[j]):
            min=arr[j]
            pos=j
    arr[pos],arr[i]=arr[i],arr[pos]
print("After Sorting:-",arr)