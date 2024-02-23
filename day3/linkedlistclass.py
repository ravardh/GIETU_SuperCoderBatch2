class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

newNode = node(1)
start = newNode

start.next = node(2)
start.next.next = node(3)
start.next.next.next = node(4)
start.next.next.next.next = node(5)

temp = start
print(temp.data)
while temp.next:
    temp = temp.next
    print(temp.data)

n1 = node(0)
n1.next = start
start = n1
print("Node added to the beginning")

temp = start
print(temp.data)
while temp.next:
    temp = temp.next
    print(temp.data)

n2 = node(6)
temp = start
while temp.next:
    temp = temp.next
temp.next = n2
print("Node added to the End")

temp = start
print(temp.data)
while temp.next:
    temp = temp.next
    print(temp.data)
