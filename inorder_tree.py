class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data)
        printInorder(root.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(22)
    root.right = Node(53)
    root.left.left = Node(84)
    root.left.right = Node(88)
    root.right.left = Node(63)
    root.right.right = Node(97)

    print("Preorder Traversal: ", end="")
    printInorder(root)