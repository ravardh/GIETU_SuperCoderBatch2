class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


def height(node):
    if node is None:
        return 0
    return node.height


def balance_factor(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)


def right_rotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x


def left_rotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y


def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    else:
        return root

    root.height = 1 + max(height(root.left), height(root.right))

    balance = balance_factor(root)

    if balance >= 2:
        if data < root.left.data:
            return right_rotate(root)
        elif data > root.left.data:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance <= -2:
        if data > root.right.data:
            return left_rotate(root)
        elif data < root.right.data:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root


def preOrder_traversal(root):
    if root:
        preOrder_traversal(root.left)
        print(root.data, end=' ')
        preOrder_traversal(root.right)
root = None
array = [50, 45, 55, 35, 40, 48, 60, 20, 70, 41, 47, 42, 15, 22, 25, 30, 90]
for data in array:
    root = insert(root, data)

print("Preorder Traversal of AVL Tree:")
preOrder_traversal(root)
