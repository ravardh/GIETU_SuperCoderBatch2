a=[1,3,5,2,7,4,8,9,5,3,5,7,9,3,2,0]
k=int(input())
max=window=0
for i in range(0,k):
    max=max+a[i]
    window=max
for i in range(0,len(a)-k):
    if(max<window):
        max=window
    window=window+a[i+k]-a[i]
print(max)