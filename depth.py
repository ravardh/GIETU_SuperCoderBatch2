class node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

def findheight(root):
    if root is None:
        return 0
    else:
        lheight = findheight(root.left)
        rheight = findheight(root.right)
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

root = node(1)
root.left = node(32)
root.right = node(10)
root.left.left = node(15)
root.left.right = node(12)
root.right.left = node(8)
root.right.right = node(24)

print(findheight(root))