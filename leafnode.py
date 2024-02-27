class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLeafNodes(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        print(node.data, end=" ")
    printLeafNodes(node.left)
    printLeafNodes(node.right)

root = Node(1)
root.left = Node(22)
root.right = Node(53)
root.left.left = Node(84)
root.left.right = Node(88)
root.left.left.left = Node(63)
root.left.left.left.left = Node(97)

printLeafNodes(root)