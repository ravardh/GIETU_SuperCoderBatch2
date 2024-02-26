class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def max_Depth(root):
    if root is None:
        return 0
    else:
        left_depth = max_Depth(root.left)
        right_depth = max_Depth(root.right)
        return max(left_depth, right_depth) + 1

def print_leaf_nodes(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        print(root.data)
    print_leaf_nodes(root.left)
    print_leaf_nodes(root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(4)
root.left.left = TreeNode(19)
root.left.right = TreeNode(14)
root.right.left = TreeNode(6)
root.right.right = TreeNode(12)
root.left.right.left = TreeNode(9)
root.left.right.right = TreeNode(5)
root.right.left.right = TreeNode(16)
root.left.right.left.right = TreeNode(10)
root.right.right.left = TreeNode(8)
root.right.right.right = TreeNode(11)
root.right.right.right.left = TreeNode(17)
root.right.right.right.right = TreeNode(20)

print(max_Depth(root))
print_leaf_nodes(root)
