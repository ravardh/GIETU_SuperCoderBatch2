
a=[1,3,5,2,7,4,8,9,5,3,5,7,9,3,2,0]
n=len(a)
max=0
k=int(input())
for i in range(0,n-k):
  sum=0
  for j in range(i,k+i):
    sum=sum+a[j]
    if(max<sum):
       max=sum
print(max)






a=[1,3,5,2,7,4,8,9,5,3,5,7,9,3,2,0]
sum=0
sl=[]
l=len(a)
for i in range(0,l-2):
  sum=a[i]+a[i+1]+a[i+2]
  sl.append(sum)
print(max(sl))






a=[]
n=int(input())
k=int(input())
for x in range(0,n):
  ele=int(input())
  a.append(ele)
lt=len(a)
for i in range(0,n-k+1):
  b=[]
  for j in range(i,k+i):
    b.append(a[j])
  print(b)
  print(max(b))
