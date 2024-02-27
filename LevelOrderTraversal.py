class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def levelOrderTraversal(root):
    if root is None:
        return
    
    queue = [root]

    while queue:
        current_node = queue.pop(0)
        print(current_node.value, end=" ")

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

 
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Level Order Traversal:")
levelOrderTraversal(root)
