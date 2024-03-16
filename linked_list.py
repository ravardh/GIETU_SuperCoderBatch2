class Node:
    def __init__(self,data):    #Creating a linked list
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    #Insertion at Beginning in Linked List
    def insertbegin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        else:
            new_node.next=self.head
            self.head=new_node
            
    #Insertion at End in Linked List
    def insertend(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=new_node

    #Insert a Node at a Specific Position in Linked List
    def insertindex(self,data,index):
        new_node=Node(data)
        temp=self.head
        position=0
        if(position==index):
            insertbegin(data)
        else:
            while(temp!=None and position+1!=index):
                position+=1
                temp=temp.next
            if temp!=None:
                new_node.next=temp.next
                temp.next=new_node
            else:
                print("Index not present")

    #deletion of a node at specific position
    def delindex(self,index):
        if self.head==None:
            return
        temp=self.head
        position = 0
        if position == index:
            self.head=self.head.next
        else:
            while(temp!=None and position+1!=index):
                position = position+1
                temp=temp.next
            if temp!=None:
                temp.next=temp.next.next
            else:
                print("Index not present")

    #print the list
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

lst=LinkedList()
lst.insertbegin(2)
lst.insertend(6)
lst.insertend(3)
lst.insertbegin(8)
lst.insertindex(12,1)

print("The list is")
lst.printlist()

lst.delindex(2)
print("After deletion")
lst.printlist()
