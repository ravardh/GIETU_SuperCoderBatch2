
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def leafnodecount(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1
    else:
        leftleaf_count = leafnodecount(root.left)
        rightleaf_count = leafnodecount(root.right)
        return leftleaf_count + rightleaf_count

# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

leaf_count = leafnodecount(root)
print("Number of leaf nodes in the binary tree:", leaf_count)
