def partition(element,low,high):
  pi=element[high]
  j=low-1
  for i in range(low,high+1):
    if element[i]<pi:
      j+=1
      element[j],element[i]=element[i],element[j]
  element[j+1],element[high]=element[high],element[j+1]
  return j+1
    
def Quicksort(element,low,high):
  if low<high:
    pi=partition(element,low,high)
    Quicksort(element,low,pi-1)
    Quicksort(element,pi+1,high)

element=[]
num=int(input("Enter the number of elements:"))
for i in range(num):
  element.append(int(input("Enter the number:")))
print("Before Sorting:",element)
Quicksort(element,0,num-1)
print("After Sorting",element)
