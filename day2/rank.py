a=[1,3,5,2,7,4,8,9,5,3,5,7,9,3,2,0]
#a=[3,5,7,1,5,8,7,9]
sun=0
max=0
n=int(input("enter the no."))

for i in range(len(a)-n+1):
    for j in range(n):
        
        sun=a[i+j]+sun
    if(sun>max):
        max=sun
    sun=0
print(max)
    