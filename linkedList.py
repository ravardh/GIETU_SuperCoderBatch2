class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.size=1

    def insertAtFirst(self,data):
        new_node=Node(data)
        new_node.next = self.head
        self.head=new_node
        
    def insertAtLast(self,data):
        new_node=Node(data)
        temp=self.head
        while temp.next != None:
            temp=temp.next
        temp.next=new_node
        
    def insert(self,data,index):
        new_node=Node(data)
        if(index==0):
            self.insertAtFirst(data)
        temp=self.head
        for i in range(1,index):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node
            
    def findLength(self):
        temp=self.head
        length=1
        while temp.next:
           length=length+1
           temp=temp.next
        return length

    def insertAtMid(self,data):
        mid=self.findLength()//2
        new_node=Node(data)
        temp=self.head
        for i in range(1,mid):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node
        
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end="->")
            current_node = current_node.next
        print("None")
        
    def deleteFirst(self):
        temp=self.head
        if(temp.next==None):
            print("Empty linked list")
        else:
            temp=temp.next
            self.head=temp
            
    def deleteLast(self):
        temp=self.head
        if(temp.next==None):
            print("Empty linked list")
        while temp.next.next:
            temp=temp.next
        temp.next=None
    
    def deleteAtPos(self,pos):
        if pos==0:
            self.deleteFirst()
        temp=self.head
        for i in range(1,pos):
            temp=temp.next
        temp.next=temp.next.next

# Example usage:
llist = LinkedList()
llist.insertAtFirst(1)
llist.insertAtFirst(2)
llist.insertAtFirst(3)
llist.insertAtFirst(4)
llist.insertAtFirst(5)

llist.insertAtLast(10)

llist.insertAtMid(25)

llist.deleteFirst()
llist.print_list()
llist.deleteLast()
# print("Length -> ",llist.findLength())
llist.print_list()
llist.deleteAtPos(3)
llist.print_list()

