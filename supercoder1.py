a=[1,2,4,7,4,3,8,7,9,6,4,9,5,7,9,3,1,5]
l=len(a)
ans=0
new=[]
for x in range(l-2):
    sum=a[x]+a[x+1]+a[x+2]
    print(sum)
    if(sum>ans):
       new.clear()
       new.append(a[x])
       new.append(a[x+1]) 
       new.append(a[x+2])  
    ans=max(ans,sum)
print("ANS = ",ans)
print(new)
