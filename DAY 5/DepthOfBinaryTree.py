class node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
def findheight(root):
    if root==None:
        return 0
    Leftheight=findheight(root.left)
    Rightheight=findheight(root.right)
    if Leftheight>Rightheight:
        max=Leftheight
    else:
        max=Rightheight
    height=max+1
    return height
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)
print(findheight(root))
