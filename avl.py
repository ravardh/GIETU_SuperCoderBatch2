class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and key < root.left.key:
            return self.rotateRight(root)
        if balance < -1 and key > root.right.key:
            return self.rotateLeft(root)
        if balance > 1 and key > root.left.key:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)
        if balance < -1 and key < root.right.key:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def rotateRight(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rotateLeft(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def insertArray(self, arr):
        for key in arr:
            self.root = self.insert(self.root, key)

    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            print(root.key, end=" ")
            self.inorderTraversal(root.right)


# Example usage:
if __name__ == "__main__":
    arr = [50,45,55,35,40,48,60,20,70,41,47,42,15,22,25,30,90]
    tree = AVLTree()
    tree.insertArray(arr)

    print("Inorder traversal of the constructed AVL tree:")
    tree.inorderTraversal(tree.root)
