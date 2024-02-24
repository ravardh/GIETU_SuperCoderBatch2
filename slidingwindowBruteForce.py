arr= [1,3,5,2,7,4,8,9,5,3,5,7,9,3,2,0]
n=int(input("Enter the consecutive number"))
l=len(arr)
sum=0
for i in range(0,n):
    sum+=arr[i]
win = sum
for i in range(0,l-n):
    if(win>sum):
        sum = win
    win-=arr[i]+arr[i+n]
print(sum)