def partition(arr,start,end):
    pivot=arr[end]
    j=start-1
    for i in range(start,end):
        if(arr[i]<=pivot):
            j+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[j + 1], arr[end] = arr[end], arr[j + 1]
    return j+1

def quicksort(arr,start,end):
    if start<end:
        pi=partition(arr,start,end)
        quicksort(arr,start,pi-1)
        quicksort(arr,pi+1,end)

n=int(input("Enter the range of numbers: "))
data=[]
for i in range(0, n):
    ele = int(input())
    data.append(ele)
print("Unsorted Array")
print(data)
size = len(data)
quicksort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)