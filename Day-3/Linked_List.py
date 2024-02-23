class node:
  def __init__(self,data=None):
    self.data=data
    self.next=None
def insertAtend(head):
  n=int(input("enter how many elements You want to insert:-"))
  if head is None:
    head = node(int(input("Enter data: ")))
    current = head
  else:
    current=head
    while current.next is not None:
      current=current.next
    for i in range(0,n):
          new_node = node(int(input("enter data:-")))
          current.next=new_node
          current=current.next
  return head
def insertAtBeg(head):
  n=int(input("enter how many elements You want to insert:-"))
  for i in range(0, n):
      current=head
      new_node = node(int(input("enter data:-")))
      new_node.next=head
      head=new_node
  return head
def insertAtAny(head):
    pos=int(input("enter the position"))
    current=head
    for i in range(pos-2):
        current=current.next
    new_node=node(int(input("enter data")))
    new_node.next=current.next
    current.next=new_node
def deleteAtend(head):
    if head is not None:
        current=head
        while(current.next.next is not None):
            current=current.next
        temp=current.next
        current.next=None
    else:
        print("Empty dear!")
def deleteAtbeg(head):
    if head is not None:
        current=head
        head=head.next
        current.next=None
    else:
        print("Empty dear!")
    return head
def deleteAtAny(head):
    if head is not None:
        pos = int(input("enter the position"))
        current = head
        for i in range(pos - 2):
            current = current.next
        current.next=current.next.next
    else:
        print("Empty dear!")
def display(head):
      temp=head
      print("the List is:-",end="")
      while(temp):
        print(temp.data,end=" ")
        temp=temp.next
head=None
option=0
while(option!=8):
    print()
    print("1:for insert at begining")
    print("2:for insert at end")
    print("3:insert at any position")
    print("4:delete at end")
    print("5:delete at any position")
    print("6:for delete at begining")
    print("7:for Display the list")
    print("8:for exit")
    option=int(input("Which one you want:-"))
    match(option):
        case 1:
            head=insertAtBeg(head)
        case 2:
            head=insertAtend(head)
        case 3:
            insertAtAny(head)
        case 4:
            deleteAtend(head)
        case 5:
            deleteAtAny(head)
        case 6:
            head=deleteAtbeg(head)
        case 7:
            display(head)
        case 8:
            print("Thanks for Visit!")
            exit()
        case _:
            print("enter a valid option")