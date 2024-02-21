def insertion(l):
    n=len(l)
    if n<=1:
        return
    for i in range(1,n):
        k=l[i]
        j=i-1
        while j>=0 and k<l[j]:
            l[j+1]=l[j]
            j-=1
        l[j+1]=k

lst=[]
n=int(input("Enter the no. of elements: "))
print("Enter elements")
for i in range(n):
    ele=int(input())
    lst.append(ele)

insertion(lst)
print("Sorted array:")
print(lst)
