#Bubble sort
lst=[]
a=int(input("enter the length"))
for k in range(a):
    l=int(input())
    lst.append(l)   
    print(lst) 
for j in range(a):
    for i in range(0,a-j-1):
         if(lst[i]>lst[i+1]):
             (lst[i],lst[i+1])=(lst[i+1],lst[i])
             print(lst)