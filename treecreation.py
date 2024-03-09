class node:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None
def traverse(root):
    if(root==None):
        return
    traverse(root.left)
    print(root.data,end="")
    traverse(root.right)
def preorder(root):
    if(root==None):
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)
def postorder(root):
    if(root==None):
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end="")
root=node(1)
root.left=node(2)
root.right=node(4)
root.left.left=node(3)
root.left.right=node(6)
root.right.left=node(5)
root.right.right=node(7)

print(root)
print(root.data)
traverse(root)
preorder(root)
postorder(root)