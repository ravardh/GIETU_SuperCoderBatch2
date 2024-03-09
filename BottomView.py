class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.horizontal_distance = 0
def bottom_view(root):
    if not root:
        return []
    result = {}
    queue = [(root, 0)]

    while queue:
        current, hd = queue.pop(0)
        result[hd] = current.value
        if current.left:
            queue.append((current.left, hd - 1))
        if current.right:
            queue.append((current.right, hd + 1))
    bottom_view_nodes = [result[hd] for hd in sorted(result.keys())]
    return bottom_view_nodes
root = TreeNode(20)
root.left = TreeNode(8)
root.right = TreeNode(22)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(25)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(14)
result = bottom_view(root)
print(result)
