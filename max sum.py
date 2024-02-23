a = [1,3,5,7,9,4,8,5,6,3,4,2,0,5]
sum = 0
for i in a:
    if (a[i]+a[i+1]+a[i+2]>sum):
        sum = a[i]+a[i+1]+a[i+2]
    i+=1
print(sum)