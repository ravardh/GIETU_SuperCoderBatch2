class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Create a linked list
linked_list = LinkedList()

# Add nodes at the beginning
linked_list.add_at_beginning(3)
linked_list.add_at_beginning(2)
linked_list.add_at_beginning(1)

# Display the linked list
linked_list.display()
