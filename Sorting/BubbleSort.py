#Bubble Sort
n=int(input("enter the no of element:-"))
arr=[]
for i in range (0,n):
    arr.append(int(input()))
print("Before sorting:",arr)
for i in range(0,n):
    flag=0
    for j in range (0,n-i-1):
        if(arr[j]>arr[j+1]):
            arr[j+1],arr[j]=arr[j],arr[j+1]
            flag=1
    if(flag==0):
        break
print("After Sorting",arr)
