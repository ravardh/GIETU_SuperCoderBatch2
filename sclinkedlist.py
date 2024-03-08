class node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1=node(10)
node2=node(20)
node3=node(30)
node4=node(40)

head=node1
node1.next=node2
node2.next=node3
node3.next=node4

current=head
while(current!=None):
    print(current.data,end= "->")
    current=current.next
print("None")

newnode=node(1)
newnode.next=node1
current=newnode
while(current!=None):
    print(current.data,end= "->")
    current=current.next
print("None")

newnode=node(50)
newnode.next=None
node4.next=newnode
current=head
while(current!=None):
    print(current.data,end= "->")
    current=current.next
print("None")

newnode=node(60)
newnode.next=node3
node2.next=newnode
current=head
while(current!=None):
    print(current.data,end= "->")
    current=current.next
print("None")

current=node2
while(current!=None):
    print(current.data,end="->")
    current=current.next
print("None")

current=node1
while(current!=node4):
    print(current.data,end="->")
    current=current.next
print("None")

current=head
while(current!=node3):
    current=current.next
current.next=current.next.next
current=head
while(current!=None):
    print(current.data,end= "->")
    current=current.next
print("None")
