class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def finddepth(node):
    if node is None:
        return 0
    else:
        left_depth = finddepth(node.left)
        right_depth = finddepth(node.right)
        if(left_depth>right_depth):
            return left_depth+1
        else:
            return right_depth+1
root = node(1)
root.left = node(3)
root.right = node(9)
root.left.left = node(5)
root.left.right = node(7)
root.right.left = node(4)
root.right.right = node(6)
root.left.left.right = node(8)
print("Height of the tree is: ",finddepth(root))
