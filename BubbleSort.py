def bubbleSort(element):
  for i in range(1,num):
    for j in range(num-1):
      if element[j]>element[j+1]:
        element[j],element[j+1]=element[j+1],element[j]
element=[]
num=int(input("Enter the number of elements:"))
for i in range(num):
  element.append(int(input("Enter the number:")))
print("Before Sorting:",element)
bubbleSort(element)
print("After Sorting:",element)