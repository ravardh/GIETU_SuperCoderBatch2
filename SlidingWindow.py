a=[1,3,5,2,7,4,3,5,7,9,3,2,0,8,9,5]
ni=int(input())
s=0
for i in range(0,ni):
    s=s+a[i]
sumn=s   
for i in range(0,len(a)-ni):
  #a1=a[i:(i+ni)]
  #sumn=sum(a1)
  # for j in range(0,ni):
  #   sumn=sumn+a[i+j]
  if(sumn > s):
    s=sumn    
  sumn=sumn-a[i]+a[i+ni]

print(s)

