class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def leafnode(root):
    if root is None:
        return 0
    elif root.left==None and root.right==None:
         print(root.data, end=" ")
    leafnode(root.left)
    leafnode(root.right)
root = node(20)
root.left = node(32)
root.right = node(10)
root.left.left = node(15)
root.left.right = node(7)
root.right.left = node(4)
root.right.right = node(6)
root.left.left.right = node(8)
leafnode(root)
