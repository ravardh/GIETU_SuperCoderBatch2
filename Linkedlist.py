class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def print_linked_list(head):
    temp = head
    while temp:
        print(temp.data, end=" -> " if temp.next else "\n")
        temp = temp.next

def add_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def add_at_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node
    return head


newNode = Node(1)
start = newNode

start.next = Node(2)
start.next.next = Node(3)
start.next.next.next = Node(4)
start.next.next.next.next = Node(5)

print("Original linked list:")
print_linked_list(start)

# Add a node at the beginning
start = add_at_beginning(start, 0)
print("\nLinked list after adding a node at the beginning:")
print_linked_list(start)

# Add a node at the end
start = add_at_end(start, 6)
print("\nLinked list after adding a node at the end:")
print_linked_list(start)
