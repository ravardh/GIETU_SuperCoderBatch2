class node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

def pre(root):
    if(root==None):
        return
    print(root.data)
    pre(root.left)
    pre(root.right)
def ino(root):
    if(root==None):
        return
    ino(root.left)
    print(root.data)
    ino(root.right)
def pos(root):
    if(root==None):
        return
    pos(root.left)
    pos(root.right)
    print(root.data)
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)
print("preorder")
pre(root)
print("inorder")
ino(root)
print("postorder")
pos(root)



    
