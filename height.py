class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def findHeight(root):
    if(root == None):
        return
    else:
        LeftHeight=findHeight(root.left)
        RightHeight=findHeight(root.right)

        if(LeftHeight>RightHeight):
            return LeftHeight+1
        else:
            return RightHeight+1

root=node(20)
root.left=node(32)
root.left.left=node(15)
root.left.left.left=node(3)
root.left.right=node(4)
root.left.right.left=node(6)
print(findHeight(root))






        