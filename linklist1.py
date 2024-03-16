
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()
def add_values_to_linked_list(linked_list, values):
    for value in values:
        linked_list.append(value)
if __name__ == "__main__":
    linked_list = LinkedList()
    n = int(input("Enter the number of values: "))
    values = [int(input("Enter value: ")) for i in range(n)]
    add_values_to_linked_list(linked_list, values)
    print("Linked List:")
    linked_list.display()
