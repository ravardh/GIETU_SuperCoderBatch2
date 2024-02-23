l=[9,1,0,3,5,2,7,8,1,4,5,6]
n=len(l)
k=int(input("Enter a number"))
m=0
for i in range(k):
    m += l[i]
    w=m
for i in range(0,n-k):
    if(m < w):
        m=w
    w+=l[i+k]-l[i]
print(m)

