from collections import deque

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def bottom_view(root):
    if not root:
        return []

    result = {}
    queue = deque([(root, 0)])

    while queue:
        node, level = queue.popleft()
        result[level] = node.val

        if node.left:
            queue.append((node.left, level - 1))
        if node.right:
            queue.append((node.right, level + 1))

    sorted_result = [result[key] for key in sorted(result)]

    return sorted_result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.left.right.right = TreeNode(5)
root.left.right.right.right = TreeNode(6)

print(bottom_view(root))
