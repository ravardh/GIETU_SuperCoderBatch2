class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
        self.height=1

class AVL:
    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balancefactor(self, node):
        if node is None:
            return 0
        return self.height(node.left)-self.height(node.right)

    def rr(self,B):
        A=B.left
        temp=A.right
        A.right=B
        B.left=temp
        B.height = 1+max(self.height(B.left),self.height(B.right))
        A.height = 1+max(self.height(A.left),self.height(A.right))
        return A

    def lr(self,A):
        B=A.right
        temp=B.left
        B.left=A
        A.right=temp
        A.height=1+max(self.height(A.left),self.height(A.right))
        B.height=1+max(self.height(B.left),self.height(B.right))
        return B

    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data<root.data:
            root.left=self.insert(root.left,data)
        elif data>root.data:
            root.right=self.insert(root.right,data)
        else:
            return root
        root.height=1+max(self.height(root.left),self.height(root.right))
        balance=self.balancefactor(root)
        if balance >= 2:
            if data<root.left.data:
                return self.rr(root)
            elif data>root.left.data:
                root.left=self.lr(root.left)
                return self.rr(root)
        if balance<=-2:
            if data>root.right.data:
                return self.lr(root)
            elif data<root.right.data:
                root.right=self.rr(root.right)
                return self.lr(root)
        return root

    def inorder_traverse(self,root):
        if root:
            self.inorder_traverse(root.left)
            print(root.data,end=' ')
            self.inorder_traverse(root.right)

tree=AVL()
root=None
array =[50, 45, 55, 35, 40, 48, 60, 20, 70, 41, 47, 42, 15, 22, 25, 30, 90]
for data in array:
    root=tree.insert(root,data)

print("Preorder Traversal of AVL Tree:")
tree.inorder_traverse(root)
