class treenode(object):
    def __init__(self, data):
        self.data = data
        self.l = None
        self.r = None
        self.h = 1
class AVLTree(object):

    def insert(self, root, key):

        if not root:
            return treenode(key)
        elif key < root.data:
            root.l = self.insert(root.l, key)
        else:
            root.r = self.insert(root.r, key)

        root.h = 1 + max(self.getHeight(root.l),
                         self.getHeight(root.r))

        b = self.getBal(root)

        if b > 1 and key < root.l.data:
            return self.rRotate(root)

        if b < -1 and key > root.r.data:
            return self.lRotate(root)

        if b > 1 and key > root.l.data:
            root.l = self.lRotate(root.l)
            return self.rRotate(root)

        if b < -1 and key < root.r.data:
            root.r = self.rRotate(root.r)
            return self.lRotate(root)
        return root

    def lRotate(self, z):
        y = z.r
        T2 = y.l
        y.l = z
        z.r = T2
        z.h = 1 + max(self.getHeight(z.l),self.getHeight(z.r))
        y.h = 1 + max(self.getHeight(y.l),self.getHeight(y.r))

        return y
    def rRotate(self, z):
        y = z.l
        T3 = y.r
        y.r = z
        z.l = T3
        z.h = 1 + max(self.getHeight(z.l),self.getHeight(z.r))
        y.h = 1 + max(self.getHeight(y.l),self.getHeight(y.r))
        return y

    def getHeight(self, root):
        if not root:
            return 0
        return root.h

    def getBal(self, root):
        if not root:
            return 0
        return self.getHeight(root.l) - self.getHeight(root.r)

    def preOrder(self, root):

        if not root:
            return

        print("{0} ".format(root.data), end="")
        self.preOrder(root.l)
        self.preOrder(root.r)


Tree = AVLTree()
root = None

root = Tree.insert(root, 50)
root = Tree.insert(root, 45)
root = Tree.insert(root, 55)
root = Tree.insert(root, 35)
root = Tree.insert(root, 40)
root = Tree.insert(root, 48)
root = Tree.insert(root, 60)
root = Tree.insert(root, 20)
root = Tree.insert(root, 70)
root = Tree.insert(root, 41)
root = Tree.insert(root, 47)
root = Tree.insert(root, 42)
root = Tree.insert(root, 15)
root = Tree.insert(root, 22)
root = Tree.insert(root, 25)
root = Tree.insert(root, 30)
root = Tree.insert(root, 90)

print("Preorder traversal of the","constructed AVL tree is")
Tree.preOrder(root)
print()
