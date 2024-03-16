class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, value):
        if root is None:
            return Node(value)
        
        if value < root.data:
            root.left = self.insert(root.left, value)
        elif value > root.data:
            root.right = self.insert(root.right, value)
        
        root.height = 1 + max(self.ght(root.left), self.ght(root.right))
        
        bl = self.bal(root)
        if bl > 1 and value < root.left.data:
            return self.rightRotate(root)
        
        if bl < -1 and value > root.right.data:
            return self.leftRotate(root)
        
        if bl > 1 and value > root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        if bl < -1 and value < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root
     def ght(self, root):
        if root is None:
            return 0
        return root.height

    def bal(self, root):
        if root is None:
            return 0
        return self.ght(root.left) - self.ght(root.right)

    def leftRotate(self, A):
        B = A.right
        temp = B.left

        B.left = A
        A.right = temp

        A.height = 1 + max(self.ght(A.left), self.ght(A.right))
        B.height = 1 + max(self.ght(B.left), self.ght(B.right))

        return B

    def rightRotate(self, B):
        A = B.left
        temp = A.right

        A.right = B
        B.left = temp

        B.height = 1 + max(self.ght(B.left), self.ght(B.right))
        A.height = 1 + max(self.ght(A.left), self.ght(A.right))

        return A
 def inOrder(self, root):
        if root == None:
            return
        self.inOrder(root.left)
        print(root.data,end=" ")
        self.inOrder(root.right)

root = None
keys = [50, 45, 55, 35, 40, 48, 60, 20, 70, 41, 47, 42, 15, 22, 25, 30, 90]

avlTree = AVLTree()
for x in keys:
    root = avlTree.insert(root, x)

avlTree.inOrder(root)