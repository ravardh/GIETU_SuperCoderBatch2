lst=[1,3,5,2,7,4,8,9,5,3,5,7,9,3,2,0]
sum=0
max=0
x=int(input("enter the no."))
for i in range(len(lst)-x+1):
    for j in range(x):
        
        sum+=lst[i+j]
    if(sum>max):
        max=sum
    sum=0
print(max)
