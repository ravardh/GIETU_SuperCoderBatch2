class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.count=1

    def checkEmpty(self):
        return self.head is None
    
    def pushBack(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

        self.count=self.count+1
    
    def pushFront(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pushMid(self,data):
        size=self.findSize()
        mid=size//2
        temp=self.head
        count=1
        while(count != mid):
            temp=temp.next
            count=count+1
        
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node
        self.count += 1


    def deleteNode(self, key):
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
            return
        prev_node.next = current_node.next
        current_node = None

    def deleteLast(self):
        temp=self.head
        while(temp.next.next):
            temp=temp.next

        temp.next=None

    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")
    
    def findSize(self):
        return self.count
    
    
node = LinkedList()
node.pushBack(1)
node.pushBack(2)
node.pushBack(4)
node.pushBack(7)
node.printLL()
node.pushMid(5)
node.printLL()
