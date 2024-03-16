def merge(array, start, mid, end):
    left_array=array[start:mid+1]
    right_array=array[mid+1:end+1]
    i=j=0
    k=start
    while i<len(left_array) and j<len(right_array):
        if left_array[i]<=right_array[j]:
            array[k]=left_array[i]
            i+=1
        else:
            array[k]=right_array[j]
            j+=1
        k+=1
    while i<len(left_array):
        array[k]=left_array[i]
        i+=1
        k+=1
    while j<len(right_array):
        array[k]=right_array[j]
        j+=1
        k+=1
def merge_sort(array,start,end):
    if start<end:
        mid=(start+end)//2
        merge_sort(array,start,mid)
        merge_sort(array,mid+1,end)
        merge(array,start,mid,end)

n=int(input("Enter the number of elements: "))
array=[]
for i in range(n):
    array.append(int(input(f"Enter element {i+1}: ")))
print("Before Sorting:",array)
merge_sort(array,0,n-1)
print("After Sorting:",array)