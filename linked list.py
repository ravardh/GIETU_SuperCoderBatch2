class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

start =  Node(1)
start.next =  Node(2)
start.next.next =  Node(3)
start.next.next.next =  Node(4)
start.next.next.next.next =  Node(5)
temp=start
while temp:
    print(temp.data,end=" ")
    temp=temp.next
#begining
print("\nAdding node at the beginning:",end=" ")
begin=Node(0)
begin.next=start
start=begin
temp = start
while temp:
    print(temp.data,end=" ")
    temp=temp.next
#ending
endNode=Node(6)
temp = start
while temp.next:
    temp=temp.next
temp.next=endNode
print("\nAdding node at the end:",end=" ")
temp = start
while temp:
    print(temp.data,end=" ")
    temp=temp.next
#desired location
desiredNode=Node(10)
position=3
temp=start
while temp.next:
    position=position-1
    if position == 1:
        desiredNode.next = temp.next
        temp.next=desiredNode
        break
    temp = temp.next
    

print("\nAdding node at the given location:",end=" ")
temp = start
while temp:
    print(temp.data,end=" ")
    temp=temp.next
