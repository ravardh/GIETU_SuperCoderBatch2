class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.data:
        root.left = insert(root.left, value)
    elif value > root.data:
        root.right = insert(root.right, value)
    return root

def pre_order(root, lst):
    if root is None:
        return
    lst.append(root.data)
    pre_order(root.left, lst)
    pre_order(root.right, lst)

lst = []
root = Node(90)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 50)
root = insert(root, 70)
root = insert(root, 20)
root = insert(root, 80)

pre_order(root, lst)
print(lst)
