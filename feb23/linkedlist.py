class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def create_linked_list():
    linked_list = LinkedList()
    n = int(input("How many elements do you want to add to the linked list? "))
    for _ in range(n):
        data = input("Enter element: ")
        linked_list.insert(data)
    return linked_list

if __name__ == "__main__":
    linked_list = create_linked_list()
    print("Linked List:")
    linked_list.display()
