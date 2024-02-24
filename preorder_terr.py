class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printPreOrder(node):
    if node is None:
        return
    print(node.data)
    printPreOrder(node.left)
    printPreOrder(node.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(22)
    root.right = Node(53)
    root.left.left = Node(84)
    root.left.right = Node(88)
    root.right.left = Node(63)
    root.right.right = Node(97)

    print("Preorder Traversal: ", end="")
    printPreOrder(root)
