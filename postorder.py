class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def postorderTraversal(root):
    if root is None:
        return []
    result = []
    result.extend(postorderTraversal(root.left))
    result.extend(postorderTraversal(root.right))
    result.append(root.val)
    return result
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print("Postorder traversal:", postorderTraversal(root))