def insertionSort(arr):
    n = len(arr)
    if n <= 1:
        return
    for i in range(1,n):
        k=arr[i]
        j=i-1
        while j>=0 and k<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=k

arr=[]
n=int(input("Enter the number of elements "))
for i in range(n):
    ele = int(input())
    arr.append(ele)

insertionSort(arr)
print("Sorted array")
print(arr)