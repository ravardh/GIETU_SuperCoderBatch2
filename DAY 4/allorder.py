class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inorder(root):
        if root == None:
            return
        
        
        inorder(root.left)
        print(root.data)
        inorder(root.right)


def preorder(root):
        if root == None:
            return
        
        print(root.data)
        preorder(root.left)
        preorder(root.right)
def postorder(root):
        if root == None:
            return
        
        
        postorder(root.left)
        postorder(root.right)
        print(root.data)

             
root =node(1)
root.left=node(2)
root.right=node(3)
root.left.right=node(5)
root.left.left=node(4)
root.right.left=node(6)
root.right.right=node(7)

print(root)
print("INORDER")
print(inorder(root))
print("PREORDER")
preorder(root)
print("POSTORDER")
postorder(root)


