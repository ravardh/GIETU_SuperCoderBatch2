class node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None

def insert(root,value):
    if root == None:
        return node(value)
    if(value<root.data):
        root.left = insert(root.left,value)
    elif value>root.data:
        root.right = insert(root.right,value)
    return root

def preorder(root):
    if root == None:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

root= None
V_L = [50,36,12,20,44,76,18,44,52,90]
for x in V_L:
    root = insert(root,x)

print(root)
preorder(root)