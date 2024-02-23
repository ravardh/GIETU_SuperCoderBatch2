# Time  Complexity of n^2
a=[1,3,5,2,7,4,8,9,5,4]
c=int(input("Enter Window Size:"))
b=0
for i in range(len(a)-(c-1)):
  s=0
  p=j=i
  while j<=p+(c-1):
    s=s+a[j]
    j+=1
  print(s,end=" ")
  if s>b:
    b=s
print("||",b)


# Time Complexity with n
a=[1,3,5,2,7,4,8,9,5,4]
c=int(input("Enter Window Size:"))
max=0
for i in range(0,c):
  max+=a[i]
  w=max
for i in range(0,len(a)-c):
  if(max<w):
    max=w
  w=w+a[i+c]-a[i]
print(max)