class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    if data<root.data:
        root.left=insert(root.left, data)
    elif data>root.data:
        root.right=insert(root.right, data)

    return root

def preOrder_traversal(root):
    if root:
        preOrder_traversal(root.left)
        print(root.data,end=' ')
        preOrder_traversal(root.right)
root = None
array = [50,36,39,66,75,19,98,76,105,22,42,21]
for data in array:
    root = insert(root, data)
print("prerder Traversal:")
preOrder_traversal(root)
