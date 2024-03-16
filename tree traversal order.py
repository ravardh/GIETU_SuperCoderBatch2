class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
        
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)
        
def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)
        
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
        
        
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(7)
root.left.left.left=node(8)
root.left.right.right=node(6)
root.right.left.left=node(11)
root.right.left.right=node(12)
root.left.right.right.left=node(9)
root.left.right.right.right=node(10)

print("postorder")
postorder(root)
print("\n")

print("preorder")
preorder(root)
print("\n")

print("inorder")
inorder(root)
print("\n")






