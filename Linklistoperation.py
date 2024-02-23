def insertAtStart(head):
    new=Node(int(input("Enter the data:")))
    new.next=head
    head=new
    return head;

def insertAtEnd(head):
    temp=head
    while temp.next!=None:
        temp=temp.next
    if temp.next==None:
        new=Node(int(input("Enter the data:")))
        temp.next=new

def insertAtMiddle(head):
    temp=head
    b=1
    c=int(input("Enter the index number:"))
    while b<=c:
        b+=1
        temp=temp.next
    new=Node(int(input("Enter the data:")))
    new.next=temp.next
    temp.next=new
def display(head):
  curr=head
  while curr:
      print(curr.data,end="-")
      curr=curr.next
  print("Null")

class Node:
    def __init__(self, data=None):
        self.data=data
        self.next=None
a=int(input("Enter the number of nodes: "))
i=0
head=None
cur=None
while i<a:
    new=Node(int(input("Enter the data: ")))
    if i==0:
        head=new
        cur=head
    else:
        cur.next=new
        cur=new
    i+=1

c=int(input("Enter a number:"))
match(c):
    case 1:
        head=insertAtStart(head)
        display(head)
    case 2:
        insertAtEnd(head)
        display(head)
    case 3:
        insertAtMiddle(head)
        display(head)
    case _:
        print("Choose right option.")
