items=[0,1,2,3,4,5,6]
price=[10,5,15,7,6,18,3]
weight=[2,3,5,7,1,4,1]
capacity=15
rows=len(items)
columns =capacity+1
arr=[[0 for _ in range(columns)] for _ in range(rows)]
for i in range(rows):
    for w in range(columns):
            arr[i][w]=max(arr[i-1][w],arr[i-1][w-weight[i]]+price[i])
print("The maximum capacity is:-",arr[rows-1][columns-1])

def fibo(l1,n):
    l1[0]=0
    l1[1]=1
    for i in range(2,len(l1)):
        l1[i]=l1[i-1]+l1[i-2]
    return l1


n=int(input())
l1=[i for i in range(n)]
result=fibo(l1,n)
print(result)

def fibbo(term,L):
  if term==0 or term==1:
    L[term]=term
    return term
  if L[term]!=-1:
    return l[term]
  else:
    return fibbo(term-1,L)+fibbo(term-2,L)
L=[-1,-1,-1,-1,-1,-1,-1,-1]
for i in range(8):
  print(fibbo(i,L),end=" ")