def selectionSort(element):
  for i in range(num):
    for j in range(i+1,num):
      if(element[i]>element[j]):
        element[i],element[j]=element[j],element[i]
element=[]
num=int(input("Enter the number of elements:"))
for i in range(num):
  element.append(int(input("Enter the number:")))
print("Before Sorting:",element)
selectionSort(element)
print("After Sorting:",element)