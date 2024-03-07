class node:
    def __init__(self,data):
        self.data = data
        self.left=None
        self.right=None
        self.height=None

class AvlTree:
    def __init__(self):
        self.root=None

    def height(self,node):
        if node is None:
            return 0
        return node.height

    def balance(self,node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def RotateRight(self,y):
        x = y.left
        T2=x.right

        x.right=y
        y.left=T2

        y.height = 1 + max(self.height(y.left),self.height(y.right))
        x.height = 1 + max(self.height(x.left),self.height(x.right))
        return x

    def RotateLeft(self,x):
        y=x.right
        T2=y.left

        y.left=y 
        x.right=T2

        x.height = 1 + max(self.height(x.left),self.height(x.right))
        y.height = 1 + max(self.height(y.left),self.height(y.right))
        return y

    def insert(self,node,data):
        if node is None:
            return node(data)
        elif data<node.data:
            node.left=self.insert(node.left,data)
        else:
            node.right = self.insert(node.right,data)

        node.height = 1 + max(self.height(node.left),self.height(node.right,data))
        balance= self.balance(node)
        if balance > 1:
            if data < node.left.data:
                return self.rotate_right(node)
            else:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

        if balance < -1:
            if data > node.right.data:
                return self.rotate_left(node)
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

        return node  

    def insert_data(self,data):
        self.root = self.insert(self.root, data)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

    def inorder(self):
        self.inorder_traversal(self.root)

avl_tree = AvlTree()
elements = [50, 45, 55, 35, 40, 48, 60, 20, 70, 41, 47, 42, 15, 22, 25, 30, 90]
for element in elements:
    avl_tree.insert_data(elements)



print("Inorder Traversal of AVL Tree:")
avl_tree.inorder()