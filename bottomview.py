from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bottom_view(root):
    if not root:
        return []

    bottom_nodes = {}


    queue = deque([(root, 0)])

    while queue:
        node, hd = queue.popleft()

        bottom_nodes[hd] = node.val

        if node.left:
            queue.append((node.left, hd - 1))

        if node.right:
            queue.append((node.right, hd + 1))

    sorted_bottom_nodes = sorted(bottom_nodes.items())

    return [val for _, val in sorted_bottom_nodes]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.left = TreeNode(7)
root.right.left.right = TreeNode(8)


print(bottom_view(root))  
