def partition(arr,start,end):
    pivot=arr[end]
    j=start-1
    for i in range(start,end):
        if(arr[i]<=pivot):
            j+=1
            arr[i],arr[j]=arr[j],arr[i]
    j+=1
    arr[j],arr[end]=arr[end],arr[j]
    return j

def quicksort(arr,start,end):
    if start<end:
        pi=partition(arr,start,end)
        quicksort(arr,start,pi-1)
        quicksort(arr,pi+1,end)

n=int(input("Enter the range of numbers: "))
lst=[]
for i in range(0, n):
    ele=int(input())
    lst.append(ele)
print("Unsorted Array")
print(lst)
quicksort(lst,0,n-1)
print('Sorted Array in Ascending Order:')
print(lst)
