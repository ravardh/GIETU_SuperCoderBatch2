def selectionsort(l,n):
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if l[j]<l[min_index]:
                min_index=j
        (l[i],l[min_index])=(l[min_index],l[i])
 
lst=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    ele=int(input("Enter element: "))
    lst.append(ele)
n=len(lst)
selectionsort(lst,n)
print('The array after sorting:')
print(lst)
