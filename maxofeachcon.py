N=int(input("Enter Num of element in the list"))
L=list(eval(input()))
l1=[]
K=int(input("Enter the num"))
L=[1,2,3,4,5,6,7,8]
for i in range(N-K+1):
    #print(max(L[i:i+K]))
    l1.append(max(L[i:i+K]))

for i in l1:
    print(i)
