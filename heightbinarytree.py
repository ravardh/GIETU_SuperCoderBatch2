class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def maxheight(node):
    if node is None:
        return 0
    else:

        lheight=maxheight(node.left)
        rheight=maxheight(node.right)

        if(lheight>rheight):
            return lheight+1
        else:
            return rheight+1
root=Node(1)
root.left=Node(7)
root.right=Node(6)
root.left.left=Node(5)
root.left.right=Node(9)
root.right.left=Node(19)
root.right.right=Node(8)

print(maxheight(root))
