class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.left: Node | None = None
        self.right: Node | None = None


class BinarySearchTree:
    def __init__(self):
        self.root: Node | None = None

    def insert(self, data: int):
        if self.root is None:
            self.root = Node(data)
            return
        self.__insert(self.root, data)

    def __insert(self, root: Node | None, data: int):
        newNode = Node(data)
        if root is None:
            return

        if root.data > data:
            if root.left is None:
                root.left = newNode
                return
            self.__insert(root.left, data)
        else:
            if root.right is None:
                root.right = newNode
                return
            self.__insert(root.right, data)

    def insert_backtrack(self, data):
        self.root = self.__insert_backtrack(self.root, data)

    def __insert_backtrack(self, root: Node | None, data: int):
        if root is None:
            return Node(data)

        if root.data > data:
            root.left = self.__insert_backtrack(root.left, data)
        else:
            root.right = self.__insert_backtrack(root.right, data)

        return root

    def inorder(self):
        self.__inorder(self.root)

    def __inorder(self, root: Node | None):
        if root is None:
            return
        self.__inorder(root.left)
        print(root.data)
        self.__inorder(root.right)


if __name__ == '__main__':
    binary_search_tree: BinarySearchTree = BinarySearchTree()
    binary_search_tree2: BinarySearchTree = BinarySearchTree()
    arr = [50, 36, 12, 20, 76, 18, 44, 52, 90]
    for i in arr:
        binary_search_tree.insert_backtrack(i)
        binary_search_tree2.insert(i)

    binary_search_tree.inorder()
    print("-------------")
    binary_search_tree2.inorder()
