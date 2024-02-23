def part(arr,st,end):
    pi=arr[end]
    i=st-1
    for j in range(st,end):
        if(pi>arr[j]):
            i+=1
            (arr[j],arr[i])=(arr[i],arr[j])
            
    (arr[i+1],arr[end])=(arr[end],arr[i+1])
    return i+1

def quick(arr, st, end):
    if st < end:
        pi = part(arr, st, end)
        quick(arr, st, pi - 1)
        quick(arr, pi + 1, end)

if __name__ == '__main__':
    arr = []
    n = int(input("Enter size: "))
    for i in range(n):
        arr.append(int(input("Enter value: ")))
    quick(arr, 0, n - 1)
    print("Sorted array:")
    for i in arr:
        print(i, end=" ")