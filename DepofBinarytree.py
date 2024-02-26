class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def maxDepth(root):
    if root is None:
        return 0
    else:
        left_depth = maxDepth(root.left)
        right_depth = maxDepth(root.right)

        return max(left_depth, right_depth) + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left= Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)


print("Depth of the binary tree is:", maxDepth(root))
