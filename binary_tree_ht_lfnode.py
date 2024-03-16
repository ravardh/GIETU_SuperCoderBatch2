class node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        
#Height of a binary tree
def findHeight(root):
   if root is None:
       return 0
   return 1 + max(findHeight(root.left),findHeight(root.right))

#Print the leaf nodes of a tree
def leafNode(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        print(root.data, end=" ")
        return
    if root.left:
        leafNode(root.left)
    if root.right:
        leafNode(root.right)

root = node(20)
root.left = node(32)
root.right = node(10)
root.left.left = node(15)
root.left.right = node(12)
root.right.left = node(8)
root.right.right = node(24)
root.left.left.left = node(4)
root.left.right.left = node(50)
root.left.right.right = node(6)
root.left.right.left.left = node(40)
root.left.right.left.right = node(35)
root.right.right.left = node(16)
root.right.right.right = node(2)

print("The height of the tree is:", findHeight(root))
print("The LeafNodes of the tree are: ",leafNode(root))

