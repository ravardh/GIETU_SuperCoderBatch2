class node:
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None

def findheight(root):
    if(root==None):
        return 0
    leftheight = findheight(root.left)
    rightheight = findheight(root.right)
    height = (max(leftheight,rightheight)) + 1 
    return height

root=node(1)
root.left=node(2)
root.right=node(4)
root.left.left=node(19)
root.left.right=node(14)
root.right.left=node(6)
root.right.right=node(12)
root.left.right.left=node(9)
root.left.right.right=node(5)
root.left.right.left.right=node(10)
root.right.left.right=node(16)
root.right.right.left=node(8)
root.right.right.right=node(11)
root.right.right.left.left=node(15)
root.right.right.right.left=node(17)
root.right.right.right.right=node(20)

print("Depth of tree is : "+str(findheight(root)))