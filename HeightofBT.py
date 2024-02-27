class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def height(root):
    if root == None:
        return 0
    else:
        l = height(root.left)
        r = height(root.right)
        if(l > r):
            return l+1
        else:
            return r+1
root= Node(1)
root.left=Node(2)
root.right=Node(4)
root.left.left=Node(3)
root.left.right=Node(6)   
root.right.left=Node(5)
root.right.right=Node(7)
print("Maximum height of tree is ",height(root))
        