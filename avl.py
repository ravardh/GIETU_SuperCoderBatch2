class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = self.right = None


class AVLTree:
    def height(self, node):
        return node.height if node else 0

    def update_height(self, node):
        if node:
            node.height = 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    def rotate_right(self, y):
        x, T2 = y.left, y.left.right
        x.right, y.left = y, T2
        self.update_height(y)
        self.update_height(x)
        return x

    def rotate_left(self, x):
        y, T2 = x.right, x.right.left
        y.left, x.right = x, T2
        self.update_height(x)
        self.update_height(y)
        return y

    def insert(self, root, key):
        if not root:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        self.update_height(root)
        balance = self.balance_factor(root)

        if balance > 1:
            if key < root.left.key:
                return self.rotate_right(root)
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance < -1:
            if key > root.right.key:
                return self.rotate_left(root)
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    def inorder(self, root):
        return (self.inorder(root.left) + [root.key] + self.inorder(root.right)) if root else []

    def __init__(self):
        self.root = None

    def inorder_traversal(self):
        return self.inorder(self.root) if self.root else []


avl_tree = AVLTree()
keys = [9, 5, 10, 0, 6, 11, -1, 1, 2]
for key in keys:
    avl_tree.insert_key(key)

print(avl_tree.inorder_traversal())
