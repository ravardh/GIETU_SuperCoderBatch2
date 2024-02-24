
def bubblesort():
    arr=[]
    for i in range(5):
       arr.append(int(input()))
    for j in range(5):
        for i in range(5-j-1):
            if(arr[i]>arr[i+1]):
                arr[i],arr[i+1]=arr[i+1],arr[i]
    print("sorted array:")
    for i in range(5):
        print(arr[i])
bubblesort()
    