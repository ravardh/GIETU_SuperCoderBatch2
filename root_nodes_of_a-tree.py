class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def print_leaf_nodes(root):
    if root is not None:
        if root.left is None and root.right is None:
                print(root.value)
        else:
            print_leaf_nodes(root.left)
            print_leaf_nodes(root.right)
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print("Leaf nodes of the binary tree:")
print_leaf_nodes(root)
