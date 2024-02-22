# 4 8 7 1 9 2 3 6 5
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        la = arr[:mid]
        ra = arr[mid:]
        mergeSort(la)
        mergeSort(ra)
        i = j = k = 0
        while(i<len(la) and j<len(ra)):
            if(la[i] <= ra[j]):
                arr[k] = la[i]
                i+=1
            else:
                arr[k] = ra[j]
                j+=1
            k+=1
        if(i<len(la)):
            while(i<len(la)):
                arr[k] = la[i]
                i+=1
                k+=1
        if(j<len(ra)):
            while(j<len(ra)):
                arr[k] = ra[j]
                j+=1
                k+=1

arr = list(map(int,input().split()))
n = len(arr)
mergeSort(arr)
print(arr)