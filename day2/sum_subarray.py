arr=[]
n=int(input())
for i in range(n):
    ele=int(input())
    arr.append(ele)
max=0
k=int(input())

for i in range(len(arr)-k+1):
    for j in range(k):
        
        if(max<arr[i+j]):
            max=arr[i+j]
    print(max)
    max=0
