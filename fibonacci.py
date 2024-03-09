def fibo(t,l):
  if t==0 or t==1:
    l[t]=t
    return t
  if l[t]!=-1:
    return l[t]
  else:
    return fibo(t-1,l)+fibo(t-2,l)
l=[-1,-1,-1,-1,-1,-1,-1,-1]
for i in range(8):
  print(fibo(i,l),end=" ")