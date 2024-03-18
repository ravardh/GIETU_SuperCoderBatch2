a=list(map(int,input("ENTER NUMBERS ").split()))
k=int(input("Enter Size of window"))
print(a)
sum=0
max=0
for  i in range(k):
    sum=sum+a[i]
max=sum
for i in range(k,len(a)):
    sum=sum-a[i-k]
    sum=sum+a[i]
    if(sum>max):
        max=sum
print(max)

