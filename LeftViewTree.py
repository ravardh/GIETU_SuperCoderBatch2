class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def left_view(root):
    left = []
    def inorder_traversal(node, level):
        nonlocal left
        if node is None:
            return
        if level == len(left):
            left.append(node.val)
        inorder_traversal(node.left, level + 1)
        inorder_traversal(node.right, level + 1)  
    inorder_traversal(root, 0)  
    return left

root = TreeNode(20)
root.left = TreeNode(32)
root.right = TreeNode(10)
root.left.left = TreeNode(15)
root.left.right = TreeNode(12)
root.right.left = TreeNode(8)
root.right.right = TreeNode(24)
root.left.left.left = TreeNode(4)
root.left.right.left = TreeNode(50)
root.left.right.right = TreeNode(6)
root.left.right.left.left = TreeNode(40)
root.left.right.left.right = TreeNode(35)
root.right.right.left = TreeNode(16)
root.right.right.right = TreeNode(2)

left_view_result = left_view(root)
print("Left view of the binary tree:", left_view_result)