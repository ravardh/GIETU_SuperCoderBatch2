class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def right_view(root):
    if root is None:
        return []

    result = []
    queue = [root]

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            current_node = queue.pop(0)

            if i == level_size - 1:
                result.append(current_node.data)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

print(right_view(root))
