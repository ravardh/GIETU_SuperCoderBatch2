class Node:
    def __init__(self, data: str):
        self.data: str = data
        self.left: Node | None = None
        self.right: Node | None = None

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None


class QObj:
    node: Node
    key: int

    def __init__(self, node: Node, key: int):
        self.node = node
        self.key = key


class Tree:
    def __init__(self):
        self.root: Node | None = None

    def preorder(self):
        self.__preorder(self.root)

    def inorder(self):
        self.__inorder(self.root)

    def postorder(self):
        self.__postorder(self.root)

    def findHeight(self) -> int:
        return self.__findHeight(self.root)

    def printLeaf(self):
        self.__printLeaf(self.root)

    def topView(self):
        queue: list = []
        view: dict = {}
        currKey: int = 0

        queue.append(QObj(self.root, currKey))
        while len(queue) != 0:
            currObj: QObj = queue.pop(0)
            currNode: Node | None = currObj.node
            currKey = currObj.key

            if currKey not in view:
                view[currKey] = currNode

            if currNode.left is not None:
                queue.append(QObj(currNode.left, currKey - 1))
            if currNode.right is not None:
                queue.append(QObj(currNode.right, currKey + 1))

        for key in view.keys():
            print(view[key].data)

    def bottom_view(self):
        if self.root is None:
            return

        queue: list = []
        view: dict = {}
        currKey: int = 0

        queue.append(QObj(self.root, currKey))
        while len(queue) != 0:
            currObj: QObj = queue.pop(0)
            currNode: Node | None = currObj.node
            currKey = currObj.key

            view[currKey] = currNode

            if currNode.left is not None:
                queue.append(QObj(currNode.left, currKey - 1))
            if currNode.right is not None:
                queue.append(QObj(currNode.right, currKey + 1))

        for key in sorted(view.keys()):
            print(view[key].data)

    def left_view(self):
        self.__left_view(self.root, 1, [0])

    def right_view(self):
        self.__right_view(self.root, 1, [0])

    def count_nodes(self) -> int:
        count: list = [0]
        self.__count_nodes(self.root, count)
        return count[0]

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

    def __findHeight(self, root: Node | None) -> int:
        if root is None:
            return 0
        leftHeight: int = self.__findHeight(root.left)
        rightHeight: int = self.__findHeight(root.right)
        return max(leftHeight, rightHeight) + 1

    def __printLeaf(self, root: Node | None):
        if root is None:
            return

        if root.right is None and root.left is None:
            print(root.data)
            return
        self.__printLeaf(root.left)
        self.__printLeaf(root.right)

    def __left_view(self, root: Node, currentLevel: int, LEVEL: list):
        if root is None:
            return

        if LEVEL[0] < currentLevel:
            print(root.data)
            LEVEL[0] = currentLevel

        self.__left_view(root.left, currentLevel + 1, LEVEL)
        self.__left_view(root.right, currentLevel + 1, LEVEL)

    def __right_view(self, root: Node, curVal: int, LEVEL: list):
        if root is None:
            return

        if LEVEL[0] < curVal:
            print(root.data)
            LEVEL[0] = curVal

        self.__right_view(root.right, curVal + 1, LEVEL)
        self.__right_view(root.left, curVal + 1, LEVEL)

    def __count_nodes(self, root: Node, count: list):
        if root is None:
            return
        count[0] = count[0] + 1
        self.__count_nodes(root.left, count)
        self.__count_nodes(root.right, count)


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
    print("_____________________")
    tree.postorder()
    print("________________")
    tree.inorder()
    print("_________________")
    print("Height is ", tree.findHeight())
    print("_______________print leaf")
    tree.printLeaf()
    print("______________top view")
    tree.topView()
    print("______________bottom view")
    tree.bottom_view()
    print("__________________left view")
    tree.left_view()
    print("__________________right view")
    tree.right_view()
    print("Total nodes ", tree.count_nodes())
