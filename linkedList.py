class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

newNode = Node(1)
start = newNode

start.next = Node(2)
start.next.next = Node(3)
start.next.next.next = Node(4)
start.next.next.next.next = Node(5)

temp = start
print("Linked list:")
while temp:
    print(temp.data)
    temp = temp.next

n1 = Node(0)
n1.next = start
start = n1
print("\nNode added at the beginning:")
temp = start
while temp:
    print(temp.data)
    temp = temp.next

n2 = Node(6)
temp = start
while temp.next:
    temp = temp.next
temp.next = n2
print("\nNode added at the end:")
temp = start
while temp:
    print(temp.data)
    temp = temp.next
