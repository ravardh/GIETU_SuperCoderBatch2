
class Node:
    def _init_(self,data):
       self.data = data
       self.head = None

class  LinkedList:
    def _init_(self):
        self.head = None
    
    def insertAtBegin(self,data):
        new_node = Node(data)
        new_node.next=self.head
        self.head = new_node

    def insertAtEnd(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while(last_node.next):
            last_node = last_node.next
        last_node.next = new_node
        new_node.next = None
           

    def display(self):
        current = self.head
        while(current):
            print(current.data , end=" -> ")
            current = current.next
        print("None")

linked_list = LinkedList()
linked_list.insertAtBegin(3)
linked_list.insertAtBegin(2)
linked_list.insertAtBegin(1)
linked_list.insertAtEnd(4)
linked_list.insertAtEnd(5)

linked_list.display()