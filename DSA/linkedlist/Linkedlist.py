class Node:
    def __init__(self, data: str):
        self.data: str = data
        self.next: Node | None = None


class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    def insert(self, data: str) -> None:
        newNode: Node = Node(data)
        if self.head is None:
            self.head = newNode
            return

        ptr: Node | None = self.head
        while ptr.next is not None:
            ptr = ptr.next

        ptr.next = newNode

    def delete(self) -> None:
        if self.head is not None:
            ptr: Node | None = self.head.next
            prevPtr: Node | None = self.head
            while ptr.next is not None:
                ptr = ptr.next
                prevPtr = prevPtr.next

            prevPtr.next = None

    def insertBegin(self, data: str) -> None:
        if self.head is None:
            self.insert(data)
            return

        newNode: Node = Node(data)
        newNode.next = self.head
        self.head = newNode

    def deleteBegin(self) -> None:
        if self.head is None:
            return

        self.head = self.head.next

    def insertAt(self, data: str, index: int) -> None:
        if self.head is None:
            self.insert(data)
            return
        newNode: Node = Node(data)
        ptr: Node = self.head
        for i in range(index):
            if ptr is None:
                print("List ended before index")
                return
            ptr = ptr.next

        newNode.next = ptr.next
        ptr.next = newNode

    def deleteAt(self, index: int) -> None:
        if self.head is None:
            return

        ptr: Node = self.head.next
        prevPtr: Node = self.head
        for i in range(index):
            if prevPtr is None:
                print("List ended before index")
                return
            ptr = ptr.next
            prevPtr = prevPtr.next

        prevPtr.next = ptr.next

    def search(self, data: str) -> None:
        ptr: Node | None = self.head
        index: int = 0
        while ptr is not None:
            if ptr.data == data:
                print(index)
            ptr = ptr.next
            index += 1

    def display(self) -> None:
        ptr: Node | None = self.head
        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next

    def displayRecursive(self):
        self.__privateDisplay(self.head)

    def __privateDisplay(self, ptr: Node | None):
        if ptr is None:
            return

        print(ptr.data)
        self.__privateDisplay(ptr.next)


if __name__ == '__main__':
    linkedlist: LinkedList = LinkedList()
    linkedlist.insert("Abhisek")
    linkedlist.insert("is")
    linkedlist.insert("a")
    linkedlist.insert("good")
    linkedlist.insert("boy")
    linkedlist.delete()
    linkedlist.insertBegin("Yup")
    linkedlist.deleteBegin()
    linkedlist.insertAt("Yey", 2)
    linkedlist.deleteAt(2)
    linkedlist.display()
    linkedlist.displayRecursive()
    linkedlist.search("is")
