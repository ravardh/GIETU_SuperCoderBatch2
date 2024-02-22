# 4 8 7 1 9 2 3 6 5
def partition(arr,l,h):
    pivot = arr[h]
    i = l-1
    for j in range(l,h):
        if(arr[j] <= pivot):
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return i+1

def quick(arr,l,r):
    if l < r:
        pi = partition(arr,l,r)
        quick(arr,l,pi-1)
        quick(arr,pi+1,r)

arr = list(map(int,input().split()))
n = len(arr)
quick(arr,0,n-1)
print(arr)
