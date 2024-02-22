'''a=[1,3,5,2,7,4,8,9,5,3,5,7,9,3,2,0]
max=0

for i in range(len(a)-2):
    sum=a[i]+a[i+1]+a[i+2]
    if(sum>max):
        max=sum
print(max)'''

# Taking user input
a=[1,3,5,2,7,4,8,9,5,3,5,7,9,3,2,0]
#a=[3,5,7,1,5,8,7,9]
add=0
max=0
num=int(input("enter the no."))
for i in range(len(a)-num+1):
    for j in range(num):
        
        add=a[i+j]+add
    if(add>max):
        max=add
    add=0
print(max)
               