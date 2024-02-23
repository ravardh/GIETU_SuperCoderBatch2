class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current_node = self.head
        prev_node = None
        count = 0
        while current_node and count < position:
            prev_node = current_node
            current_node = current_node.next
            count += 1
        if current_node is None:
            print("Position out of range")
            return
        new_node.next = current_node
        prev_node.next = new_node

    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            print("Element not found")
            return
        prev_node.next = current_node.next
        current_node = None

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' -> ')
            current_node = current_node.next
        print("None")

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_beginning(1)
    linked_list.insert_at_beginning(2)
    linked_list.insert_at_end(3)
    linked_list.insert_at_position(4, 1)
    linked_list.display()

    linked_list.delete_node(2)
    linked_list.display()
