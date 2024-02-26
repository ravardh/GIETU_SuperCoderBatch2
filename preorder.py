class node:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None

def tree(root):

    if(root==None):
        return

    print(root.data)
    tree(root.left)
    tree(root.right)
    
root=node(1) #root
root.left=node(2)#left of the root
root.right=node(4)
root.left.left=node(3)
root.left.right=node(6)
root.right.left=node(5)
root.right.right=node(7)

print("the root value is",root)
print("preorder is ",root.data,end="  ")
tree(root)




