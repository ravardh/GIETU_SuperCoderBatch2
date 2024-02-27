class node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
def findleaf(root):
    if root==None:
        return 
    
    elif(root.left==None and root.right==None):
        print(root.data)
    findleaf(root.left)
    findleaf(root.right)
    
root=node(20)
root.left=node(32)
root.right=node(10)
root.left.left=node(15)
root.left.right=node(12)
root.right.left=node(8)
root.right.right=node(24)
root.left.left.left=node(4)
root.left.right.left=node(50)
root.left.right.right=node(6)
root.right.right.left=node(16)
root.right.right.right=node(2)
root.left.right.left.left=node(40)
root.left.right.left.right=node(35)
findleaf(root)