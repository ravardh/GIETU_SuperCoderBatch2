class Node:
    def __init__(self, data: str):
        self.data: str = data
        self.left: Node | None = None
        self.right: Node | None = None

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None


class Tree:
    def __init__(self):
        self.root: Node | None = None

    def preorder(self):
        self.__preorder(self.root)

    def inorder(self):
        self.__inorder(self.root)

    def postorder(self):
        self.__postorder(self.root)

    def __preorder(self, root: Node | None):
        if root is None:
            return
        print(root.data)
        self.__preorder(root.left)
        self.__preorder(root.right)

    def __inorder(self, root: Node | None):
        if root is None:
            return
        self.__inorder(root.left)
        print(root.data)
        self.__inorder(root.right)

    def __postorder(self, root: Node | None):
        if root is None:
            return

        self.__postorder(root.left)
        self.__postorder(root.right)
        print(root.data)


if __name__ == '__main__':
    tree: Tree = Tree()

    tree.root = Node("1")
    tree.root.left = Node("2")
    tree.root.right = Node("4")
    tree.root.left.left = Node("3")
    tree.root.left.right = Node("6")
    tree.root.right.left = Node("5")
    tree.root.right.right = Node("7")

    tree.preorder()
    print("__________")
    tree.postorder()
    print("__________")
    tree.inorder()
