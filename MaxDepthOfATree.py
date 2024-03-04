class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def maxdepth(root):
    if root is None:
        return 0
    else:
        left_depth = maxdepth(root.left)
        right_depth = maxdepth(root.right)
        return max(left_depth, right_depth) + 1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
depth = maxdepth(root)
print("Depth of the binary tree:", depth)