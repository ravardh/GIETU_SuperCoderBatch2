class node:
  def __init__(self,data=None):
    self.data=data
    self.next=None

n1 = node(1)
n2 = node(2)
n3 = node(3)
n4 = node(4)
n5 = node(5)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5

Start = temp = n1

while temp:
  print(temp)
  print(temp.data)
  temp=temp.next