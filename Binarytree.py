class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def inOrder(root):
    if root is not None:
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)
def preOrder(root):
    if root is not None:
        print(root.data, end=" ")
        preOrder(root.left)
        preOrder(root.right)
def postOrder(root):
    if root is not None:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=" ")
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print("Inorder=",end="")
inOrder(root)
print()
print("PreOrder=",end="")
preOrder(root)
print()
print("PostOrder=",end="")
postOrder(root)
print()
