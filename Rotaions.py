class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, B):
        A = B.left
        temp = A.right

        A.right = B
        B.left = temp

        B.height = 1 + max(self.height(B.left), self.height(B.right))
        A.height = 1 + max(self.height(A.left), self.height(A.right))

        return A

    def left_rotate(self, A):
        B = A.right
        temp = B.left

        B.left = A
        A.right = temp

        A.height = 1 + max(self.height(A.left), self.height(A.right))
        B.height = 1 + max(self.height(B.left), self.height(B.right))

        return B

    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        else:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.balance_factor(root)

        if balance >= 2:
            if data < root.left.data:
                return self.right_rotate(root)
            elif data > root.left.data:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance <= -2:
            if data > root.right.data:
                return self.left_rotate(root)
            elif data < root.right.data:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def inOrder_traversal(self, root):
        if root:
            self.inOrder_traversal(root.left)
            print(root.data, end=' ')
            self.inOrder_traversal(root.right)


# Example usage
avl_tree = AVL()
root = None
array = [50, 45, 55, 35, 40, 48, 60, 20, 70, 41, 47, 42, 15, 22, 25, 30, 90]

for data in array:
    root = avl_tree.insert(root, data)

print("Preorder Traversal of AVL Tree:")
avl_tree.inOrder_traversal(root)
