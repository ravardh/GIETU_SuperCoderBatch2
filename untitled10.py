
ch=input();
a=int(input());
b=int(input());
match ch:
  case"+":
    print(a+b)
  case"-":
    print(a-b)
  case"*":
    print(a*b)
  case"/":
    print(a/b)
  case"%":
    print(a%b)
  case"//":
    print(a//b)





list=[]
n=int(input())
for x in range(0,n):
  ele=int(input())
  list.append(ele)
print(list)
l=len(list)
print("original list",list)
def Bubble(list):
  for i in range(0,l):
    for j in range(i+1,l):
      if(list[i]>list[j]):
        list[i],list[j]=list[j],list[i]
  print("Sorted list",list)
Bubble(list)







list=[]
n=int(input())
for x in range(0,n):
  ele=int(input())
  list.append(ele)
l=len(list)
print("Original list:",list)
def selection(list):
  for i in range(l-1):
    min=i
    for j in range(i+1,l):
      if(list[j]<list[min]):
        min=j
    list[i],list[min]=list[min],list[i]

  print("Selection sort:",list)
selection(list)









list=[]
n=int(input())
for x in range(0,n):
  ele=int(input())
  list.append(ele)
print(list)
l=len(list)
print("Original list",list)
def InsertionSort(list):
  for i in range(1,l):
    value=list[i]
    j=i-1
    while(j>=0 and value<list[j]):
      list[j+1]=list[j]
      j-=1
    list[j+1]=value
  print("Insertion sort",list)
InsertionSort(list)
