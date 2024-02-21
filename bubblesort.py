def bubblesort(l):
    n=len(l)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
		
lst=[]
n=int(input("enter the no. of elements"))
print("Enter elements")
for i in range(n):
    ele=int(input())
    lst.append(ele)
    
bubblesort(lst)
print("Sorted array:")
for i in range(len(lst)):
    print("%d"%lst[i],end=" ")
