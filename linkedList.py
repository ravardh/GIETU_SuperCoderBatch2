class Node:
    def __init__(self,data):
        self.data=data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtEnd(self,data):
        new_node  = Node(data)
        if self.head ==None:
            self.head = new_node

        current_node = self.head
        while(current_node.next):
            current_node  = current_node.next
        current_node.next = new_node

    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next

    def remove_first(self):
        if self.head == None:
            return
        self.head = self.head.next

    def remove_node(self,data):
        current_node = self.head

        if current_node.data ==data:
            self.remove_first()
            return
        while current_node.next.data!=data and current_node!=None:
            current_node = current_node.next

        if current_node==None:
            return
        else:
            current_node.next = current_node.next.next

        


list1 = linkedList()
list1.insertAtBegin(14)
list1.insertAtEnd('satyam')
list1.remove_node(14)
list1.printLL()

