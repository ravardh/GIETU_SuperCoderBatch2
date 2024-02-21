def insertionSort(element):
  for i in range(1,num):
    j=i-1
    while j>=0 and element[j]>element[j+1]:
      element[j],element[j+1]=element[j+1],element[j]
      j=j-1
element=[]
num=int(input("Enter the number of elements:"))
for i in range(num):
  element.append(int(input("Enter the number:")))
print("Before Sorting:",element)
insertionSort(element)
print("After Sorting:",element)