def partion(arr,l,h):
    pivot=arr[h]
    j=l-1
    for i in range(0,h):
        if(arr[i]<=pivot):
            j+=1
            arr[j],arr[i]=arr[i],arr[j]
    arr[j+1],arr[h]=arr[h],arr[j+1]
    return i+1
def quicksort(arr,l,h):
    if l<h:
        p=partion(arr,l,h)
        quicksort(arr,l,p-1)
        quicksort(arr,p+1,h)
n=int(input())
arr = list(map(int,input().split()))
quicksort(arr,0,n-1)
print(arr)